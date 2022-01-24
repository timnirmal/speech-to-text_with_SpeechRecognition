import speech_recognition as sr
dir(sr)

if __name__ == '__main__':
    word = "audio"
    dur = 2
    print("You need to say: " + word)

    init_rec = sr.Recognizer()
    print("Listening...")
    with sr.Microphone() as source:
        audio_data = init_rec.record(source, duration=dur)
        # save audio data to file
        with open("audio.wav", "wb") as f:
            # TypeError: a bytes-like object is required, not 'AudioData'
            f.write(audio_data.get_wav_data())

        try:
            print("Recognizing your text.............\n")
            text = init_rec.recognize_google(audio_data, language='en-in')
            print("Text is : ", end=" ")
            print(text)

            # if text include word
            if word in text:
                print("your pronunciation is correct")
            else:
                print("Your pronunciation is wrong")
                print("Please try again")

        except Exception as e:
            print("Sorry, I didn't get that. Please try again.\n")
            print("Error: " + str(e))

# pip install SpeechRecognition
# pip install pipwin
# pipwin install pyaudio
