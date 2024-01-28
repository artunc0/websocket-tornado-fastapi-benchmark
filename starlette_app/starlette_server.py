import os
import json
import asyncio
import ccxt
from starlette.applications import Starlette
from starlette.websockets import WebSocket, WebSocketDisconnect
from starlette.routing import WebSocketRoute
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')

exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
})

symbol = 'BTC/USDT'

clients = set()
clients_lock = asyncio.Lock() 
message_queue = asyncio.Queue()

async def fetch_data():
    while True:
        try:
            ticker = exchange.fetch_ticker(symbol)
            price = round(ticker['last'], 4)
            data = {
                'price': price,
                'timestamp': ticker['timestamp'] / 1000
            }

            message = json.dumps(data)
            await message_queue.put(message)

            await asyncio.sleep(0.005)

        except ccxt.NetworkError as ne:
            logging.error(f"Network error: {ne}")
            await asyncio.sleep(5)  # Retry after 5 seconds on network error

        except ccxt.ExchangeError as ee:
            logging.error(f"Exchange error: {ee}")
            await asyncio.sleep(10)  # Retry after 10 seconds on exchange error

        except Exception as e:
            logging.error(f"Error fetching data: {e}")

async def stream_real_time_data(websocket: WebSocket):
    while True:
        message = await message_queue.get()
        await websocket.send_text(message)

async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
    except Exception as e:
        logging.error(f"Error during websocket handshake: {e}")
        return

    async with clients_lock:  # New: Use the lock when modifying the clients set
        clients.add(websocket)

    try:
        # New: Use a separate task for each client to send messages
        await asyncio.gather(
            stream_real_time_data(websocket),
            return_exceptions=True,
        )
    finally:
        async with clients_lock:  # New: Use the lock when modifying the clients set
            clients.remove(websocket)

app = Starlette(routes=[
    WebSocketRoute('/websocket', websocket_endpoint)
])

# Start the data fetcher
asyncio.create_task(fetch_data())
