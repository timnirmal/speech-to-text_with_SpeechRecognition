import speech_recognition as sr
import pyttsx3

dur = 2
speakingError = True
word = "audio"

# audio of system to respond
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# simple function to recognise speech from user
def takecommand():
    # it takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        audio = r.record(source, duration=dur)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print('User Said : ', query)

    except Exception as e:
        print('exception : ', e)
        return "None"
    return query


while True:
    query = takecommand()  # whatever user says will be stored in this variable
    print("The Test got in program is : " + query)

    # Prounce check
    if query in word:
        print("Pronounce is correct")
        if speakingError:
            speak("Pronounce is correct")
    elif query == "None":
        print("Sorry, I didn't hear that, Say that again Please")
        if speakingError:
            speak("Sorry, I didn't hear that, Say that again Please")
    else:
        print("Pronounce is wrong")
        if speakingError:
            speak("Pronounce is wrong")
