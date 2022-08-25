import webbrowser, sys, pyperclip
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import speech_recognition as sr
import pyttsx3

load_dotenv()
passwordMLB = os.getenv('MLB_PASS')
userNameMLB = os.getenv('MLB_USER')
passwordFD = os.getenv('FD_PASS')
userNameFD = os.getenv('FD_USER')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)





def launchBrowser():
    global userNameMLB, passwordMLB, userNameFD, passwordFD
    
    browser = webdriver.Chrome(ChromeDriverManager().install())
    
    browser.get('https://www.fanduel.com/')

    browser.execute_script("window.open('about:blank', 'tab2');")
    browser.switch_to.window("tab2")

    browser.get('https://www.mlb.com/login')
    
    userElem = browser.find_element('id', 'okta-signin-username')
    userElem.send_keys(userNameMLB)

    passwordElem = browser.find_element('id', 'okta-signin-password')
    passwordElem.send_keys(passwordMLB)
    passwordElem.submit()

    browser.execute_script("window.open('about:blank', 'tab3');")
    browser.switch_to.window("tab3")

    browser.get('https://windailysports.com/daily-fantasy-baseball-articles/')

    browser.execute_script("window.open('about:blank', 'tab4');")
    browser.switch_to.window("tab4")

    browser.get("https://www.rotowire.com/daily/mlb/")
    
    while True:
        pass

    return browser

def launchWeather():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What is your zip code?")
        print("What is your zip code?")
        audio = r.listen(source)

        try:
            zipCode = r.recognize_google(audio)
            print(f"Zip Code: {zipCode}")
            browser = webdriver.Chrome(ChromeDriverManager().install())
            browser.get('https://weather.com/weather/today/l/' + zipCode + ':4:US')
        except:
            speak("I don't recognize that zip code. Please try again")
            launchWeather()

    while True:
        pass

def launchNews():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What type of news would you like?")
        print("Options: \n World \n U.S \n Politics \n Business \n Tech \n Health \n Sports")
        audio = r.listen(source)

        try:
            topic = r.recognize_google(audio)
            print(f"Topic: {topic}")
            browser = webdriver.Chrome(ChromeDriverManager().install())
            browser.get('https://www.nytimes.com/section/' + topic)
        except:
            speak("I don't recognize that topic. Please try again")
            launchNews()

        while True:
            pass

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Hello. I'm Jarvis, your virtual assistant. What can I help you with?")
        print("Jarvis Active")
        audio = r.listen(source)
        
        try:
            query = r.recognize_google(audio)
            print(f"user: {query}")
            if 'baseball' in query:
                launchBrowser()
            if 'joke' in query:
                speak('Am I a clown? Do I amuse you?')
            if 'weather' in query:
                launchWeather()
            if 'news' in query:
                launchNews()
            else:
                 speak("I'm sorry, I don't recognize that command. Please try again.")
                 command()       
            return query
        except:
            print("Try Again.")

    


command()











