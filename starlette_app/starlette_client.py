import os
import json
import asyncio
import websockets
import time
import sys
import psutil

async def main():
    start_time = time.perf_counter()  # Record start time
    test_duration = 5  # Set the test duration in seconds

    total_messages = 0
    total_size = 0
    errors = 0
    url = "ws://localhost:8888/websocket"
    async with websockets.connect(url) as websocket:
        await websocket.send('Hello, server!')

        process = psutil.Process(os.getpid())
        start_cpu = process.cpu_percent()

        while True:
            current_time = time.perf_counter()
            if current_time - start_time >= test_duration:
                break

            try:
                msg = await websocket.recv()
                print("msg: ",msg)
                if msg is None:
                    # Connection closed unexpectedly
                    print("Connection closed before the test duration.")
                    break

                total_messages += 1
                total_size += sys.getsizeof(msg)
            except Exception as e:
                errors += 1

        # Calculate throughput and latency after the test duration
        elapsed_time = current_time - start_time
        throughput = total_messages / elapsed_time
        latency = elapsed_time / total_messages if total_messages > 0 else 0
        avg_msg_size = total_size / total_messages if total_messages > 0 else 0

        end_cpu = process.cpu_percent()
        cpu_usage = end_cpu - start_cpu
        memory_usage = process.memory_info().rss

        print(f"\nTest Duration: {test_duration} seconds")
        print(f"Total messages: {total_messages}")
        print(f"Throughput: {throughput:.2f} messages/second")
        print(f"Average Latency: {latency:.4f} seconds/message")
        print(f"Average Message Size: {avg_msg_size:.2f} bytes/message")
        print(f"Errors: {errors}")
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage / (1024 * 1024):.2f} MB")

if __name__ == "__main__":
    asyncio.run(main())
