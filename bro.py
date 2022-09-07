import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import facedetect
import screenshot
import weather


engine = pyttsx3.init ('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak('Good Morning bro')
    elif hour>=12 and hour < 18:
        speak('Good Afternoon bro')
    else:
        speak('Good Evening bro')
    speak(' how may I help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source,duration=0.5)
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)

    try:
        print("recognising...")
        query = r.recognize_google(audio, language='eng-in')
        print("User said: ",query)
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your-email','your-password')
    server.sendmail('your email',to,content)
    server.close()


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    
        #logic
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'hello' in query:
            speak('hey there')

        elif 'how are you' in query:
            speak('i am good, thanks for asking')

        elif 'who are you' in query:
            speak('I am your bro, your virtual assistant')
        
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('https://www.youtube.com/')

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open('https://www.google.co.in/webhp?tab=rw&authuser=0')

        elif 'open classroom' in query:
            speak('opening google classroom')
            webbrowser.open('https://classroom.google.com/u/1/h')

        elif 'open map' in query:
            speak('opening google maps')
            webbrowser.open('https://www.google.co.in/maps/@28.9931264,77.6667136,14z?hl=en&authuser=0')

        elif 'open photos' in query:
            speak('opening google photos')
            webbrowser.open('https://www.google.com/photos/about/')

        elif 'open meet' in query:
            speak('opening google meet')
            webbrowser.open('https://meet.google.com/')

        elif 'open skype' in query:
            speak('opening skype')
            webbrowser.open('https://www.skype.com/en/')

        elif 'open drive' in query:
            speak('opening google drive')
            webbrowser.open('https://accounts.google.com/ServiceLogin/signinchooser?service=wise&passive=1209600&continue=https%3A%2F%2Fdrive.google.com%2F%3Ftab%3Dro&followup=https%3A%2F%2Fdrive.google.com%2F%3Ftab%3Dro&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

        elif 'open news' in query:
            speak('opening google news')
            webbrowser.open('https://news.google.com/topstories?tab=rn&hl=en-IN&gl=IN&ceid=IN:en')

        elif 'open calendar' in query:
            speak('opening calendar')
            webbrowser.open('https://accounts.google.com/ServiceLogin/signinchooser?service=cl&passive=1209600&osid=1&continue=https%3A%2F%2Fcalendar.google.com%2Fcalendar%2Frender%3Ftab%3Drc&followup=https%3A%2F%2Fcalendar.google.com%2Fcalendar%2Frender%3Ftab%3Drc&scc=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

        elif 'open docs' in query:
            speak('opening google docs')
            webbrowser.open('https://accounts.google.com/ServiceLogin/signinchooser?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fdocument%2Fu%2F0%2F&followup=https%3A%2F%2Fdocs.google.com%2Fdocument%2Fu%2F0%2F&ltmpl=docs&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

        elif 'open slides' in query:
            speak('opening google slides')
            webbrowser.open('https://accounts.google.com/ServiceLogin/signinchooser?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fpresentation%2F%3Fusp%3Dslides_alc&followup=https%3A%2F%2Fdocs.google.com%2Fpresentation%2F%3Fusp%3Dslides_alc&ltmpl=slides&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        
        elif 'open sheets' in query:
            speak('opening google sheets')
            webbrowser.open('https://accounts.google.com/ServiceLogin/signinchooser?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2F%3Fusp%3Dsheets_alc&followup=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2F%3Fusp%3Dsheets_alc&ltmpl=sheets&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

        elif 'open gmail' in query:
            speak('opening gmail')
            webbrowser.open('https://accounts.google.com/ServiceLogin/signinchooser?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Ftab%3Drm%26ogbl&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

        elif 'open whatsapp' in query:
            speak('opening whatsapp')
            webbrowser.open('https://web.whatsapp.com/')

        elif 'open facebook' in query:
            speak('opening facebook')
            webbrowser.open('https://www.facebook.com/')

        elif 'open linkedin' in query:
            speak('opening linkedin')
            webbrowser.open('https://www.linkedin.com/home')

        elif 'open instagram' in query:
            speak('opening instagram')
            webbrowser.open('https://www.instagram.com/')

        elif 'open twitter' in query:
            speak('opening twitter')
            webbrowser.open('https://twitter.com/login?lang=en-gb')
        
        elif 'open snapchat' in query:
            speak('opening snapchat')
            webbrowser.open('https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fwelcome')

        elif 'open myntra' in query:
            speak('opening myntra')
            webbrowser.open('https://www.myntra.com/login')

        elif 'open amazon' in query:
            speak('opening amazon')
            webbrowser.open('https://www.amazon.in/ref=nav_logo')

        elif 'open flipkart' in query:
            speak('opening flipkart')
            webbrowser.open('https://www.flipkart.com/')

        elif 'open hacker rank' in query:
            speak('opening hacker rank')
            webbrowser.open('https://www.hackerrank.com/dashboard')

        elif 'open leet code' in query:
            speak('opening leet code')
            webbrowser.open('https://leetcode.com/')

        elif 'open codetantra' in query:
            speak('opening codetantra')
            webbrowser.open('https://miet.codetantra.com/login.jsp')

        elif 'open udemy' in query:
            speak('opening udemy')
            webbrowser.open('https://www.udemy.com/')

        elif 'open cousrera' in query:
            speak('opening coursera')
            webbrowser.open('https://www.coursera.org/in')

        elif 'open salesforce ' in query:
            speak('opening salesforce')
            webbrowser.open('https://login.salesforce.com/?locale=eu')

        elif 'open trailhead ' in query:
            speak('opening trailhead')
            webbrowser.open('https://trailhead.salesforce.com/en/home')
        
        elif 'open code chef ' in query:
            speak('opening code chef')
            webbrowser.open('https://www.codechef.com/')

        elif 'open codeforces' in query:
            speak('opening code forces')
            webbrowser.open('https://codeforces.com/')

        elif 'open aws' in query:
            speak('opening aws')
            webbrowser.open('https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Faws.amazon.com%2Fmarketplace%2Fmanagement%2Fsignin%3Fstate%3DhashArgs%2523%26isauthcode%3Dtrue&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Faws-mp-seller-management-portal&forceMobileApp=0&code_challenge=eV4_nIcey629jmh7YGUl5UV9XAAm5oa2g1r1VytD3Wc&code_challenge_method=SHA-256')

        elif 'open one view' in query:
            speak('opening one view')
            webbrowser.open('https://erp.aktu.ac.in/webpages/oneview/oneview.aspx')
        
        elif 'open github' in query:
            speak('opening github')
            webbrowser.open('https://github.com/')
        
        elif 'open geeks for geeks' in query:
            speak('opening geeks for geeks')
            webbrowser.open('https://www.geeksforgeeks.org/')
        
        elif 'open programiz' in query:
            speak('opening programiz')
            webbrowser.open('https://www.programiz.com/')

        elif 'open swiggy' in query:
            speak('opening swiggy')
            webbrowser.open('https://www.swiggy.com/')

        elif 'open uber' in query:
            speak('opening upen')
            webbrowser.open('https://auth.uber.com/login/?breeze_local_zone=phx3&next_url=https%3A%2F%2Fm.uber.com%2F&state=pcQ-DTjD_CyH2UoOQUcDsL_2VW7-8yXfU9R-25cvNe4%3D')

        elif 'open zomato' in query:
            speak('opening zomato')
            webbrowser.open('https://www.zomato.com/akola/restaurants?context=delivery')

        elif "open domino's" in query:
            speak("opening domino's")
            webbrowser.open('https://www.dominos.co.in/')

        elif 'open pizza hut' in query:
            speak('opening pizza hut')
            webbrowser.open('https://www.pizzahut.co.in/')

        elif 'open burger king' in query:
            speak('opening burger king')
            webbrowser.open('https://www.burgerking.in/')

        elif 'open hdfc' in query:
            speak('opening hdfc')
            webbrowser.open('https://netbanking.hdfcbank.com/netbanking/')

        elif 'open pnb' in query:
            speak('opening pnb net banking')
            webbrowser.open('https://netpnb.com/')

        elif 'open sbi' in query:
            speak('opening sbi net banking')
            webbrowser.open('https://retail.onlinesbi.com/retail/login.htm')

        elif 'open kfc' in query:
            speak('opening kfc')
            webbrowser.open('https://online.kfc.co.in/home')

        elif 'open Netflix' in query:
            speak('opening Netflix')
            webbrowser.open('https://www.netflix.com/in/')
        
        elif 'open prime' in query:
            speak('opening prime')
            webbrowser.open('https://www.primevideo.com/')

        elif 'open hotstar' in query:
            speak('opening hotstar')
            webbrowser.open('https://www.hotstar.com/in')

        elif 'open sonyliv' in query:
            speak('opening sonyliv')
            webbrowser.open('https://www.sonyliv.com/')

        elif 'open zee5' in query:
            speak('opening zee5')
            webbrowser.open('https://www.zee5.com/')

        elif 'open voot' in query:
            speak('opening voot')
            webbrowser.open('https://www.voot.com/')

        elif 'play music' in query:
            speak('playing music')
            music_dir = 'C:\\Users\\Lenovo\\OneDrive\\Desktop\\Vro-The-Virtual-Assistant-main\\Vro-The-Virtual-Assistant-main\music_dir'
            songs = os.listdir(music_dir)
            i=random.randint(1,6) #change the range by adding your favourite music to the music_dir.
            os.startfile(os.path.join(music_dir,songs[i]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Lenovo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codepath)

        elif 'open excel' in query:
            codepath = "C:\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codepath)

        elif 'open powerpoint' in query:
            codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(codepath)

        elif 'open word' in query:
            codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codepath)

        elif "open face detection" in query:
            speak('opening face detection')
            facedetect.detect()

        elif "screenshot" in query:
            speak('Taking screen shot')
            screenshot.screenshot()

        elif "temperature" in query:
            speak('Name the place of which you want to know the temperature')
            place=takeCommand().lower()
            temp=weather.temperature(place)
            string=f"temperature in {place} now is {temp}"
            speak(string)

        elif 'send email' in query:
            try:
                speak('What shaould i say?')
                content = takeCommand()
                to = 'your email'
                sendEmail(to, content)
                speak('Email ha been sent!')
            except Exception as e:
                print(e)
                speak("Sorry sir, unable to send this eamil")

        elif 'thank you' in query:
            speak('My Pleasure')
            quit()

        #else:
            #speak("i don't have any answer for that, would you like to ask anything else")