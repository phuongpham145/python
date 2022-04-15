import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice', voice[1].id)
def speak(audio):
    print("P.H.A.M\n" + audio)
    friday.say(audio)
    friday.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I: %M: %p")
    speak(Time)
def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Night Sir")
    speak("How can I help you?")
def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='en')
        print("Phuong Pham : " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query = str(input("Your order is: "))
    return query
if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("What shoud I search boss?")
            search = command().lower()
            url= f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Hrer is your {search} on Google")
