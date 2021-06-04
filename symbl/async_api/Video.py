from symbl.Conversations import Conversation
from symbl import AuthenticationToken
from symbl_rest import AsyncApi as async_api_rest
from symbl.utils.Logger import Log

def initialize_api_client(function):
    def wrapper(*args, **kw):
        credentials = None
        self = args[0]
        
        if 'credentials' in kw:
            credentials = kw['credentials']

        api_client = AuthenticationToken.get_api_client(credentials)
        self.async_api_rest = async_api_rest(api_client)

        return function(*args, **kw)
    
    return wrapper

def correct_boolean_values(dictionary: dict):
    for key in dictionary:
        if dictionary[key] == True:
            dictionary[key] = "true"
        elif dictionary[key] == False:
            dictionary[key] = "false"
    return dictionary

class Video():

    def __init__(self, api_client=None):
        '''
            It will initialize the Analysis class
            with the object of Initialize Class
        '''
        self.__async_api_rest = async_api_rest(api_client)

    @initialize_api_client
    def process_file(self, file_path:str, credentials=None, content_type:str='video/mp4', wait:bool=True, parameters={}):
        '''
            video files to be analyzed
            returns Conversation object
        '''
        if file_path == None:
            raise ValueError("Please enter a valid file_path")

        file = open(file_path, 'rb')
        video_file = file.read()
        response = self.__async_api_rest.add_video(body=video_file, content_type=content_type, **correct_boolean_values(parameters))
        Log.getInstance().info("Job with jobId {} for conversationId {} started".format(response.job_id, response.conversation_id))

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)


    @initialize_api_client
    def process_url(self, url:str, credentials=None, wait:bool=True, parameters={}):
        '''
            url of audio file to be analyzed
            returns Conversation object
        '''

        if url == None:
            raise ValueError("Please enter a valid url.")

        response = self.__async_api_rest.add_video_url(body={ 'url': url }, **correct_boolean_values(parameters))
        Log.getInstance().info("Job with jobId {} for conversationId {} started".format(response.job_id, response.conversation_id))

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)


    @initialize_api_client
    def append_file(self, file_path:str, conversation_id:str, credentials=None, content_type:str='video/mp4', wait:bool=True, parameters={}):
        '''
            video files to be appended
            returns Conversation object
        '''
        if file_path == None:
            raise ValueError("Please enter a valid file_path")

        if conversation_id == None or len(conversation_id) == 0:
            raise ValueError("Please enter a valid conversation_id")

        file = open(file_path, 'rb')
        video_file = file.read()
        response = self.__async_api_rest.append_video(body=video_file, content_type=content_type, conversation_id=conversation_id, **correct_boolean_values(parameters))
        Log.getInstance().info("Job with jobId {} for conversationId {} started".format(response.job_id, response.conversation_id))

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)


    @initialize_api_client
    def append_url(self, url : str, conversation_id:str, credentials=None, wait:bool=True, parameters={}):
        '''
            url of video file to be appended
            returns Conversation object
        '''
        if url == None:
            raise ValueError("Please enter a valid url")

        if conversation_id == None or len(conversation_id) == 0:
            raise ValueError("Please enter a valid conversation_id")

        response = self.__async_api_rest.append_video_url(body={ 'url': url }, conversation_id=conversation_id, **correct_boolean_values(parameters))
        Log.getInstance().info("Job with jobId {} for conversationId {} started".format(response.job_id, response.conversation_id))

        return Conversation(response.conversation_id, response.job_id, wait=wait, credentials=credentials)