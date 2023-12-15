"""
Run "python3 request.py" after starting up the flask server in "server.py"
"""
import requests

SERVER_URL = 'http://localhost:5000/decode_audio'

def send_audio(filename):
    # Read audio file as bytes
    with open(filename, 'rb') as file:
        audio_bytes = file.read()

    # Send audio bytes to the backend
    response = requests.post(SERVER_URL, data=audio_bytes)

    # Print the response from the backend
    print(response.json())

if __name__ == '__main__':
    send_audio('test.wav')
