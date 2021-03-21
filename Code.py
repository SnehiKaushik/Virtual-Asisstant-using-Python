from tkinter import *
from ttkthemes import themed_tk as tk
import pyttsx3
import speech_recognition as sr
from PyDictionary import PyDictionary
import datetime
import pyjokes
import pywhatkit
import wikipedia
import requests
import bs4
import smtplib
from email.message import EmailMessage


root = tk.ThemedTk()
root.title('spy')
root.geometry("520x350")
root.config(bg='black')
root.iconbitmap("circle (1) (1).ico")
root.get_themes()
root.set_theme('black')

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',130)
dictionary = PyDictionary()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("LISTENING....")
            listener.pause_threshold =1
            listener.energy_threshold = 10000
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'spy' in command:
                command = command.replace('spy','')
                print(command)
    except:
        pass
    return command


def run_spy():
    command = take_command()
    otherCommands = ['play','time','joke','define','tell me','email']
    for i in range(1):
        if otherCommands[0] in command or otherCommands[1] in command or otherCommands[2] in command or otherCommands[3] in command or otherCommands[4] in command or otherCommands[5] in command:
            break
        else:
            url ='https://google.com/search?q=' + command
            request_result = requests.get(url)
            soup = bs4.BeautifulSoup(request_result.text,'html.parser')
            answer = soup.find('div',class_ = 'BNeawe').text
            print(answer)
            talk(answer)
            break
    if 'define' in command:
        word = command.replace('define','')
        meaning = dictionary.meaning(word)
        print(meaning)
        talk(meaning)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'tell me' in command:
        question = command.replace('tell me','')
        info = wikipedia.summary(question,1)
        print(info)
        talk(info)
    elif 'email' in command:

        def send_email(receiver,subject,message):
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            #make sure to give app access to your gmail account
            server.login('snehikaushik9@gmail.com', 'PoZx098{#^')
            email = EmailMessage()
            email['From'] ='snehikaushik9@gmail.com'
            email['To'] = receiver
            email['Subject'] = subject
            email.set_content(message)
            server.send_message(email)



        email_list = {
            # 'name' : 'emailid@gmail.com',
            # 'name2' : 'emailid@gmail.com',
            # 'name3' : 'emailid@gmail.com'
            'john': 'chhavikaushik3@gmail.com',
            'snehi': 'snehikaushik9@gmail.com',
            'Harsh': 'harshverma98@gmail.com',
            'manan': 'manannagpal@gmail.com',
            'divij': 'divijnagpaldn@gmail.com',
            'rithik': 'rithikkhatri212@gmail.com'
        }
        def get_email_info():
            talk("To whom you want to send an email?")
            name = take_command()
            receiver = email_list[name]
            talk('what is the subject of your email?')
            subject = take_command()
            talk('please tell me the content of your email.')
            message = take_command()
            send_email(receiver,subject,message)
            talk('Your email is sent')
        get_email_info()


def start():
    talk("Hey, I am spy. How can i help you?")
    while True:
        run_spy()

middleframe = Frame(root)
middleframe.config(bg='black')
middleframe.pack()

SPY = PhotoImage(file = 'circle (1).png')
spy = Button(middleframe,image = SPY, bg = 'black' , activebackground = 'black',command = start)
spy.grid(row=0,column=2,padx=100,pady = 100)
root.mainloop()

# end of code