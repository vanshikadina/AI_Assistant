import pyttsx3 ##for the ai to speak, ## text to speech library
import datetime
import speech_recognition as sr ##for getting input voices   ## speech to text library
import wikipedia #for surfing wikipedia
import os ##for opening local files
import webbrowser ## for surfing the internet
import time
import pyautogui ## controls the mouse and kyboard just like a human

##Importing the voice for AI
engine = pyttsx3.init('sapi5') ##one of the engine present inside this library
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id) #Male voice represent 0

##speak function which will convert the text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait() ##it will basically stop

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("It is a fine morning sir !")

    elif hour >=12 and hour<18:
        speak("hope you had your brunch, Good Afternoon Sir !")

    else:
        speak("The wind is lovely, Good Evening Sir !")

    speak("Hello How are you? I am your personal AI Assistant Dave! How can I be of service")

# Function to change the AI's voice
def change_voice():
    current_voice = engine.getProperty('voice')
    if current_voice == voices[0].id:  # Male voice
        engine.setProperty('voice', voices[1].id)  # Female voice
        speak("Voice changed to female.")
    else:
        engine.setProperty('voice', voices[0].id)  # Male voice
        speak("Voice changed to male.")

##developing differenrt command
def command():
    r = sr.Recognizer() ## will convert speech to text
    with sr.Microphone() as source: ## one we are using is recognised google
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        r.pause_threshold = 1.2 ## that is the ai will take 1.2 seconds pause
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in') ##speech to text
        print(f"You said: {query} \n")
    except Exception as e:
        print("i could not get you, please speak again")
        speak("I could not get you please speak again")
        return "None"
    
    return query

##Writing different tasks for AI to perform
if __name__=="__main__": ## this is the root function
    greet()
    while True:
        query = command().lower() ##coverting it into lower case

        #Logic for executing taks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(f'{query}',sentences=2) ##will just give me first two sentences
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")

        elif 'search on google' in query:
            speak("What would you like to search for?")
            search_query = command()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'the weather' in query:
            webbrowser.open("https://www.msn.com/en-ca/weather/forecast/in-Ottawa,Ontario?loc=eyJsIjoiT3R0YXdhIiwiciI6Ik9udGFyaW8iLCJyMiI6Ik90dGF3YSIsImMiOiJDYW5hZGEiLCJpIjoiQ0EiLCJnIjoiZW4tY2EiLCJ4IjoiLTc1LjY5MjQiLCJ5IjoiNDUuNDIwNCJ9&weadegreetype=C&ocid=winp2fptaskbar&cvid=36cb0e19ac7644dba33c69f30bec5a63&content=TeaserDayTempChange_wxnwtsdtr2t111/")

        elif 'play music' in query or 'open spotify' in query:
            webbrowser.open("https://open.spotify.com/")
            speak("Opening Spotify.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'search on youtube' in query:
            speak("What would you like to search for?")
            search_query = command()
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

        elif 'change voice' in query:
            change_voice()

        elif 'open notepad' in query:
            os.system("notepad.exe")

        elif 'take a note' in query or 'note' in query:
            speak("Opening Notepad for you...")
            os.system("notepad.exe")

            time.sleep(2)  # Wait a bit for Notepad to open
            speak("What would you like me to write?")
            note = command()

            time.sleep(1)
            pyautogui.write(note, interval=0.05)  # types the note into Notepad
            speak("Your note has been written in Notepad.")

        elif 'set alarm' in query:
            speak("For how many minutes?")
            duration = int(command())
            time.sleep(duration * 60)
            speak("Time's up! Your alarm is ringing.")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye, Sir!")
            break

        else:
            speak("I'm sorry, I didn't understand that. Could you please repeat or try another command?")



