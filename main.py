import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init() #initializing the library
voices = engine.getProperty('voices')  #getting all the available voice versions for our assistant
#engine.setProperty("voice",voices[1].id) #this is the index of female voice

