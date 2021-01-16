import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init() #initializing the library
voices = engine.getProperty('voices')  #getting all the available voice versions for our assistant
#engine.setProperty("voice",voices[1].id) #this is the index of female voice

def talk(text):
    engine.say(text)
    engine.runAndWait()

def input_command():
    #engine.say("hello there! what can i do for you?")  #say function is built in our system speaks back the sentence.
    #engine.runAndWait()
    try:
        with sr.Microphone as source:
            print("Listening")
            voice = Listener.listen(source)
            my_command = listener.recognize_google(voice)
            my_command = my_command.lower()
            if 'assname' in my_command:
                talk(my_command)
    except:
        my_command = "exception" #this is written because if microphone failes it prints this command.
        print("microphone not working properly")
    return my_command

def start_assname():
    command = input_command()
    command = command.replace("hey assname","")
    if 'time' in command:
        current_time = datetime.datetime.now().strftime('%H%M')
        talk(current_time)

start_assname()  #main function call