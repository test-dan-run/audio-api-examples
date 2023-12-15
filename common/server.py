"""
Start up the flask server using "python3 server.py"
"""
import io
import logging

import soundfile as sf
from flask import Flask, request, jsonify

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d \
:: %(message)s', level = logging.DEBUG)

app = Flask(__name__)

@app.route('/decode_audio', methods=['POST'])
def decode_audio():
    try:
        # Receive the audio bytes from the request
        audio_bytes = request.data

        # load with soundfile, data will be a numpy array
        data, samplerate = sf.read(io.BytesIO(audio_bytes))
        logging.debug(f"data type  : {type(data)}")
        logging.debug(f"data shape : {data.shape}")
        logging.debug(f"sample rate: {samplerate}")

        # do whatever you want with the array
        # over here, I'm testing if the audio file can be regenerated and sounds the same
        sf.write("decoded_audio.wav", data, samplerate)

        return jsonify({'message': 'Audio decoded successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
