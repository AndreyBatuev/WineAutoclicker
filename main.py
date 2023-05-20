import pyautogui
import time
from tkinter import *
from tkinter import ttk
from time import sleep

import Settings
import About
window = Tk()
window.geometry('375x250')
window.title('Wine Autoclicker')
window['bg'] = 'pink'
window.resizable(False, False)
window.iconbitmap('Icon.ico')

CursorX, CursorY = pyautogui.position()

TimeClicks = 0
IntervalClicks = 0

EntIntClicksLb = Label(window, text='Enter the interval clicks', bg = 'red', fg = 'white')
EntIntClicksLb.place(x=10,y=15)

EntTimeClicksLb = Label(window, text='Enter the time clicks (-1 for eterno)', bg = 'red', fg = 'white')
EntTimeClicksLb.place(x=10,y=40)

MouseButtonSelection  = IntVar()
RightRadioBtn = Radiobutton(text="Right",bg='red', variable=MouseButtonSelection, value=0)
RightRadioBtn.place(x=10,y=65)
LeftRadioBtn = Radiobutton(text="Left",bg='red', variable=MouseButtonSelection, value=1)
LeftRadioBtn.place(x=80,y=65)

MvLeftLb = Label(window, text='Move cursor to the left', bg = 'red', fg = 'white')
MvLeftLb.place(x=10,y=95)

MvRightLb = Label(window, text='Move cursor to the right', bg = 'red', fg = 'white')
MvRightLb.place(x=10,y=120)

MvUpLb = Label(window, text='Move cursor to the up', bg = 'red', fg = 'white')
MvUpLb.place(x=10,y=145)

MvDownLb = Label(window, text='Move cursor to the down', bg = 'red', fg = 'white')
MvDownLb.place(x=10,y=170)

CursorStatusNowLb = Label(window, text='The cursor now is x = ' + str(CursorX) + ' y = ' + str(CursorY), bg = 'crimson', fg = 'white')
CursorStatusNowLb.place(x=40,y=195)


EntIntEntry = Entry(window, bg='#d77bba',fg='white')
EntIntEntry.insert(0, "0")
EntIntEntry.place(x=225,y=15)

EntTimeEntry = Entry(window, bg='#d77bba',fg='white')
EntTimeEntry.insert(0, "0")
EntTimeEntry.place(x=225,y=40)

EntMvLEntry = Entry(window, bg='#d77bba',fg='white')
EntMvLEntry.insert(0, "0")
EntMvLEntry.place(x=225,y=90)

EntMvREntry = Entry(window, bg='#d77bba',fg='white')
EntMvREntry.insert(0, "0")
EntMvREntry.place(x=225,y=115)

EntMvUEntry = Entry(window, bg='#d77bba',fg='white')
EntMvUEntry.insert(0, "0")
EntMvUEntry.place(x=225,y=140)

EntMvDEntry = Entry(window, bg='#d77bba',fg='white')
EntMvDEntry.insert(0, "0")
EntMvDEntry.place(x=225,y=165)

def ButtonStart():
    intervalClicks = float(EntIntEntry.get())
    NowTime = 0
    TimeClicks = EntTimeEntry.get()
    
    i = 0
    EndTime = time.time() + float(TimeClicks)
    if TimeClicks == -1:
        TimeClicks = 2147483647
    while True:
        if EndTime <= time.time():
            break
        
        # for infinite while
        if TimeClicks == 2147483647:
            TimeClicks = 2147483647 
        
        mouseButton = 'right'
        if MouseButtonSelection == 0:
            mouseButton = 'right'
        else:
            mouseButton = 'left'
        
        sleep(intervalClicks)

        NowX, NowY = pyautogui.position()   
        
        NowX = NowX + int(EntMvREntry.get())
        NowX = NowX - int(EntMvLEntry.get())
        NowY = NowY + int(EntMvDEntry.get())
        NowY = NowY + int(EntMvUEntry.get())
        pyautogui.dragTo(NowX, NowY, button=mouseButton)
        
        i += 1
def CreateSettingsWindow():
    Settings.SettingsWindow()
def CreateAboutWindow():
    About.AboutWindow()

AboutBtn = Button(window, text = "About", command=CreateAboutWindow, bg='#d95763', fg='white')
AboutBtn.place(x=10,y=220)

SetingsBtn = Button(window, text = "Settings", command=CreateSettingsWindow, bg='#d95763', fg='white')
SetingsBtn.place(x=240,y=220)

StartBtn = Button(window, text = "Start", command=ButtonStart, bg='#d95763', fg='white')
StartBtn.place(x=300,y=220)

def Refresher():
    NowX, NowY = pyautogui.position()
    temp = 'The cursor now is x = ' + str(NowX) + ' y = ' + str(NowY)
    CursorStatusNowLb.config(text = temp)
    window.after(1000, Refresher)
    
Refresher()
window.mainloop()