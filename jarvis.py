# https://www.youtube.com/watch?v=8WKjX0dbh4E&t=380s&ab_channel=AVM

# pip install SpeechRecognition
# pip install pyttsx3
# pip install PyAudio

import speech_recognition as sr
import pyttsx3
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 130)

name = 'jarvis'

# engine.say('hola joaquin, como estas')
# engine.runAndWait()

def talk(text):    
    engine.say(text)
    engine.runAndWait()


# for voice in voices:
#     print(voice)

def listen():
    try:
        with sr.Microphone() as source:
            print('escuchando..')
            voice = listener.listen(source)
            # rec = listener.recognize_google(voice)
            rec = listener.recognize_google(voice, language="es-ES")
            print(rec)
            rec = rec.lower()
            if name in rec:
                # talk(rec)
                return rec
            else:
                return ''

    except:
        pass 
    # return rec

def run():
    rec = listen()
    if 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        print('son las ' + hora)
        talk('son las ' + hora)
        
    else:
        talk('intente de nuevo.')
while True:
    run()