import cv2
import mediapipe as mp
import time
import controller2 as cnt
import threading
import pyttsx3
import speech_recognition as sr

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening****")
        audio = r.listen(source)
        try:
            print("Recognize****")
            query = r.recognize_google(audio, language='en-in')
        except Exception as e:
            print("Try Again****")
            return "None"
        return query

def recognize_speech():
    while True:
        query = takeCommand().lower()
        if 'light on' in query:
            print("Light On.........")
            speak("Light On....")
            cnt.led(6)
        elif 'light off' in query:
            print("Light Off.........")
            speak("Light Off.........")
            cnt.led(7)
        elif 'fan on' in query:
            print("Fan On.........")
            speak("Fan On....")
            cnt.led(8)
        elif 'fan off' in query:
            print("Fan Off.........")
            speak("Fan Off....")
            cnt.led(9)
        elif 'music on' in query:
            print("Music On.........")
            speak("Music On....")
            cnt.led(10)
        elif 'music off' in query:
            print("Music Off.........")
            speak("Music Off....")
            cnt.led(11)
        elif 'ac on' in query:
            print("AC On.........")
            speak("AC On....")
            cnt.led(12)
        elif 'ac off' in query:
            print("AC Off.........")
            speak("AC Off....")
            cnt.led(13)
        elif 'tv on' in query:
            print("TV On.........")
            speak("TV On....")
            cnt.led(14)
        elif 'tv off' in query:
            print("TV Off.........")
            speak("TV Off....")
            cnt.led(15)
        elif 'power off' in query:
            print("Everything off.........")
            speak("Everything  Off....")
            cnt.led(16)
        elif 'exit' in query:
            break

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

time.sleep(0)

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tipIds = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
    voice_thread = threading.Thread(target=recognize_speech)
    voice_thread.start()

    while True:
        ret,image=video.read()
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable=False
        results=hands.process(image)
        image.flags.writeable=True
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lmList=[]
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands=results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h,w,c=image.shape
                    cx,cy= int(lm.x*w), int(lm.y*h)
                    lmList.append([id,cx,cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
        fingers=[]
        if len(lmList)!=0:
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            total=fingers.count(1)
            cnt.led(total)

            if total == 0:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "0", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
                cv2.putText(image, "OFF", (100, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
            elif total==1:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "1", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "LIGHT", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            elif total==2:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "2", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "FAN", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            elif total==3:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "3", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "MUSIC", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            elif total==4:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "4", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "AC", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            elif total==5:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "5", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "TV", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

voice_thread.join()
video.release()
cv2.destroyAllWindows()
