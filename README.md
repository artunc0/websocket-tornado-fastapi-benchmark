# WebSocket Server-Client Implementation using Tornado

This project involves the implementation of a WebSocket server-client using the Tornado framework in Python. The server streams real-time data, and the client actively listens to this data flow.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- Tornado library
- ccxt library

### Installation

1. Clone the repo
2. Install Python packages

### Usage
- **Run the server script**:
    python tornado_server.py

- **Run the client script**:
    python tornado_client.py

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

### Tornado Client Test

- Test Duration: 60 seconds
- Total messages: 190
- Throughput: 3.15 messages/second
- Average Latency: 0.3172 seconds/message
- Average Message Size: 96.91 bytes/message
- Errors: 0
- CPU Usage: 0.2%
- Memory Usage: 25.73 MB
