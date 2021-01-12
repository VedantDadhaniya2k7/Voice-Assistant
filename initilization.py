"""
First of all you need to import the following modules with pip:
    - playsound
    - SpeechRecognition
    - gTTS
    - pyaudio
"""


import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import subprocess

"""
Defining the function to make the AI speak
"""
aud_num = 0
def speak(text):
    global aud_num
    aud_num += 1
    tts = gTTS(text=text, lang="en")
    filename = "voice"+str(aud_num)+".mp3"
    tts.save(filename)

    playsound.playsound(filename)

"""
Defining the function to get audio from the user
"""
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now")
        audio = r.listen(source)
        said = ""
        
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exeption: " + str(e))
    return said

"""
Defining the function to open apps when an user input is provided
"""
def Open_App(user_input):
    """
    the user input has to be provided after decoding the user's speech, i.e. to
    provide text like - "google" or "excel" or etc
    """
    note_count = 0
    if user_input == "Google":
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
        return
    if user_input == "Notepad":
        file_name = "Note_" + str(note_count) + ".txt"
        with open(file_name, "w") as f:
            speak("What do you want to write down?")
            input_ = get_audio()
            f.write(input_)
        subprocess.Popen(["notepad.exe", file_name])
    if user_input == "Word":
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk') 
        return
    if user_input == "Excel":
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk') 
        return
    
GOOGLE_KEYWORDS = [
    "open google",
    "start google",
    "open google chrome",
    "start google chrome",
    "open chrome",
    "start chrome",
    "google",
    "google chrome",
    "chrome"
    ]

NOTEPAD_KEYWORDS = [
    "write this down",
    "take a note",
    "open notepad",
    "open notes",
    "start notepad",
    "start notes",
    "notes"
    ]

WORD_FILE_KEYWORDS = [
    "open word",
    "open word file",
    "open word file editor",
    "start word",
    "start word file",
    "start word file editor",
    "word file",
    "word file editor"
    ]

EXCEL_KEYWORDS = [
    "open excel",
    "open excel file",
    "open excel file editor",
    "start excel",
    "start excel file",
    "start excel file editor",
    "excel file",
    "excel file editor"
    ]


def main():
    run  = True
    while run:
        User_input = get_audio()
        for word in EXCEL_KEYWORDS :
            if word in str(User_input).lower():
                Open_App("Excel")
        for word in WORD_FILE_KEYWORDS :
            if word in str(User_input).lower():
                Open_App("Word")
        for word in NOTEPAD_KEYWORDS :
            if word in str(User_input).lower():
                Open_App("Notepad")
        for word in GOOGLE_KEYWORDS :
            if word in str(User_input).lower():
                Open_App("Google")

        if "close" in str(User_input).lower() or "stop" in str(User_input).lower():
            run = False

