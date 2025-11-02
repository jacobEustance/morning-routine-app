import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from time import strftime 
import fnmatch
import os
from pygame import mixer
import requests
import time
import random

root = tk.Tk()

root.geometry("1024x640")
root.title("Good Morning App")
root.configure(bg="grey15")  

# clock display in centre...

def Livetime():
    string = strftime('%H:%M:%S %p')
    label1.config(text=string)
    label1.after(1000, Livetime)

label1 = tk.Label(root, font=("ds-digital", 80), bg="grey15", fg="white")
label1.place(relx=0.5, rely=0.5, anchor='center')

Livetime()


# morning cklist top left...


from tkinter import messagebox

tasks = ['Electrolytes', 'breakfast', 'gym', 'coffee']

# Functions
def listtasks():
    listbox.delete(0, tk.END)
    for index, task in enumerate(tasks):
        listbox.insert(tk.END, f"{index + 1}. {task}")

def deltask():
    selected = listbox.curselection()  # get selected index
    if selected:
        task_index = selected[0]
        completed_task = tasks.pop(task_index)
        messagebox.showinfo("Task Completed", f"Task '{completed_task}' marked as done!")
        listtasks()
    else:
        messagebox.showwarning("No Selection", "Please select a task to complete.")


label7 = tk.Label(root, text="Your Tasks:", font=("Arial", 14))
label7.place(y=10, x=10)

listbox = tk.Listbox(root, width=30, height=10, fg='cyan',bg='gray15', justify='center')
listbox.place(y=56, x=10)
listtasks()

complete_button = tk.Button(root, text="               Complete", command=deltask)
complete_button.place(y=5, x=10)

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.place(y=5, x=10)


#music player top middle...




rootpath = "//Users/jacobeustance/Desktop/CODING/Python projects/own_projects/Morning_routine/music free"
pattern = '*.mp3'

mixer.init()

prev_img = tk.PhotoImage(file = 'prev_img.png')
next_img = tk.PhotoImage(file = 'next_img.png')
pause_img = tk.PhotoImage(file = 'pause_img.png')
play_img = tk.PhotoImage(file = 'play_img.png')
stop_img = tk.PhotoImage(file = 'stop_img.png')

def select():
    label2.config(text = listBox.get('anchor'))
    mixer.music.load(rootpath + '//' + listBox.get('anchor'))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label2.config(text = next_song_name)
    
    mixer.music.load(rootpath + '//' + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label2.config(text = next_song_name)
    
    mixer.music.load(rootpath + '//' + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def pause():
    if pauseButton['text'] == 'pause':
        mixer.music.pause()
        pauseButton['text'] = 'play'
    else: 
        mixer.music.unpause()
        pauseButton['text'] = 'pause'



listBox = tk.Listbox(root, fg = 'yellow', bg = 'grey15', width = 20, font = ('poppins', 14), justify='center')
listBox.pack(padx = 0, pady = 20,)

label2 = tk.Label(root, text = '', bg = 'grey15', fg = 'yellow', font = ('poppins', 18))
label2.pack(pady = 15)

top = tk.Frame(root, bg = 'grey15')
top.pack(padx = 10, pady = 5, anchor = 'center')

prevButton = tk.Button(root, text = 'prev', image = prev_img, background = 'grey15', borderwidth = 0, command = play_prev)
prevButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(root, text = 'stop', image = stop_img, bg = 'grey15', borderwidth = 0, command = stop)
stopButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(root, text = 'stop', image = play_img, bg = 'grey15', borderwidth = 0, command = select)
playButton.pack(pady = 15, in_ = top, side = 'left')

pauseButton = tk.Button(root, text = 'stop', image = pause_img, bg = 'grey15', borderwidth = 0, command = pause)
pauseButton.pack(pady = 15, in_ = top, side = 'left')

nextButton = tk.Button(root, text = 'stop', image = next_img, bg = 'grey15', borderwidth = 0, command = play_next)
nextButton.pack(pady = 15, in_ = top, side = 'left')

for roots, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)



#quote of the day bottom whole...



q = open("quotes.txt", "r")
quotes = q.readlines()
randomquote = random.choice(quotes)


index = quotes.index(randomquote)
a = open("authors.txt", "r")
authors = a.readlines()



label5 = tk.Label(root, font=("ds-digital", 20), bg="grey15", fg="white")
label5.config(text=f'"{randomquote.strip()}"\n- {authors[index].strip()}')
label5.pack(anchor='center', side='bottom', pady=200)

#weather top right...

def GetWeather(root):
    location =  textfield.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=2abb1ec02008546569362504212b0b21"
    try:
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind_speed = json_data['wind']['speed']
        time_offset = 3600
        sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] + time_offset))
        sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] + time_offset))

        final_info = condition + "\n" + str(temp) + ".C"
        final_data = "\n" + "Max temp: " + str(max_temp) + "\n" + "Min temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset) + "\n" + "wind speed: " + str(wind_speed)
        label3.config(text=final_info)
        label4.config(text=final_data)
    except Exception as e:
        label3.config(text="Weather error")
        label4.config(text=str(e))


f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(root, justify= "center", font = t, fg='cyan', bg='grey15')
textfield.place(x=1000, y=20)
textfield.focus()
textfield.bind('<Return>', GetWeather)

label3 = tk.Label(root, font = t, bg='grey15', fg='cyan', justify='center')
label3.place(x=1180, y=90)
label4 = tk.Label(root, font = f, bg='grey15', fg='cyan', justify='center')
label4.place(x=1180, y=170)






root.mainloop()
