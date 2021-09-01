import pyttsx3
import speech_recognition as sr
import datetime
import os
from requests import get
import  wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import  sys
import pyautogui
import time
import keyboard
import wolframalpha
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from anikaUi import Ui_anikaGui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning ")
        

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Anika Mam. Please tell me how may I help you")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your password')
    server.sendmail('your email id',to,content)
    server.close()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            #audio = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        query = query.lower()
        return query

    
    def TaskExecution(self):

        wishMe()

        while True:
            self.query = self.takeCommand().lower()

            if "open notepad" in self.query:
                speak("Launching notepad...")
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif "introduce yourself" in self.query:
                speak("Ok mam")
                speak("Hello all, Myself Anika I am a virtual assistant created by Simran and her team. My work is to assist simran in her work like to launch any application or website and to send emails and whatsapp message and many more things")

            elif "open command prompt" in self.query:
                speak("Opening command prompt")
                os.system("start cmd")

            elif "wikipedia" in self.query:
                speak("Searching wikipedia...")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query, sentences=1)
                speak("According to wikipedia")
                speak(results)

            #youtube automation

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")
                
            elif "youtube search" in self.query:
                speak("Ok Mam, This is what I found for your search!")
                self.query = self.query.replace("helena","")
                self.query = self.query.replace("youtube search","")
                web = 'https://www.youtube.com/results?search_query=' + self.query
                webbrowser.open(web)
                speak("Done Mam")

            elif 'pause' in self.query:
                keyboard.press('space bar') 

            elif 'restart' in self.query:
                keyboard.press('0')

            elif 'mute' in self.query:
                keyboard.press('m')

            elif 'forward' in self.query:
                keyboard.press('l')

            elif 'backward' in self.query:
                keyboard.press('j')

            elif "play song on youtube" in self.query:
                speak("Which song would you like to listen..")
                songName = self.takeCommand()
                kit.playonyt(songName)

            elif "video downloader" in self.query:
                root = Tk()
                root.geometry('500x300')
                root.resizable(0,0)
                root.title("Youtube Video Downloader")
                speak("Enter the video link")

                Label(root,text="Youtube Video Downloader",font='arial 15 bold').pack()
                link = StringVar()
                Label(root, text='Paste YT Video URL here',font='arial 15 bold').place(x=160,y=60)
                Entry(root,width=70,textvariable =link).place(x=32,y=90)

                def VideoDownloader():
                    url = YouTube(str(link.get()))
                    video = url.streams.first()
                    video.download()
                    Label(root,text="Downloaded",font = 'arial 15').place(x=180,y=210)

                Button(root,text="Download",font='arial 15 bold',bg='pale violet red',padx=2,command= VideoDownloader).place(x=180,y=150)

                root.mainloop()
                speak("Video Downloaded")
            
            #chrome automation

            elif "google search" in self.query:
                speak("Ok Mam, This is what I found for your search!")
                self.query = self.query.replace("anika","")
                self.query = self.query.replace("google search","")
                kit.search(self.query)
                speak("Done Mam")

            elif "open google" in self.query:
                speak("Mam, what should I search on google")
                cm = self.takeCommand()
                webbrowser.open(f"{cm}")

            elif "open new tab" in self.query:
                speak("Opening new tab")
                keyboard.press_and_release('ctrl + t')

            elif "close this tab" in self.query:
                speak("Closing current tab")
                keyboard.press_and_release('ctrl + w')

            elif "open new window" in self.query:
                speak("Launching new window")
                keyboard.press_and_release('ctrl + n')

            elif "history" in self.query:
                speak("Checking the history")
                keyboard.press_and_release('ctrl + h')

            elif "add a bookmark" in self.query:
                speak("Ok Mam, adding a new bookmark")
                keyboard.press_and_release('ctrl + d')

            elif "open bookmark manager" in self.query:
                speak("Launching bookmark manager")
                keyboard.press_and_release('ctrl + shift + o')

            elif "website" in self.query:
                speak("Ok Mam, Launching...")
                self.query = self.query.replace("anika","")
                self.query = self.query.replace("website","")
                self.query = self.query.replace(" ","")
                web1 = self.query.replace("open","")
                web2 = 'https://www.'+ web1 + '.com'
                webbrowser.open(web2)
                speak("Launched!")


            elif "switch the windows" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "what is the time" in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Mam the time is {strTime}")

            #Email automation

            elif "email to simran" in self.query:
                try:
                    speak("What should i send?")
                    content = self.takeCommand()
                    to = "your email id"
                    sendEmail(to,content)
                    speak("Email has been send sucessfully")

                except Exception as e:
                    print(e)
                    speak("sorry mam, not able to send mail")

            
            elif "send a mail" in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand().lower()
                    speak("Whom should I send?")
                    to = input()
                    sendEmail(to, content)
                    speak("Email has been send sucessfully")

                except Exception as e:
                    print(e)
                    speak("sorry mam, not able to send mail")

            #whatsapp automation

            

            elif 'send message to shivani' in self.query:
                speak("Tell me the message that you want to send")
                msg = self.takeCommand()
                speak("set the time to deliver message!")
                kit.sendwhatmsg("+91**********",f"{msg}",int(input()),int(input()) )
                speak("Message sent successfully!!")

            elif 'send message to pooja' in self.query:
                speak("Tell me the message that you want to send")
                msg = self.takeCommand()
                speak("set the time to deliver message!")
                kit.sendwhatmsg("+91**********",f"{msg}",int(input()),int(input()) )
                speak("Message sent successfully!!")

            elif 'answer me' in self.query:
                speak('what question do you want to ask?')
                question=self.takeCommand()
                client = wolframalpha.Client("***********")
                res = client.query(question)
                speak(next(res.results).text)
                print(next(res.results).text)
    

            elif "exit" in self.query:
                speak("thanks for using me mam, have a good day.")
                sys.exit()

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_anikaGui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../helena/bg.jpg")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../helena/screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../helena/robo.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../helena/Anika.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../helena/google.jpg")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../helena/mail.jpg")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../helena/mus.jpg")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../helena/whp.jpg")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../helena/web.jpg")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../helena/yout.jpg")
        self.ui.label_10.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../helena/mic.gif")
        self.ui.label_11.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../helena/frame1.jpg")
        self.ui.label_12.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../helena/frame1.jpg")
        self.ui.label_13.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)

app = QApplication(sys.argv)
anika = Main()
anika.show()
exit(app.exec_())



