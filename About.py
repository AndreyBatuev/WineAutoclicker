from tkinter import *
from tkinter import ttk

AboutText = ''' 
Program made by Andrey Batuev 2023 
MIT LICENSE
Official reposetory https://github.com/AndreyBatuev/WineAutoclicker


\t\t\t\t Version 0.08
'''

def AboutWindow():
    SettingsWindow = Tk()
    SettingsWindow.geometry('400x150')
    SettingsWindow.title('About')
    SettingsWindow['bg'] = 'pink'
    SettingsWindow.resizable(False, False)
    SettingsWindow.iconbitmap('AboutIcon.ico')
    Text = Label(SettingsWindow, text=AboutText, bg = 'red', fg = 'white')
    Text.place(x=10,y=10)
