import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning My dear ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon My dear ")
    else:
        speak("good evening My dear ")
    speak("Let me know how can i help you , what are looking for?")


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you guna....")
        r.pause_threshold= 1
        audio=r.listen(source)



    try:
        print("Recognising your voice.....")
        query=r.recognize_google(audio, language='en-in')
        print(f"my dear you said :{query}\n")

    except Exception as e:
        print("Guna say that again please....")
        return "None"
    return query



def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('gunasekharreddy1122@gmail.com','wiunqydpzq')
    server.sendmail('sekharguna491@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'open wikipedia' in query:
            speak("Searching wikipedia.....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        if 'play music' in query:
            npath="C:\\Users\\gunas\\Music\\my music\\[iSongs.info] 01 - Ala Meda Mida.mp3"
            os.startfile(npath)
            
            
        elif 'open notepad' in query:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            

        elif 'open instagram' in query:
            webbrowser.open('https://www.instagram.com/')


        elif 'open google' in query:
            webbrowser.open('https://www.google.co.in/')
            

        elif 'tell me the time' in query:
            strTime=datetime.datetime.now().strftime("%H%M%S")
            speak(f"my dear time is {strTime}")


        elif 'open jonathan youtube channel' in query:
            webbrowser.open('https://www.youtube.com/c/JONATHANGAMINGYT')


        elif 'open linkedin' in query:
            webbrowser.open('https://www.linkedin.com/')
            

        elif 'email to other friend' in query:
            try:
                speak("what should I send?")
                content=takecommand()
                to="sekharguna491@gmail.com"
                sendEmail(to,content)
                speak("Your email has been sent successfully")

            except Exception as e:
                print(e)
                speak("my dear i am unable to send the email.... please address the error ")
                
        elif 'thank you' in query:
            speak('Its ok my love')
    









