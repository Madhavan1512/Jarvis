from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import re
import pyaudio
import random
import time
import webbrowser
import datetime
import wikipedia

import wolframalpha
from Jarvis import JarvisAssistant

obj = JarvisAssistant()
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wish():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Hello My name is Jarvis , now i am online")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good night")
    c_time = obj.tell_time()
    c_date = obj.tell_me_date()
    speak(f"Currently it is {c_time}")
    speak(f'today is {c_date}')
    speak("I am good and ready to go sir . Please tell me , how may I help you")





class mainT(QThread):
    def __init__(self):
        super(mainT, self).__init__()
    
    def run(self):
        wish()
        self.JARVIS()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...........")
            audio = R.listen(source)
        try:
            print("Recognising......")
            text = R.recognize_google(audio, language='en-in')
            print(">> ", text)
        except Exception:
            speak("Sorry Speak Again")
            print("Sorry Speak Again")
            return "none"
        text = text.lower()
        return text

    def JARVIS(self):

        while True:
            self.query = self.STT()
            if "wikipedia" in self.query:
                speak("searching details....Wait")
                self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                print(results)
                speak(results)
            elif 'date' in self.query or 'what\'s today\'s date' in self.query or 'what date' in self.query or 'today\'s date' in self.query :
                date = obj.tell_me_date()
                print(date)
                speak(date)
            elif "time" in self.query or 'what\'s the time' in self.query or 'what is time' in self.query or 'what the time' in self.query or 'now ' in self.query or 'now time' in self.query:
                time_c = obj.tell_time()
                print(time_c)
                speak(f"Sir the time is {time_c}")
            elif 'open youtube' in self.query or "open video online" in self.query:
                webbrowser.open("www.youtube.com")
                speak("opening youtube")

            elif 'open github' in self.query:
                webbrowser.open("https://www.github.com")
                speak("opening github")

            elif 'open facebook' in self.query:
                webbrowser.open("https://www.facebook.com")
                speak("opening facebook")

            elif 'open instagram' in self.query:
                webbrowser.open("https://www.instagram.com")
                speak("opening instagram")

            elif 'open google' in self.query:
                webbrowser.open("https://www.google.com")
                speak("opening google")

            elif 'open yahoo' in self.query:
                webbrowser.open("https://www.yahoo.com")
                speak("opening yahoo")

            elif 'open gmail' in self.query:
                webbrowser.open("https://mail.google.com")
                speak("opening google mail")

            elif 'open snapdeal' in self.query:
                webbrowser.open("https://www.snapdeal.com")
                speak("opening snapdeal")

            elif 'open amazon' in self.query or 'shop online' in self.query:
                webbrowser.open("https://www.amazon.com")
                speak("opening amazon")

            elif 'open flipkart' in self.query:
                webbrowser.open("https://www.flipkart.com")
                speak("opening flipkart")

            elif 'open ebay' in self.query:
                webbrowser.open("https://www.ebay.com")
                speak("opening ebay")

            elif 'what is the weather' in self.query:
                webbrowser.open("https://www.google.com/search?q=weather")
                speak("checking weather")

            elif 'music from pc' in self.query or "music" in self.query or 'song' in self.query:
                speak("Here is the music that you requested")
                music_dir = './music'
                musics = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, musics[0]))
                print("Here is the music that you requested")

            elif 'video from pc' in self.query or "video" in self.query:
                speak("Here is the video that you requested")
                video_dir = './video'
                videos = os.listdir(video_dir)
                os.startfile(os.path.join(video_dir, videos[0]))
                print("Here is the video that you requested")
            elif 'good bye' in self.query or "That will be all JARVIS" in self.query:
                speak("good bye sir , have a nice day")
                exit()

            elif "shutdown" in self.query:
                speak("shutting down")
                os.system('shutdown -s')

            elif "what\'s up" in self.query or 'how are you' in self.query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy',
                          'i am okay ! How are you']
                ans_q = random.choice(stMsgs)
                speak(ans_q)
                print("How are you , sir?")
                speak("How are you , sir?")
                ans_take_from_user_how_are_you = self.JARVIS()
                if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okay' in ans_take_from_user_how_are_you or 'good' in ans_take_from_user_how_are_you:
                    speak('Very happy to hear that sir')
                    print('Very happy to hear that sir')
                elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you or 'bad' in ans_take_from_user_how_are_you:
                    speak('Very sad to hear that sir')
                    print('Very sad to hear that sir')
            elif 'make you' in self.query or 'created you' in self.query or 'develop you' in self.query:
                ans_m = " I was Created by Madhavan S and Nishanth . I hold them in very high regards "
                print(ans_m)
                speak(ans_m)

            elif "who are you" in self.query or "about you" in self.query or "your details" in self.query:
                about = "I am Jarvis an A I based computer program but i can help you a lot like your close friend ! I promise you ! Simply try  to give me a simple command ! like playing music or video from your directory I can also play video and song from web or online !  ok Lets Start "
                print(about)
                speak(about)

            elif "hello" in self.query or "hello Jarvis" in self.query:
                hel = "Hello  Sir ! How May i Help you.."
                print(hel)
                speak(hel)

            elif "your name" in self.query or "sweat name" in self.query:
                na_me = "My name is JARVIS , thank you very much for asking."
                print(na_me)
                speak(na_me)

            elif "you feeling" in self.query:
                print("feeling great after meeting you")
                speak("feeling great after meeting you")

            elif self.query == 'none':
                continue

            elif 'exit' in self.query or 'abort' in self.query or 'stop' in self.query or 'bye' in self.query or 'quit' in self.query or 'good night' in self.query or 'see you' in self.query:
                ex_exit = 'It was a pleasure meeting your sir ,  have a good day !!'
                print(ex_exit)
                speak(ex_exit)
                exit()

            elif 'old are you' in self.query or 'old you' in self.query or 'old are' in self.query or 'when were you born' in self.query:
                print("I was created on 13th January 2022")
                speak("I was created on 13th January 2022")

            else:
                temp = self.query.replace(' ', '+')
                g_url = "https://www.google.com/search?q="
                res_g = 'I got this result on the Internet'
                print(res_g)
                speak(res_g)
                webbrowser.open(g_url + temp)

FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1366,768)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit -Copy.png);\n"
        "border:free;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont(' Acens ', 8)))
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setXOffset(-1)
        self.shadow.setYOffset(-1)
        self.shadow.setBlurRadius(20)
        self.shadow.setColor(QColor(255, 255, 255))
        self.label_5.setGraphicsEffect(self.shadow)


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())