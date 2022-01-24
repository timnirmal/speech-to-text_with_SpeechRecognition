import speech_recognition as sr
import pyttsx3

dur = 4
speakingError = True
phrase = "Audio word"

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

    except Exception as e:
        print('exception : ', e)
        return "None"
    return query


while True:
    print("\nYou need to say : ", phrase, end="\n\n")

    query = takecommand()  # whatever user says will be stored in this variable
    print("You said : " + query)

    if query == "None":
        print("Sorry, I didn't hear that, Say that again Please")
        if speakingError:
            speak("Sorry, I didn't hear that, Say that again Please")
    else:
        query = query.lower()
        phrase = phrase.lower()
        phraseList = phrase.split()
        queryList = query.split()
        wrongList = []
        rightList = []

        # find words not in phrase compare to queryList and print them
        for word in phraseList:
            if word not in queryList:
                wrongList.append(word)
            else:
                rightList.append(word)

        # print("phraseList : ", phraseList)
        # print("queryList : ", queryList)
        # print("wrongList : ", wrongList)
        # print("rightList : ", rightList)

        # if wrongList is empty
        if len(wrongList) == 0:
            print("Pronounce is correct")
            if speakingError:
                speak("Pronounce is correct")
        else:
            print("You pronounced ", wrongList, " wrong")
            if speakingError:
                speak("You pronounced " + str(wrongList) + " wrong")
