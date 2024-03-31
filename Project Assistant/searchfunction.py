import wikipedia
import speech_recognition as sr
import win32com.client
import webbrowser
import pywhatkit as pwt

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
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
        
query = takeCommand().lower
        
def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("assistant","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")
        pwt.search(query)
        result = googleScrap.summary(query,1)
        

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("assistant","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pwt.playonyt(query)
        speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("assistant","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)