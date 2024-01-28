# WebSocket Server-Client Implementations using Tornado and Starlette

This project involves the implementation of 2 WebSocket server-client modules using the Tornado framework and Starlette library in Python. The server streams real-time data, and the client actively listens to this data flow. Main goal is to compare the performance results of these 2 applications.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- ccxt library

- Tornado library

- Starlette and Uvicorn library

### Installation

1. Clone the repo
2. Install Python packages

### Usage

## For Tornado App
- **Run the server script**:
    python tornado_server.py

- **Run the client script**:
    python tornado_client.py

## For Starlette/Uvicorn App
- **Run the server script**:
uvicorn starlette_server:app --host 0.0.0.0 --port 8888
- **Run the client script**:
    python starlette_client.py

- **High Load Test**
The high load test simulates a high load scenario by sending a large number of messages concurrently.

## Test Environment

The tests were conducted under the following environment:

- **Data Type/Size Streamed**: The data streamed is a JSON object that includes the price and timestamp. The size of this data in bytes is 97.

- **Hardware Details**:
    - **CPU**: Apple M1 Pro
    - **RAM**: 16 GB
    - **Operating System**:
        - ***macOS:*** 14.0 (23A344)
        - ***Operating System:*** Darwin 23.0.0
        - ***Kernel Version:*** Darwin Kernel Version 23.0.0
        - ***Release Date of Kernel Version:*** Fri Sep 15 14:41:43 PDT 2023
        - ***Machine Hardware Name:*** arm64

- **Number of Cores and Threads Utilized**: The tests were run using a single core and a thread.

## Test Results

### High Load Test For Tornado Application
- With 10 clients:
    - Mean response time: 0.2627 seconds
    - Median response time: 0.2628 seconds
    - Standard deviation of response time: 0.0002 seconds
    - Number of errors: 0

- With 100 clients:
    - Mean response time: 0.2681 seconds    
    - Median response time: 0.2683 seconds  
    - Standard deviation of response time: 0.0005 seconds   
    - Number of errors: 0   

- With 1000 clients:
    - Mean response time: 0.3345 seconds
    - Median response time: 0.3318 seconds
    - Standard deviation of response time: 0.0443 seconds
    - Number of errors: 93

### High Load Test For Starlette/Uvicorn Application
- With 10 clients:
    - Mean response time: 0.4611 seconds
    - Median response time: 0.0014 seconds
    - Standard deviation of response time: 1.2438 seconds
    - Number of errors: 0
- With 100 clients:
    - Mean response time: 15.0040 seconds
    - Median response time: 15.8675 seconds
    - Standard deviation of response time: 10.2929 seconds
    - Number of errors: 0

### Tornado Client Test

- Test Duration: 60 seconds
- Total messages: 190
- Throughput: 3.15 messages/second
- Average Latency: 0.3172 seconds/message
- Average Message Size: 96.91 bytes/message
- Errors: 0
- CPU Usage: 0.2%
- Memory Usage: 25.73 MB

### Starlette/Uvicorn Client Test

- Test Duration: 60 seconds
- Total messages: 716
- Throughput: 11.91 messages/second
- Average Latency: 0.0840 seconds/message
- Average Message Size: 96.69 bytes/message
- Errors: 0
- CPU Usage: 0.2%
- Memory Usage: 26.09 MB

## Findings

### High Load Test For Tornado Application
- Tornado performs well under high load conditions with up to 100 clients, showing consistent and low response times.
- However, with 1000 clients, the response time increases, and a significant number of errors (93) are observed. This suggests a potential scalability limitation.

### High Load Test For Starlette/Uvicorn Application
- Starlette/Uvicorn exhibits degraded performance under high load conditions, especially with 100 clients. The response times are considerably higher, and the standard deviation indicates variability in responses.
- While errors are not observed, the overall performance is not as robust as Tornado under similar conditions.

### Tornado Client Test
- Tornado client demonstrates stable performance over a 60-second test duration, with low latency, low CPU usage, and minimal memory consumption.
- Throughput and average latency metrics indicate efficient message processing.

### Starlette/Uvicorn Client Test
- Starlette/Uvicorn client performs well in terms of throughput and average latency, showcasing a higher throughput compared to the Tornado client.
- CPU and memory usage are similar to the Tornado client, indicating efficient resource utilization.

## Conclusion

- Tornado shows better performance and scalability under high load conditions compared to Starlette/Uvicorn in the tested scenarios.
- Tornado's ability to handle a large number of clients with low response times makes it a suitable choice for applications requiring high concurrency.
- Starlette/Uvicorn, while performing well in certain conditions, might need optimizations to match the scalability and responsiveness of Tornado, especially under high loads. Considerations should be given to the specific requirements of the application and the trade-offs between frameworks.
