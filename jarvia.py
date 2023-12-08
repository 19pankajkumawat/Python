# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# # print(voice[1].id)
# print(voices[1].id)

# engine.setProperty('voie',voices[0].id)
# def speak(audio):
#  engine.say(audio)
#  engine.runAndWait()

# if __name__== "__main__":
#     speak("morning")

# print("hello");


# import speech_recognition as sr
# def speak (text):
#     tts = gTTS(text=text, lang='en')
#     tts.save("output.mp3")


import pyttsx
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

    speak("test the app")
