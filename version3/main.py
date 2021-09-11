import speech_recognition as sr 


r = sr.Recognizer()
r.energy_threshold = 1568 
r.dynamic_energy_threshold = True
# record Audio *************************
def record_audio():
    with sr.Microphone(sample_rate=44100) as source:
        # print("say something")
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print("Sorry, i did not get that ")
        except sr.RequestError:
            print("Sorry, my speech service is down ")

        return voice_data
print("How can i help you")
voice_data = record_audio()
print(voice_data)

