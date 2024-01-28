import asyncio
import time
import logging
import tornado.websocket

logger = logging.getLogger('my_application')

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    clients = {}
    last_access_time = {}
    client_id = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._compression_options = {}

    async def open(self):
        WebSocketHandler.client_id += 1
        self.id = WebSocketHandler.client_id
        logger.info(f'WebSocket opened for client {self.id}')
        WebSocketHandler.clients[self.id] = self
        WebSocketHandler.last_access_time[self.id] = time.time()
        await asyncio.sleep(1)

    def on_message(self, message):
        try:
            current_time = time.time()
            last_access_time = WebSocketHandler.last_access_time.get(self.id, 0)
            elapsed_time = current_time - last_access_time

            if elapsed_time < 1:
                logger.warning(f'Rate limit exceeded for client {self.id}. Ignoring message.')
                return

            logger.info(f'Received message from client {self.id}: {message}')
            WebSocketHandler.last_access_time[self.id] = current_time
            
        except Exception as e:
            logger.error('Error handling incoming message', exc_info=True)

    def on_close(self):
        logger.info(f'WebSocket closed for client {self.id}')
        del WebSocketHandler.clients[self.id]
        del WebSocketHandler.last_access_time[self.id]
