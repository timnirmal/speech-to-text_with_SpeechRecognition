import speech_recognition as sr
import pyttsx3

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
        #r.pause_threshold = 0.8
        #r.energy_threshold = 4000
        #audio = r.listen(source, timeout=2)
        audio = r.record(source, duration=2)
        # audio to file
        with open('audio.wav', 'wb') as f:
            f.write(audio.get_wav_data())



    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print('User Said : ', query)

    except Exception as e:
        print('exception : ', e)

        speak("Sorry, I didn't hear that, Say that again Please")
        return "None"
    return query


while True:
    query = takecommand()  # whatever user says will be stored in this variable
    print("The Test got in program is : " + query)
