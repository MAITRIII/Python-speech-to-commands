import webbrowser as wb
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from googlesearch import search
import subprocess as sp


def facebook(name):
    speak("hold on "+name+", i will redirect you to facebook")
    wb.open("www.facebook.com")
def gmail(name):
    speak("just a minute"+name+"bring you to gmail")
    wb.open("www.gmail.com")
def locations(data,name):
    data = data.split(" ")
    location = data[2]
    speak("Hold on"+name+",I will search for "+location)
    wb.open("https://www.google.nl/maps/place/" + location + "/&amp")
def search(data,name):
    speak("wait for a while "+name+" ,I will search for you.")
    wb.open("https://www.google.co.in/?gfe_rd=cr&ei=V7DXWJuQNarT8gfb-42QBw&gws_rd=ssl#newwindow=1&safe=active&q="+data+"&*")
def notepad(name):
    speak("Opening notepad for you")
    pname = "notepad.exe"
    filename = "filename.txt"
    sp.Popen([pname, filename])
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("audio.mp3")
def closee(name):
    speak("closing"+name)
    #sp.Popen("cmd.exe")
    #os.chdir("C:\\Users\\maitr\\Desktop\\my")
    #os.startfile("close.bat")
    #imp.load_source("C:\\Users\\maitr\\Desktop\\my\\close")
    #pname = "C:\\Users\\maitr\\Desktop\\my\\close"
    #sp.Popen([pname])
    filepath="C:/Users/maitr/Desktop/my/close.bat"
    os.system(filepath)
def calc(name):
    filepath="C:/Users/maitr/Desktop/my/openc.bat"
    #p = sp.Popen(filepath, shell=True, stdout = sp.PIPE)
    #stdout, stderr = p.communicate()
    #print(p.returncode)
    os.system(filepath)
def recordAudio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said:"+data)
    except sr.UnknownValueError:
        print("Google can not understand you")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

        
    return data
def PA(data,name):
    if "close" in data:
        closee(name)
    if "what is your name" in data:
        speak("i am Ciara.")
    if "notepad" in data:
        notepad(name)
    if "how are you" in data:
        speak("i am fine and you?")
    if "what time is it" in data:
        speak(ctime())
    if "where is" in data:
        locations(data,name)
    if "I would like to use Facebook" in data:
        facebook(name)
    if "I would like to hear some music" in data:
        youtube(name)
    if "check my mail" in data:
        gmail(name)
    if "search for" in data:
        search(data,name)
    if "open calculator" in data:
        calc(name)
    if "goodbye" in data:
        speak("goodbye mann")
        exit()
speak("what is your name:")
name=input()
speak("HI "+name+"!!!What can i do for you?")
while 1:
    print("SPEAK:")
    data = ''+recordAudio()
    print("PROCESSING...")
    PA(data,name)
                
