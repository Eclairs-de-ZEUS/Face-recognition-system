import speech_recognition as sr
import datetime
import playsound
from gtts import gTTS
import os
from voice_handler.speech_to_file import *

def talk(output: str) -> None:
    """Talk to a person"""
    num = 0
    print(output)
    num += 1
    response = gTTS(text=output, lang='fr')
    _file = str(num) + ".mp3"
    response.save(_file)
    playsound.playsound(_file, True)
    os.remove(_file)

def welcome(name: str) -> None:
    """Handle salutation"""
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        talk(f"Bonjour {name}")
    elif hour >= 12 and hour <= 24:
        talk(f"Bonsoir {name}")

def takeCommand() -> str:
    """Record user command during 5 seconds"""
    speech_to_file("file.wav", 5)
    r = sr.Recognizer()
    with sr.AudioFile("file.wav") as source:
        audio_text = r.listen(source)
        data = ""
        try:
            data = r.recognize_google(audio_text, language="fr-FR")
            print(f"Ta question est {data}")
        except sr.UnknownValueError:
            talk("Désolé. Je ne t'avais pas entendu. Peux-tu répéter ?")
    os.remove("file.wav")
    return data

def voice_assistant(name: str, horos: str):
    """Main function"""
    stopwords = ["au revoir", "bye"]
    good_words = ["bien", "ça va"]
    bad_words = ["mal", "pas bien", "ça va mal", "très mal"]

    welcome(name)
    talk("Comment vas-tu ?")
    data = takeCommand()

    for word in bad_words:
        if word in data:
            talk("Ça ira mieux.")

    for word in good_words:
        if word in data:
            talk("Cool")
    
    talk("Que puis-je pour toi ?")
    ndata = takeCommand()

    if "horoscope" in ndata:
        talk(name + ', ' + 'ton horoscope dit que ' + horos)
    
    talk("Bonne journée")
