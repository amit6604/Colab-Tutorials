# Converting Text Files To Audio File Using Python 

from gtts import gTTS
import os
import tkinter as tk
from playsound import playsound
from tkinter import filedialog

win = tk.Tk()
win.minsize(160,160)
win.maxsize(260,260)


def ChooseFile():
	global content
	file = filedialog.askopenfile(filetypes = [('Text Files', '*.txt')])
	sfile = tk.Label(win, text=f"Selected File : {file.name}")
	sfile.grid(row=1, column=0, columnspan=2)
	if file is not None:
		content = file.read()
	return content



def Convert():
	text = content
	speech = gTTS(text = content, lang="en-in")
	path = os.getcwd() + "\Speech.mp3"
	speech.save(path)
	
	playsound(path)


label = tk.Label(win, text="Select File")
label.grid(row=0, column=0, padx=8, pady=8)


button = tk.Button(win, text="Select", command=ChooseFile)
button.grid(row=0, column=1, padx=8, pady=8)


button2 = tk.Button(win, text="Convert Audio", command=Convert)
button2.grid(row=2, column=0, columnspan=2, padx=8, pady=8)

win.mainloop()
