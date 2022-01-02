import speech_recognition as sr

if __name__ == '__main__':
    word = "audio"
    dur = 2
    print("You need to say: " + word)

    init_rec = sr.Recognizer()
    print("Listening...")
    with sr.Microphone() as source:
        audio_data = init_rec.record(source, duration=dur)
        print("Recognizing your text.............\n")
        text = init_rec.recognize_google(audio_data)
        print("You said : " + text + "\n")

    # if text include word
    if word in text:
        print("your pronunciation is correct")
    else:
        print("Your pronunciation is wrong")
        print("Please try again")

# Try Later
# https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
