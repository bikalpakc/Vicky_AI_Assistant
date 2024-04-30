import speech_recognition as sr
import google.generativeai as genai
import pyaudio
import wave
import tempfile
import os
import webbrowser
import time
import datetime
import random
from win32com.client import Dispatch

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    genai.configure(api_key="<<YOUR_API_KEY>>")
    chatStr += f"User: {query}"


    # Set up the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])

    convo.send_message(query)
    say(convo.last.text)

def ai(prompt):
    genai.configure(api_key="AIzaSyCTFrA5MADwq1xVZcof8E1Rgp3KXUdH3uw")
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"


    # Set up the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])

    convo.send_message(prompt)
    print(convo.last.text)
    text += convo.last.text
    if not os.path.exists("Gemini"):
        os.mkdir("Gemini")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Gemini/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)




def say(text):

    speak = Dispatch("SAPI.SpVoice").Speak
    speak({text})

def takeCommand():

    def record_audio(seconds=5):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = seconds

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* Recording audio...")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* Finished recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        audio = b''.join(frames)
        print("* Audio recorded")

        return audio

    def save_audio_to_file(audio_data, filename):
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(audio_data)

    def recognize_speech(audio_file):
        recognizer = sr.Recognizer()

        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)  # Load audio file
            print("Recognizing...")
            try:
                text = recognizer.recognize_google(audio)
                print("Speech recognized:", text)
                return text
            
            except Exception as e:
                return "An Error Occured. I am Sorry. Please try again"
        

    if __name__ == "__main__":
        audio = record_audio()
        temp_audio_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        temp_audio_file.close()
        save_audio_to_file(audio, temp_audio_file.name)
        query = recognize_speech(temp_audio_file.name)
        return query
        os.unlink(temp_audio_file.name)  # Delete temporary audio file



say("Hey yo!, It's Vicky AI. developed by the greatest, lord Becalpa, How can I help you?")
# say("Sorry sir, I mispronounced your name. But Now I know it. It's Becalpa. See I told you")
while True:
    print("Listening..")
    query=takeCommand()
    sites=[["Youtube", "https://www.youtube.com"],["Netflix", "https://www.netflix.com"], ["Instagram", "https://www.instagram.com"], ["Facebook", "https://www.facebook.com"]]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            say(f"As you wish. Opening {site[0]} for you sir")
            webbrowser.open(f"{site[1]}")
            time.sleep(3)
            say("My response is really fast, ain't it?")

    if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir, time is {hour} {min}")  

    elif "open epic games".lower() in query.lower():
            epic_games_launcher_path="C:/Users/Public/Desktop/Epic Games Launcher.lnk"
            os.system(f"open {epic_games_launcher_path}") 

    elif "using Artificial Intelligence".lower() in query.lower(): 
        ai(prompt=query)       

    elif "Vicky Quit".lower() in query.lower():
            exit()

    elif "reset chat".lower() in query.lower():
            chatStr = ""                 
  
    else:
            print("Chatting...")
            chat(query)        

    # say(query)
    # os.unlink(takeCommand.temp_audio_file.name)  # Delete temporary audio file






# if __name__=="__main__":
#     print('VS Code')
#     # say("Hey yo!, It's Vicky A.I")
#     say()
