import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import cv2
import os
import numpy as np
import pyaudio
import wave

class AttendanceSystemGUI:
    def __init__(self):
        # Create a main window
        self.root = tk.Tk()
        self.root.title("Attendance System")

        # Create the buttons
        self.capture_btn = tk.Button(self.root, text="Capture Image", width=20, command=self.capture_image)
        self.record_btn = tk.Button(self.root, text="Record Audio", width=20, command=self.record_audio)
        self.run_btn = tk.Button(self.root, text="Run System", width=20, command=self.run_system)

        # Create the labels
        self.image_label = tk.Label(self.root, text="Captured Image", font=("Arial", 14))
        self.audio_label = tk.Label(self.root, text="Recorded Audio", font=("Arial", 14))

        # Create the image and audio placeholders
        self.image_placeholder = tk.Label(self.root)
        self.audio_placeholder = tk.Label(self.root)

        # Position the widgets using the grid layout
        self.capture_btn.grid(row=0, column=0, padx=10, pady=10)
        self.record_btn.grid(row=0, column=1, padx=10, pady=10)
        self.run_btn.grid(row=0, column=2, padx=10, pady=10)
        self.image_label.grid(row=1, column=0, padx=10, pady=10)
        self.audio_label.grid(row=1, column=1, padx=10, pady=10)
        self.image_placeholder.grid(row=2, column=0, padx=10, pady=10)
        self.audio_placeholder.grid(row=2, column=1, padx=10, pady=10)

        # Start the GUI
        self.root.mainloop()

    def capture_image(self):
        # Code to capture image from camera
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        # Save the captured image to a file
        img_file = "captured_image.png"
        cv2.imwrite(img_file, frame)

        # Display the captured image in the GUI
        image = Image.open(img_file)
        image = image.resize((300, 300))
        photo = ImageTk.PhotoImage(image)
        self.image_placeholder.configure(image=photo)
        self.image_placeholder.image = photo

    # def record_audio(self):
    #     chunk = 1024
    #     channels = 1
    #     sample_rate = 44100
    #     duration = 5
    #     format = pyaudio.paInt16

    #     # Create the PyAudio object and start the audio stream
    #     audio = pyaudio.PyAudio()
    #     stream = audio.open(format=format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk)

    #     # Start recording audio
    #     frames = []
    #     for i in range(int(sample_rate / chunk * duration)):
    #         data = stream.read(chunk)
    #         frames.append(data)

    #     # Stop the audio stream and terminate the PyAudio object
    #     stream.stop_stream()
    #     stream.close()
    #     audio.terminate()

    #     # Save the recorded audio to a file
    #     audio_file = "recorded_audio.wav"
    #     wf = wave.open(audio_file, "wb")
    #     wf.setnchannels(channels)
    #     wf.setsampwidth(audio.get_sample_size(format))
    #     wf.setframerate(sample_rate)
    #     wf.writeframes(b"".join(frames))
    #     wf.close()

    #     # Play back the recorded audio to confirm
    #     wf = wave.open(audio_file, "rb")
    #     stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)
    #     data = wf.readframes(chunk)

    #     while data:
    #         stream.write(data)
    #         data = wf.readframes(chunk)

    #     stream.stop_stream()
    #     stream.close()
    #     audio.terminate()

    #     # Display a message to indicate that audio recording is complete
    #     messagebox.showinfo("Record Audio", "Audio recording complete!")

    #     # Display the recorded audio file in the GUI
    #     audio = Image.open(audio_file)
    #     audio = audio.resize((300, 100))
    #     photo = ImageTk.PhotoImage(audio)
    #     self.audio_placeholder.configure(image=photo)
    #     self.audio_placeholder.image = photo

    def run_system(self):
        self.system_window = tk.Toplevel(self.root)
        self.system_window.title("Attendance System")

        # Add a label for the image capture section
        image_label = tk.Label(self.system_window, text="Capture Image", font=("Arial", 16))
        image_label.pack(pady=10)

        # Add a button to capture the image
        image_button = tk.Button(self.system_window, text="Capture Image", command=self.capture_image)
        image_button.pack()

        # Add a label for the audio recording section
        audio_label = tk.Label(self.system_window, text="Record Audio", font=("Arial", 16))
        audio_label.pack(pady=10)

        # Add a button to record audio
        audio_button = tk.Button(self.system_window, text="Record Audio", command=self.record_audio)
        audio_button.pack()

        # Add a label to display the verification status
        self.status_label = tk.Label(self.system_window, text="", font=("Arial", 24))
        self.status_label.pack(pady=50)

    def capture_image(self):
        # Code to capture image from camera
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        # Save the captured image to a file
        img_file = "captured_image.png"
        cv2.imwrite(img_file, frame)

        # Display the captured image in the GUI
        image = Image.open(img_file)
        image = image.resize((300, 300))
        photo = ImageTk.PhotoImage(image)
        self.image_placeholder.configure(image=photo)
        self.image_placeholder.image = photo
        pass

    def record_audio(self):
        chunk = 1024
        channels = 1
        sample_rate = 44100
        duration = 5
        format = pyaudio.paInt16

        # Create the PyAudio object and start the audio stream
        audio = pyaudio.PyAudio()
        stream = audio.open(format=format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk)

        # Start recording audio
        frames = []
        for i in range(int(sample_rate / chunk * duration)):
            data = stream.read(chunk)
            frames.append(data)

        # Stop the audio stream and terminate the PyAudio object
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Save the recorded audio to a file
        audio_file = "recorded_audio.wav"
        wf = wave.open(audio_file, "wb")
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames))
        wf.close()

        # Play back the recorded audio to confirm
        wf = wave.open(audio_file, "rb")
        stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)
        data = wf.readframes(chunk)

        while data:
            stream.write(data)
            data = wf.readframes(chunk)

        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Display a message to indicate that audio recording is complete
        messagebox.showinfo("Record Audio", "Audio recording complete!")

        # Display the recorded audio file in the GUI
        audio = Image.open(audio_file)
        audio = audio.resize((300, 100))
        photo = ImageTk.PhotoImage(audio)
        self.audio_placeholder.configure(image=photo)
        self.audio_placeholder.image = photo
        pass

# Create an instance of the GUI
attendance_system_gui = AttendanceSystemGUI()
