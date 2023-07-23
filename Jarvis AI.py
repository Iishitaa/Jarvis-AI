import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
from api import api_key
import random
import smtplib
import wikipedia
import win32com.client

emails = [["Ishita", "ig374@snu.edu.in"], ["Mummy", "drkirtijagupta@gmail.com"], ["uncle", "suneelgi@gmail.com" ],["arihant", "aj534@snu.edu.in"]]
sites = [["youtube", "https:/www.youtube.com"], ["wikipedia", "https:/www.wikipedia.com"], ["google", "https:/www.google.com"], ["facebook", "https:/www.facebook.com"], ["instagram", "https:/www.instagram.com"], ["twitter", "https:/www.twitter.com"], ["linkedin", "https:/www.linkedin.com"], ["reddit", "https:/www.reddit.com"], ["stack overflow", "https://stackoverflow.com/"], ["github", "https:/www.github.com"], ["amazon", "https:/www.amazon.com"], ["netflix", "https:/www.netflix.com"], ["spotify", "https:/www.spotify.com"], ["pinterest", "https:/www.pinterest.com"]]
apps = [["chrome", "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"], ["notepad", "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2304.26.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"], ["Word", "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"], ["excel", "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"], ["powerpoint", "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"],["whatsapp", "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2327.6.0_x64__cv1g1gvanyjgm\\WhatsApp.exe"], ["Prime", "C:\\Program Files\\WindowsApps\\AmazonVideo.PrimeVideo_1.0.145.0_x64__pwbj9vvecjh7j\\PrimeVideo.exe"], ["snipping tool", "C:\\Program Files\\WindowsApps\\Microsoft.ScreenSketch_11.2303.17.0_x64__8wekyb3d8bbwe\\SnippingTool\\SnippingTool.exe"]]

chat = ""
def talk_to_user(query):

    global chat
    #print(chat)
    openai.api_key = api_key
    chat = f"Ishita: {query}\n Jarvis: "

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= chat,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    speak(response["choices"][0]["text"])
    chat += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
    

def artificiall_int(prompt):

    some_string = f"Response for prompt by OpenAI is : {prompt} \n *************** \n\n"
    openai.api_key = api_key

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    #print(response["choices"][0]["text"])
    some_string += response["choices"][0]["text"]
    if not os.path.exists("AI files"):
        os.mkdir("AI files")

    with open(f"AI files/prompt - {random.randint(1,100)}", "w") as f:
        f.write(some_string)

def speak(text):
    speak = win32com.client.Dispatch("SAPI.SpVoice")
    speak.Speak(text)

def takeCommand(): # it takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognizing...\n")
            query = r.recognize_google(audio, language= "en-in")
            print(f"user said : {query}")
            return query
        except:
            return "sorry, some error occured."
        
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("ishitagupta8960@gmail.com", "zfhcztjvqychfiaj")
    server.sendmail("ishitagupta8960@gmail.com", to, content)
    server.close()

if __name__ == '__main__':

    speak("Hello there, I am Jarvis! How can I help you today?")

    while True:
        print("listening...\n")

        #text = takeCommand()
        #speak(text)

        query = takeCommand()

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} ma'am...")
                webbrowser.open(site[1])

        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                speak(f"Opening {app[0]} ma'am...")
                os.startfile(app[1])
        
        try:
            for mail in emails:
                if f"send mail to {mail[0]}".lower() in query.lower():
                    speak("What should I say?")
                    content = takeCommand()
                    sendEmail(mail[1], content)
                    speak("Email has been sent!")
        except Exception as e:
                print(e)
                speak("Sorry, I am unable to send the email")

        if "wikipedia".lower() in query.lower():
            speak("Searching Wikipedia...\n")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)   

        elif "open music" in query:
            musicPath = "\\Users\\ASUS\\Desktop\\python\\jarvis project\\vinee-heights-126947.mp3"
            os.startfile(musicPath)

        elif "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"ma'am the current time is {current_time}")
                    

        elif "open discord".lower() in query.lower():
            path = "\\Users\\ASUS\\AppData\\Local\\Discord\\app-1.0.9015\\Discord.exe"
            os.startfile(path)

        elif "using AI".lower() in query.lower():
            artificiall_int(prompt = query)
        
        elif "Jarvis quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chat = ""

        else:   
            print("Chatting...\n")
            talk_to_user(query)

        


        

            
          



            
            


                
            

        

    








    

