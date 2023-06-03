import numpy as np
from python_speech_features import mfcc
import pyaudio
import pickle
import wave
import time
import scipy.io.wavfile as wav
import os

def speaker_recognition():
    # Load GMM model from file
    model_file = '/Users/vaiebhavchettri/Documents/gui/gmm_model.pkl'
    # model_file = '/Users/vaiebhavchettri/Desktop/newmodel.pkl'

    with open(model_file, 'rb') as f:
        gmm = pickle.load(f)

    # Configure audio stream
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024

    # Prompt user to speak
    print("Speak now for 5 seconds")
    time.sleep(1)

    # Record audio from microphone and save to file
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    frames = []
    for i in range(int(RATE / CHUNK * 5)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save audio to file
    filename = 'recordedaudio.wav'
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    # Extract MFCC features from audio
    rate, new_audio = wav.read(filename)
    new_mfccs = mfcc(new_audio, rate, numcep=13, nfft=2048)

    # Predict speaker
    num_frames = new_mfccs.shape[0]
    speaker_probs = gmm.predict_proba(new_mfccs.reshape(num_frames, -1))
    predicted_speaker = np.argmax(speaker_probs)

    # Return predicted speaker
    speakers = ['SaiIshwarya', 'syed', 'VAIEBHAV']
    if 0 <= predicted_speaker < len(speakers):
          return speakers[predicted_speaker]
    else:
          return "Unknown"
  


# import numpy as np
# from python_speech_features import mfcc
# import pyaudio
# import pickle
# import wave
# import time
# import scipy.io.wavfile as wav

# # Load GMM model from file
# model_file = '/Users/vaiebhavchettri/Documents/gui/gmm_model.pkl'
# with open(model_file, 'rb') as f:
#     gmm = pickle.load(f)

# # Configure audio stream
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 44100
# CHUNK = 1024

# # Prompt user to speak
# print("Speak now for 5 seconds")
# time.sleep(1)

# # Record audio from microphone and save to file
# p = pyaudio.PyAudio()
# stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
# frames = []
# for i in range(int(RATE / CHUNK * 5)):
#     data = stream.read(CHUNK)
#     frames.append(data)
# stream.stop_stream()
# stream.close()
# p.terminate()

# # Save audio to file
# filename = 'recorded_audio.wav'
# with wave.open(filename, 'wb') as wf:
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(p.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))

# # Extract MFCC features from audio
# rate, new_audio = wav.read(filename)
# new_mfccs = mfcc(new_audio, rate, numcep=13, nfft=2048)

# # Predict speaker
# num_frames = new_mfccs.shape[0]
# speaker_probs = gmm.predict_proba(new_mfccs.reshape(num_frames, -1))
# predicted_speaker = np.argmax(speaker_probs)

# # Print predicted speaker
# speakers = ['SAI ISHWARYA', 'SAI SMARAN', 'VAIEBHAV']
# if 0 <= predicted_speaker < len(speakers):
#     print(f"Predicted speaker: {speakers[predicted_speaker]}")
# else:
#     print("Could not predict speaker.")



# import time
# import numpy as np
# from python_speech_features import mfcc
# import pyaudio
# import pickle

# def speaker_recognition():
#     # Load GMM model from file
#     model_file = '/Users/vaiebhavchettri/Documents/gui/gmm_model.pkl'
#     with open(model_file, 'rb') as f:
#         gmm = pickle.load(f)

#     # Configure audio stream
#     FORMAT = pyaudio.paInt16
#     CHANNELS = 1
#     RATE = 44100
#     CHUNK = 1024

#     # Prompt user to speak
#     print("Speak now for 5 seconds")
#     time.sleep(1)

#     # Record audio from microphone and extract features
#     p = pyaudio.PyAudio()
#     stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
#     frames = []
#     for i in range(int(RATE / CHUNK * 5)):
#         data = stream.read(CHUNK)
#         frames.append(data)
#     stream.stop_stream()
#     stream.close()
#     p.terminate()

#     # Extract MFCC features from audio
#     audio = np.frombuffer(b''.join(frames), dtype=np.int16)
#     mfccs = mfcc(audio, RATE, numcep=13, nfft=2048)

#     # Predict speaker
#     num_frames = mfccs.shape[0]
#     speaker_probs = gmm.predict_proba(mfccs.reshape(num_frames, -1))
#     predicted_speaker = np.argmax(speaker_probs)

#     # Return predicted speaker
#     speakers = ['SAI ISHWARYA', 'SAI SMARAN', 'VAIEBHAV']
#     return speakers[predicted_speaker]
