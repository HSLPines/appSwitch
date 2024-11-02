
import keyboard
import subprocess
import os
import sys
import time
from tkinter import Tk, Canvas

# Function to create a black screen
def show_black_screen():

    black_screen = Tk()
    black_screen.attributes('-fullscreen', True)
    black_screen.configure(background='black')
    black_screen.bind("<Escape>", lambda e: black_screen.destroy())
    black_screen.mainloop()

# Function to open Chrome
def open_chrome():
    if sys.platform == "win32":
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        subprocess.Popen([chrome_path])
    elif sys.platform == "darwin":  # macOS
        subprocess.Popen(["open", "-a", "Google Chrome"])
    elif sys.platform == "linux":
        subprocess.Popen(["google-chrome"])

# Function to open the terminal
def open_terminal():
    if sys.platform == "win32":
        subprocess.Popen("start cmd", shell=True)
    elif sys.platform == "darwin":  # macOS
        subprocess.Popen(["open", "-a", "Terminal"])
    elif sys.platform == "linux":
        subprocess.Popen(["gnome-terminal"])

print("Press 'b' for a black screen, 'c' to open Chrome, 't' to open Terminal, or 'esc' to exit.")

while True:
    if keyboard.is_pressed('b'):
        show_black_screen()
        time.sleep(0.5)  
    elif keyboard.is_pressed('c'):
        open_chrome()
        time.sleep(0.5)
    elif keyboard.is_pressed('t'):
        open_terminal()
        time.sleep(0.5)
    elif keyboard.is_pressed('esc'):
        print("Exiting program.")
        break
