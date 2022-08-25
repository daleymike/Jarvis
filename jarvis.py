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
engine.setProperty('rate', 200)
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
        print("Options: \n World \n U.S \n Politics \n Business \n Technology \n Health \n Sports")
        audio = r.listen(source)

        try:
            topic = r.recognize_google(audio)
            print(f"Topic: {topic}")
            browser = webdriver.Chrome(ChromeDriverManager().install())
            browser.get('https://www.nytimes.com/section/' + topic.lower())
        except:
            speak("I don't recognize that topic. Please try again")
            launchNews()

        while True:
            pass

def launchLookUp():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What would you like to Google?")
        audio = r.listen(source)

        try:
            search = r.recognize_google(audio)
            print(f"Search: {search}")
            search.split(" ")
            newSearch = ''
            for i in search:
                print(i)
                newSearch += i + '+'
            
            browser = webdriver.Chrome(ChromeDriverManager().install())
            browser.get('https://www.google.com/search?q=' + newSearch + '&sxsrf=ALiCzsZLrK1k2hfmLz1Rq1x0fvQ2j5KjTQ%3A1661443550228&ei=3p0HY5OnDYSy5NoPn4alqAE&ved=0ahUKEwiTjoDFr-L5AhUEGVkFHR9DCRUQ4dUDCA4&uact=5&oq=banana+is+cool+da&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCgATIFCCEQoAEyCAghEB4QFhAdMggIIRAeEBYQHTIICCEQHhAWEB0yCAghEB4QFhAdMggIIRAeEBYQHTIICCEQHhAWEB0yCAghEB4QFhAdOgcIABBHELADOggIABAeEBYQCjoGCAAQHhAWOgUIIRCrAjoKCCEQHhAPEBYQHUoECEEYAEoECEYYAFC5B1jcCWCHEGgBcAF4AIABYYgB8AGSAQEzmAEAoAEByAEIwAEB&sclient=gws-wiz')
        except:
            speak("I don't recognize that search. Please try again")
            launchLookUp()

        while True:
            pass

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Hello. I'm Jarvis, your virtual assistant. What can I help you with?")
        print("Jarvis Active. Available commands: \n Baseball \n Joke \n Weather \n News")
        audio = r.listen(source)
        
        try:
            query = r.recognize_google(audio)
            print(f"user: {query}")
            if 'baseball' in query:
                launchBrowser()
            elif 'joke' in query:
                speak('Am I a clown? Do I amuse you?')
            elif 'weather' in query:
                launchWeather()
            elif 'news' in query:
                launchNews()
            elif 'google' in query or 'Google' in query or 'look up' in query:
                launchLookUp()
            else:
                 speak("I'm sorry, I don't recognize that command. Please try again.")
                 command()       
            return query
        except:
            print("Try Again.")

    


command()











