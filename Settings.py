from tkinter import *
from tkinter import ttk

def SettingsWindow():
    SettingsWindow = Tk()
    SettingsWindow.geometry('300x200')
    SettingsWindow.title('Settings')
    SettingsWindow['bg'] = 'pink'
    SettingsWindow.resizable(False, False)
    SettingsWindow.iconbitmap('SettingsIcon.ico')
