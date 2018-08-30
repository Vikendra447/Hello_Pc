from Tkinter import *
from math import *
import speech_recognition as sr
import string
import os as s
root=Tk()
root.title('CALCULATOR')
root.geometry('400x450')
    
e=Entry(root, width=18, font='Arial 30 bold', bd=5,bg='gray', relief='sunken',justify='left')
e.grid(row=0, column=0, columnspan=4)
def add_entry(x):
    e.insert(28, x)
def result(y):
    e.delete(0, END)
    e.insert(28, y)
def clear():
    e.delete(0, END)
def back():
    e.delete(0,1)
b0=Button(root, text='7', width=3, height=3, command=lambda:add_entry('7'))
b0.grid(row=1,column=0, sticky=E+W+N+S)

b1=Button(root, text='8', width=3, height=3, command=lambda:add_entry('8'))
b1.grid(row=1,column=1, sticky=E+W+N+S)

b2=Button(root, text='9', width=3, height=3, command=lambda:add_entry('9'))
b2.grid(row=1,column=2, sticky=E+W+N+S)

b3=Button(root, text='+', width=3, height=3, command=lambda:add_entry('+'))
b3.grid(row=1,column=3, sticky=E+W+N+S)

b4=Button(root, text='4', width=3, height=3, command=lambda:add_entry('4'))
b4.grid(row=2,column=0, sticky=E+W+N+S)

b5=Button(root, text='5', width=3, height=3, command=lambda:add_entry('5'))
b5.grid(row=2,column=1, sticky=E+W+N+S)

b6=Button(root, text='6', width=3, height=3, command=lambda:add_entry('6'))
b6.grid(row=2,column=2, sticky=E+W+N+S)

b7=Button(root, text='-', width=3, height=3, command=lambda:add_entry('-'))
b7.grid(row=2,column=3, sticky=E+W+N+S)

b8=Button(root, text='1', width=3, height=3, command=lambda:add_entry('1'))
b8.grid(row=3,column=0, sticky=E+W+N+S)

b9=Button(root, text='2', width=3, height=3, command=lambda:add_entry('2'))
b9.grid(row=3,column=1, sticky=E+W+N+S)

b10=Button(root, text='3', width=3, height=3, command=lambda:add_entry('3'))
b10.grid(row=3,column=2, sticky=E+W+N+S)

b11=Button(root, text='*', width=3, height=3, command=lambda:add_entry('*'))
b11.grid(row=3,column=3, sticky=E+W+N+S)

b12=Button(root, text='0', width=3, height=3, command=lambda:add_entry('0'))
b12.grid(row=4,column=0, sticky=E+W+N+S)

b13=Button(root,text=',',  width=3,height=3,command=lambda:add_entry(','))
b13.grid(row=4,column=1,sticky=E+W+N+S)

b14=Button(root, text='.', width=3, height=3, command=lambda:add_entry('.'))
b14.grid(row=4,column=2, sticky=E+W+N+S)

b15=Button(root, text='/', width=3, height=3, command=lambda:add_entry('/'))
b15.grid(row=4,column=3, sticky=E+W+N+S)

b16=Button(root,text='PI', width=3,height=3,command=lambda:add_entry('pi'))
b16.grid(row=5,column=0, sticky=E+W+N+S)

b17=Button(root,text='COS',width=3,height=3,command=lambda:add_entry('cos('))
b17.grid(row=5,column=1,sticky=E+W+N+S)

b18=Button(root,text='SIN',width=3,height=3,command=lambda:add_entry('sin('))
b18.grid(row=5,column=2,sticky=E+W+N+S)

b19=Button(root,text='TAN',width=3,height=3,command=lambda:add_entry('tan('))
b19.grid(row=5,column=3,sticky=E+W+N+S)

b20=Button(root,text='LOG',width=3,height=3,command=lambda:add_entry('log('))
b20.grid(row=6,column=0,sticky=E+W+N+S)

b21=Button(root,text='SQRT',width=3,height=3,command=lambda:add_entry('sqrt('))
b21.grid(row=6,column=1,sticky=E+W+N+S)

