import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voices = listener.listen(source)
            command = listener.recognize_google(voices)
            command = command.lower()
            if 'siyam' in command:
                command = command.replace('alexa', '')
                print(command)




    except:
        pass
    return command


def run_sammy():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Okay playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Ekhon Shomoy' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        jokes = pyjokes.get_jokes()
        talk(jokes)
    elif 'hello' in command:
        talk('I am Siyam. What can I do for you?')
    elif 'single' in command:
        talk('yes, i am single forever')
    elif 'date' in command:
        talk('Sorry, I can not go for date with you. because tui ekta pooola')
    else:
        talk('I can not understand. Please say again')



while True:
    run_sammy()


