from symbl.configs.configs import SYMBL_WEBSOCKET_BASE_PATH, X_API_KEY_HEADER
from symbl.AuthenticationToken import get_api_header
import threading
import json
import websocket

class Connection():

    def __init__(self, conversationId: str, connectionId: str, resultWebSocketUrl: str, eventUrl: str, credentials=None):
        
        self.conversation_id = conversationId
        self.credentials = credentials
        self.connectionId = connectionId
        self.resultWebSocketUrl = resultWebSocketUrl
        self.eventUrl = eventUrl
        access_token = get_api_header(self.credentials).get(X_API_KEY_HEADER)
        self.header = "{}:{}".format(X_API_KEY_HEADER, access_token)
        self.connection = None

    def __on_message_handler(self, data, event_callbacks):
        try:
            if data != None and type(data) == str:  
                json_data = json.loads(data)
                if 'type' in json_data and json_data['type'] in event_callbacks:
                    event_callbacks[json_data['type']](data) 
        except Exception as error:
            print(error)

    def async_subscribe(self, event_callbacks: dict = {}):
        if event_callbacks != None or event_callbacks != {}:
            print("Eshtablishing connection")
            self.connection = websocket.WebSocketApp(url=SYMBL_WEBSOCKET_BASE_PATH + self.connectionId, header=[self.header])
            print("Connection Eshtablished")

            self.connection.on_message = lambda this, data : self.__on_message_handler(data=data, event_callbacks=event_callbacks)
            self.connection.on_error = lambda self, error : print(error)

            self.connection.run_forever()
        else:
            print("Can not subscribe to empty events")

    def subscribe(self, event_callbacks: dict):
        try:
            thread = threading.Thread(target=self.async_subscribe, args=(event_callbacks,))
            thread.start()
        except (KeyboardInterrupt, SystemExit):
            self.stop()
            print("Exiting")

    def stop(self):
        self.connection.send(data=str({
            'type': 'stop_request'
        }))
        self.connection.close()