b22=Button(root, text='<-', width=3, height=3, command=lambda:back())
b22.grid(row=6,column=2, sticky=E+W+N+S)

b23=Button(root, text='C', width=3, height=3, command=lambda:clear())
b23.grid(row=6,column=3, sticky=E+W+N+S)

b24=Button(root, text='=', width=3, height=3, command=lambda:result(eval(e.get())))
b24.grid(row=7,column=0, sticky=E+W+N+S)

b25=Button(root, text='POWER', width=3, height=3, command=lambda:add_entry('**'))
b25.grid(row=7,column=1, sticky=E+W+N+S)

b26=Button(root, text='(', width=3, height=3, command=lambda:add_entry('('))
b26.grid(row=7,column=2, sticky=E+W+N+S)

b27=Button(root, text=')', width=3, height=3, command=lambda:add_entry(')'))
b27.grid(row=7,column=3, sticky=E+W+N+S)
try:
    while (True==True):
        def voice():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=5)
                print("Give Some Input!")
                audio = r.listen(source,phrase_time_limit=5)
                response = str(r.recognize_google(audio))
            return response
        def calc():
            n=0
            k=0
            y=[n]
            x=voice()
            print x
            if (x=='7' or x=='heaven' or x=='seven'):
                y[n]=b0.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)
    
            elif (x=='8' or x=='IIT' or x=='iit' or x=='eight'):
                y[n]=b1.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='9' or x=='nine' or x=='fine' or x=='vine' or x=='mine' or x=='wine'):
                y[n]=b2.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='+' or x=='plus'):
                y[n]=b3.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='4' or x=='four' or x=='hour' or x=='for'):
                y[n]=b4.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='5' or x=='hi' or x=='five'):
                y[n]=b5.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='6' or x=='six' or x=='sic' or x=='fix'):
                y[n]=b6.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='-' or x=='minus'):
                y[n]=b7.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='1' or x=='one' or x=='onn' or x=='on'):
                y[n]=b8.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='2' or x=='two' or x=='to' or x=='to' or x=='do'):
                y[n]=b9.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='3' or x=='three' or x=='free' or x=='ree'):
                y[n]=b10.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='into' or x=='Pintu' or x=='Mintu' or x=='Chintu'):
                y[n]=b11.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='0' or x=='zero'):
                y[n]=b12.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='oma' or x=='comma' or x==','):
                y[n]=b13.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='point' or x=='joint'):
                y[n]=b14.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='divide by' or x=='what why'):
                y[n]=b15.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='I' or x=='i' or x=='bhai' or x=='my' or x=='pi'):
                y[n]=b16.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='cause of' or x=='cause off' or x=='call of' or x=='call off'):
                y[n]=b17.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='I know' or x=='sign of' or x=='sign off' or x=='sin of' or x=='sin off'):
                y[n]=b18.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='tan of' or x=='tan off' or x=='turn of' or x=='turn off' or x=='and of' or x=='and off'):
                y[n]=b19.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='log off' or x=='log of' or x=='loss of' or x=='loss off'):
                y[n]=b20.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='square root of' or x=='square root off'):
                y[n]=b21.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='back' or x=='hack' or x=='map'):
                y[n]=b22.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='clear' or x=='fear' or x=='dear' or x=='near'):
                y[n]=b23.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='=' or x=='equal' or x=='equals' or x=='equals to' or x=='equal to' or x=='equal 2' or x=='eqaul two' or x=='equal tu' or x=='equals 2' or x=='equals two' or x=='equals tu'):
                y[n]=b24.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='power of' or x=='power off'):
                y[n]=b25.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='opening bracket'):
                y[n]=b26.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)

            elif (x=='closing bracket'):
                y[n]=b27.invoke()
                y.remove('None')
                k=','.join(repr(e) for e in y)
                add_entry(k)
            else:
                print 'Sorry Bad Command:'
                sys.exit()

            root.update_idletasks()
            root.update()
        calc()
except Exception as e:
    print (e)
root.mainloop()
