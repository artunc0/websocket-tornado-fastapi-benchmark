import os
import json
import asyncio
import ccxt
import tornado.ioloop
import tornado.web
import tornado.websocket
import logging
from websocket_handler import WebSocketHandler

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
async def stream_real_time_data():
    exchange = ccxt.binance({
        'apiKey': api_key,
        'secret': api_secret,
    })
    symbol = 'BTC/USDT'

    while True:
        try:
            ticker = exchange.fetch_ticker(symbol)
            price = round(ticker['last'], 4)
            data = {
                'price': price,
                'timestamp': ticker['timestamp'] / 1000
            }

            message = json.dumps(data)

            gather_tasks = [
                asyncio.ensure_future(client.write_message(message)) for client in WebSocketHandler.clients.values()
            ]

            await asyncio.gather(*gather_tasks)

            await asyncio.sleep(0.005)

        except ccxt.NetworkError as ne:
            logging.error(f"Network error: {ne}")
            await asyncio.sleep(5)  # Retry after 5 seconds on network error

        except ccxt.ExchangeError as ee:
            logging.error(f"Exchange error: {ee}")
            await asyncio.sleep(10)  # Retry after 10 seconds on exchange error

        except Exception as e:
            logging.error(f"Error fetching and streaming data: {e}")

if __name__ == "__main__":
    application = tornado.web.Application([(r"/websocket", WebSocketHandler)])
    application.listen(8888)
    logging.info("Tornado WebSocket server listening on port 8888")

    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    tornado.ioloop.IOLoop.current().spawn_callback(stream_real_time_data)
    tornado.ioloop.IOLoop.current().start()
