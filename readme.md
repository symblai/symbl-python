# Symbl Python SDK

The Symbl Python SDK provides convenient access to the Symbl API from applications written in the Python language. It includes a pre-defined set of classes for a simple and clear utilization of APIs.

## Documentation

See the [Python API docs](https://docs.symbl.ai/docs/).

### Requirements

- Python 2.7+ or Python 3.4+ (PyPy supported)

## Installation

First make sure that Python is installed in your system.

To install the python, just click on the system which you are using:

- [Windows](https://phoenixnap.com/kb/how-to-install-python-3-windows)

- [Mac](https://flaviocopes.com/python-installation-macos/)

You don't need this source code unless you want to modify the package. If you just
want to use the package, then you can install it, either using 'pip' or with 'source':

>just run the command mentioned below to install using 'pip':

```sh
pip install --upgrade symbl
```

>or you can also install the package with source:

```sh
python setup.py install
```

## Configuration

To initialize the SDK, you need to provide app_id and app_token which you can get by signing up on [Symbl Platform][api-keys].

You can either provide the api_keys by saving a file named symbl.conf in your working directory or home directory in the following format.

>Home directory will be C:/Users/\<Your Username\> on your windows system, or ~ in your Linux or Mac system.

```conf
[credentials]
app_id=<app_id>
app_secret=<app_secret>
```
>Example for 'symbl.conf' file

```conf
[credentials]
app_id=1234567890 #Update with your app_id, without any quotes
app_secret=abcdefghijklmnop #Update with your app_secret, without any quotes
```
### Usages

The library needs to be configured with your account's credentials (appId & appSecret) which is
available in your [Symbl Platform][api-keys].

## A speech to text converter under 5 lines of code

To know more about **Async Audio API**, see the [Async Audio API docs][async_audio-docs]. To know more about the Python SDK Audio Package, see the docs for [Audio class][extended_readme-audio].

```python
import symbl

# Process audio file
conversation = symbl.Audio.process_file(
  # credentials={app_id: <app_id>, app_secret: <app_secret>}, #Optional, Don't add this parameter if you have symbl.conf file in your home directory
  file_path=<file_path>)

# Printing transcription messages
print(conversation.get_messages())
```

To know more about conversation object and its functions, see the docs on [conversation object][extended_readme-conversation-object].

## Extracting insights from Textual conversation

To know more about **Async Text Api**, see [Async Text API docs][async_text-docs]. To know more about the Python SDK Text Package, see the docs for [Text class][extended_readme-text].

  ``` python

import symbl

payload = {
  "messages": [
    {
      "payload": {"content": "Hi Anthony. I saw your complaints about bad call reception on your mobile phone. Can I know what issues you are currently facing?"},
      "from": {"userId": "surbhi@example.com","name": "Surbhi Rathore"}
    },
    {
      "payload": {"content": "Hey Surbhi, thanks for reaching out. Whenever I am picking up the call there is a lot of white noise and I literally can’t hear anything."},
      "from": {"userId": "anthony@example.com","name": "Anthony Claudia"}
    },
    {
      "payload": {"content": "Okay. I can schedule a visit from one of our technicians for tomorrow afternoon at 1:00 PM. He can look at your mobile and handle any issue right away"},
      "from": {"userId": "surbhi@example.com","name": "Surbhi Rathore"}
    },
    {
      "payload": {"content": "That will be really helpful. I'll follow up with the technician about some other issues too, tomorrow"},
      "from": {"userId": "anthony@example.com","name": "Anthony Claudia"}
    },
    {
      "payload": {"content": "Sure. We are happy to help. I am scheduling the visit for tomorrow. Thanks for using Abccorp networks. Have a good day."},
      "from": {"userId": "surbhi@example.com","name": "Surbhi Rathore"}
    }
  ]
}

conversation = symbl.Text.process(payload=payload)

print(conversation.get_action_items())
print(conversation.get_topics())
print(conversation.get_follow_ups())

  ```

## Analysis of your Zoom Call on your email (Symbl will join your zoom call and send you analysis on provided email)

To know more about **Telephony API**, see the docs on [Telephony API][telephony_api-docs]. To know more about the Python SDK Telephony Package, see the docs for [Telephony class][extended_readme-telephony].

```python

import symbl

phoneNumber = "" # Zoom phone number to be called, check here https://us02web.zoom.us/zoomconference
meetingId = "" # Your zoom meetingId
password = "" # Your zoom meeting passcode
emailId = ""

connection = symbl.Telephony.start_pstn(
      # credentials={app_id: <app_id>, app_secret: <app_secret>}, #Optional, Don't add this parameter if you have symbl.conf file in your home directory or working directory
      phone_number=phoneNumber,
      dtmf = ",,{}#,,{}#".format(meetingId, password),
      actions = [
        {
          "invokeOn": "stop",
          "name": "sendSummaryEmail",
          "parameters": {
            "emails": [
              emailId
            ],
          },
        },
      ]
    )

print(connection)

```

## Live audio transcript using your system's microphone

To know more about **Streaming API**, see the docs on [Streaming API][streaming_api-docs]. To know more about the Python SDK Streaming Package, see the docs for the [Streaming class][extended_readme-streaming].

```python
import symbl

connection = symbl.Streaming.start_connection()

connection.subscribe({'message_response': lambda response: print('got this response from callback', response)})

connection.send_audio_from_mic()
```

## Extended Readme

You can see all the functions provided by SDK in the **extended [readme.md][extended-readme] file**.

You can go through some examples for understanding the use of all functionality [Explore more example](https://github.com/symblai/symbl-python/tree/roshani_readme_changes/example)

## Possible Errros

1. PortAudio Errors on Mac Systems:-

   If you're getting PortAudio Error which looks like this
    > sounddevice.PortAudioError: Error opening InputStream: Internal PortAudio error [PaErrorCode -9986]
  
   Please consider updating the PortAudio library in your system. Running the following command can help.
    > brew install portaudio

## Need support

If you are looking for some specific use cases do check our [examples][examples] folder.

If you can't find your answers, do let us know at support@symbl.ai or join our [slack channel][slack-invite].

[api-keys]: https://platform.symbl.ai/#/login
[symbl-docs]: https://docs.symbl.ai/docs/
[streaming_api-docs]: https://docs.symbl.ai/docs/streamingapi/introduction
[telephony_api-docs]: https://docs.symbl.ai/docs/telephony/introduction
[async_text-docs]: https://docs.symbl.ai/docs/async-api/overview/text/post-text/
[async_audio-docs]: https://docs.symbl.ai/docs/async-api/overview/audio/post-audio
[extended-readme]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md
[extended_readme-conversation-object]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#conversation-object
[extended_readme-streaming]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#streaming-class
[extended_readme-telephony]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#telephony-class
[extended_readme-text]: <https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#text-class>
[extended_readme-audio]: https://github.com/symblai/symbl-python/blob/main/symbl/readme.md#audio-class
[examples]: https://github.com/symblai/symbl-python/tree/main/example
[unicodeerror]: https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca
[slack-invite]: https://symbldotai.slack.com/join/shared_invite/zt-4sic2s11-D3x496pll8UHSJ89cm78CA#/
