import asyncio
import time
import websockets
import json
import statistics
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('high_load_test')

async def simulate_high_load():
    url = "ws://localhost:8888/websocket"
    response_times = []
    errors = 0

    async def connect_and_send_message():
        nonlocal errors
        try:
            async with websockets.connect(url, timeout=5) as ws:
                message = {"type": "high_load", "content": "High load message"}
                start_time = time.time()
                await ws.send(json.dumps(message))
                response = await ws.recv()  # Assuming the server sends a response
                end_time = time.time()
                response_time = end_time - start_time
                response_times.append(response_time)
        except Exception as e:
            logger.error(f"Error in high load simulation: {e}")
            errors += 1

    # Create a list of tasks to run concurrently
    tasks = [connect_and_send_message() for _ in range(100)]

    # Run the tasks concurrently
    await asyncio.gather(*tasks)

    # Calculate and log aggregate statistics
    if response_times:
        logger.info(f"Mean response time: {statistics.mean(response_times):.4f} seconds")
        logger.info(f"Median response time: {statistics.median(response_times):.4f} seconds")
        logger.info(f"Standard deviation of response time: {statistics.stdev(response_times):.4f} seconds")
    logger.info(f"Number of errors: {errors}")

if __name__ == "__main__":
    asyncio.run(simulate_high_load())
