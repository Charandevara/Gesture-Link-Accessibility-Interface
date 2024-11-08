import pyttsx3
import speech_recognition as sr
import controller as cnt

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening****")
        audio=r.listen(source)
        try:
            print("Recognize****")
            query=r.recognize_google(audio, language='en-in')
        except Exception as e:
            print("Try Again****")
            return "None"
        return query

if __name__=="__main__":
    while True:
        query=takeCommand().lower()
        if 'light on' in query:
            print("Light On.........")
            speak("Light On....")
            cnt.led(1)
        elif 'light off' in query:
            print("Light Off.........")
            speak("Light Off.........")
            cnt.led(2)
        elif 'fan on' in query:
            print("Fan On.........")
            speak("Fan On....")
            cnt.led(3)
        elif 'fan off' in query:
            print("Fan Off.........")
            speak("Fan Off....")
            cnt.led(4)
        elif 'music on' in query:
            print("Music On.........")
            speak("Music On....")
            cnt.led(5)
        elif 'music off' in query:
            print("Music Off.........")
            speak("Music Off....")
            cnt.led(6)
        elif 'ac on' in query:
            print("AC On.........")
            speak("AC On....")
            cnt.led(7)
        elif 'ac off' in query:
            print("AC Off.........")
            speak("AC Off....")
            cnt.led(8)
        elif 'tv on' in query:
            print("TV On.........")
            speak("TV On....")
            cnt.led(9)
        elif 'tv off' in query:
            print("TV Off.........")
            speak("TV Off....")
            cnt.led(10)
        elif 'power off' in query:
            print("Everything off.........")
            speak("Everything  Off....")
            cnt.led(11)
        elif 'exit' in query:
            break