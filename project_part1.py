import speech_recognition as sr
import string
import os as s
import sys
try:
    while(True):
        def hel():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=5)
                print("Tell Me Your Application!")
                audio = r.listen(source,phrase_time_limit=5)
                text = str(r.recognize_google(audio))
            return text
        def hel2():
            y=hel()
            print y
            if (y == 'notepad' or y=='not bad' or y=='notbad'):
                s.startfile("notepad.exe")
            elif (y == 'Chrome'):
                s.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
            elif (y == 'putty'):
                s.startfile("C:\Users\Vikendra singh\Desktop\putty")
            elif (y == 'Explorer'):
                s.startfile("C:\Program Files\Internet Explorer\iexplore.exe")
            elif (y == 'Vlc'):
                s.startfile("C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")
            elif (y == 'Microsoft Excel'):
                s.startfile("C:\\Program Files (x86)\\Microsoft Office\\root\Office16\\EXCEL.EXE")
            elif (y == 'Microsoft Word'):
                s.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word 2016")
            elif (y == 'Microsoft PowerPoint'):
                s.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint 2016")
            elif (y == 'Adobe Reader'):
                s.startfile("C:\Program Files (x86)\Adobe\Reader 11.0\Reader\AcroRd32.exe")
            elif (y == 'Dev C plus plus'):
                s.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Bloodshed Dev-C++\Dev-C++")
            else:
                print 'Sorry Bad Command:'
                sys.exit()
        hel2()
except Exception as e:
    print (e)
