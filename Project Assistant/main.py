import speech_recognition as sr
import os
import webbrowser
import google.generativeai as genai
from config import apikey,generation_config,safety_settings
import datetime
import random
import win32com.client
import pyautogui
import pywhatkit as pwt
import wikipedia

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Assistant"

if __name__ == '__main__':
    print('Welcome to Your Virtual Assistant')
    say("Hello Am your Virtual Assistant")
    while True:
        print("Listening...")
        query = takeCommand()
        
        if "open" in query.lower():
            query = query.replace("assistant","")
            query = query.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.press("enter")
            pyautogui.sleep(1)
            pyautogui.press("enter")

        elif "time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")   
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} hours {min} minutes")

        elif "google" in query.lower():
            import wikipedia as googleScrap
            query = query.replace("assistant","")
            query = query.replace("search","")
            query = query.replace("google","")
            say("This is what I found on google")
            pwt.search(query)
            result = googleScrap.summary(query,1)

        elif "YouTube" in query:
            say("This is what I found for your search!") 
            query = query.replace("youtube search","")
            query = query.replace("youtube","")
            query = query.replace("assistant","")
            web  = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            pwt.playonyt(query)
            say("Done, Sir")

        elif "wikipedia" in query.lower():
            say("Searching from wikipedia....")
            query = query.replace("wikipedia","")
            query = query.replace("search wikipedia","")
            query = query.replace("assistant","")
            results = wikipedia.summary(query,sentences = 5)
            say("According to wikipedia..")
            print(results)
            say(results)

        elif "artificial intelligence" in query.lower():
            def ai(prompt):
                genai.configure(api_key=apikey)
                model = genai.GenerativeModel(model_name="gemini-1.0-pro",generation_config=generation_config,safety_settings=safety_settings)
                text = f"Gemini response for Prompt: {prompt} \n *************************\n\n"
                response = model.generate_content(prompt)
                text += response.text
                if not os.path.exists("GEMINI_project"):
                    os.mkdir("GEMINI_project")

                with open(f"GEMINI_project/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
                    f.write(text) 
            ai(query)
            break

        elif "hello assistant" in query:
            def chat(prompt):
                genai.configure(api_key=apikey)
                model = genai.GenerativeModel(model_name="gemini-1.0-pro",generation_config=generation_config,safety_settings=safety_settings)
                convo = model.start_chat(history=[])
                convo.send_message(prompt)
                print(convo.last.text)
                say(convo.last.text)
            while True:
                if "sleep" in query:
                    exit()
                chat(query)
                print("listening...")
                query = takeCommand()   

        elif "chat" in query:
            def chat(prompt):
                genai.configure(api_key=apikey)
                model = genai.GenerativeModel(model_name="gemini-1.0-pro",generation_config=generation_config,safety_settings=safety_settings)
                convo = model.start_chat(history=[])
                convo.send_message(prompt)
                print(convo.last.text)
                say(convo.last.text)
            while True:
                if "sleep" in query:
                    exit()
                chat(query)
                print("listening...")
                query = takeCommand() 

        elif "sleep" in query.lower():
            say("exiting the program")
            exit()


        