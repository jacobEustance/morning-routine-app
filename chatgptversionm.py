import tkinter as tk
from tkinter import messagebox
from time import strftime
import fnmatch
import os
from pygame import mixer
import requests
import time
import random

# --- Main Window ---
root = tk.Tk()
root.geometry("1024x640")
root.title("Good Morning App")
root.configure(bg="#1c1c1c")  # dark background

# --- Clock in center ---
def Livetime():
    string = strftime('%H:%M:%S %p')
    clock_label.config(text=string)
    clock_label.after(1000, Livetime)

clock_label = tk.Label(root, font=("ds-digital", 80), bg="#1c1c1c", fg="#00ffff")
clock_label.place(relx=0.5, rely=0.5, anchor='center')
Livetime()

# --- Tasks Top Left ---
tasks = ['Electrolytes', 'breakfast', 'gym', 'coffee']

def listtasks():
    task_listbox.delete(0, tk.END)
    for index, task in enumerate(tasks):
        task_listbox.insert(tk.END, f"{index + 1}. {task}")

def deltask():
    selected = task_listbox.curselection()
    if selected:
        task_index = selected[0]
        completed_task = tasks.pop(task_index)
        messagebox.showinfo("Task Completed", f"Task '{completed_task}' marked as done!")
        listtasks()
    else:
        messagebox.showwarning("No Selection", "Please select a task to complete.")

task_frame = tk.Frame(root, bg="#2a2a2a", bd=2, relief="ridge")
task_frame.place(x=10, y=10, width=250, height=300)

task_label = tk.Label(task_frame, text="Morning Tasks", font=("Arial", 16, "bold"), bg="#2a2a2a", fg="white")
task_label.pack(pady=5)

task_listbox = tk.Listbox(task_frame, width=30, height=10, bg="#1c1c1c", fg="cyan", font=("Arial", 12))
task_listbox.pack(pady=5)

complete_button = tk.Button(task_frame, text="Complete Task", bg="#00bfff", fg="white", command=deltask)
complete_button.pack(pady=5)

listtasks()

# --- Music Player Top Center ---
rootpath = "//Users/jacobeustance/Desktop/CODING/Python projects/own_projects/Morning_routine/music free"
pattern = '*.mp3'
mixer.init()

# Load icons
prev_img = tk.PhotoImage(file='prev_img.png')
next_img = tk.PhotoImage(file='next_img.png')
pause_img = tk.PhotoImage(file='pause_img.png')
play_img = tk.PhotoImage(file='play_img.png')
stop_img = tk.PhotoImage(file='stop_img.png')

def select():
    label_song.config(text=music_listbox.get('anchor'))
    mixer.music.load(rootpath + '/' + music_listbox.get('anchor'))
    mixer.music.play()

def stop():
    mixer.music.stop()
    music_listbox.select_clear('active')

def play_next():
    next_song = music_listbox.curselection()
    next_song = next_song[0] + 1
    next_song_name = music_listbox.get(next_song)
    label_song.config(text=next_song_name)
    mixer.music.load(rootpath + '/' + next_song_name)
    mixer.music.play()
    music_listbox.select_clear(0, 'end')
    music_listbox.activate(next_song)
    music_listbox.select_set(next_song)

def play_prev():
    prev_song = music_listbox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = music_listbox.get(prev_song)
    label_song.config(text=prev_song_name)
    mixer.music.load(rootpath + '/' + prev_song_name)
    mixer.music.play()
    music_listbox.select_clear(0, 'end')
    music_listbox.activate(prev_song)
    music_listbox.select_set(prev_song)

def pause():
    if pause_btn['text'] == 'pause':
        mixer.music.pause()
        pause_btn['text'] = 'play'
    else:
        mixer.music.unpause()
        pause_btn['text'] = 'pause'

music_frame = tk.Frame(root, bg="#2a2a2a", bd=2, relief="ridge")
music_frame.place(relx=0.5, y=10, anchor='n', width=400, height=250)

music_label = tk.Label(music_frame, text="Music Player", font=("Arial", 16, "bold"), bg="#2a2a2a", fg="white")
music_label.pack(pady=5)

music_listbox = tk.Listbox(music_frame, width=40, height=8, bg="#1c1c1c", fg="yellow", font=("Arial", 12))
music_listbox.pack(pady=5)

for roots, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        music_listbox.insert('end', filename)

label_song = tk.Label(music_frame, text='', bg="#2a2a2a", fg="yellow", font=("Arial", 12, "bold"))
label_song.pack(pady=5)

controls_frame = tk.Frame(music_frame, bg="#2a2a2a")
controls_frame.pack()

prev_btn = tk.Button(controls_frame, image=prev_img, bg="#2a2a2a", borderwidth=0, command=play_prev)
prev_btn.pack(side='left', padx=5)
stop_btn = tk.Button(controls_frame, image=stop_img, bg="#2a2a2a", borderwidth=0, command=stop)
stop_btn.pack(side='left', padx=5)
play_btn = tk.Button(controls_frame, image=play_img, bg="#2a2a2a", borderwidth=0, command=select)
play_btn.pack(side='left', padx=5)
pause_btn = tk.Button(controls_frame, image=pause_img, bg="#2a2a2a", borderwidth=0, command=pause, text="pause")
pause_btn.pack(side='left', padx=5)
next_btn = tk.Button(controls_frame, image=next_img, bg="#2a2a2a", borderwidth=0, command=play_next)
next_btn.pack(side='left', padx=5)

# --- Quote of the Day Bottom ---
with open("quotes.txt", "r") as q:
    quotes = q.readlines()
with open("authors.txt", "r") as a:
    authors = a.readlines()

rand_index = random.randint(0, len(quotes)-1)
quote_label = tk.Label(root, text=f'"{quotes[rand_index].strip()}"\n- {authors[rand_index].strip()}', font=("Arial", 14), bg="#1c1c1c", fg="cyan", wraplength=900, justify="center")
quote_label.place(relx=0.5, rely=0.9, anchor='center')

# --- Weather Top Right ---
def GetWeather(event=None):
    location = textfield.get()
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

        final_info = f"{condition}\n{temp}°C"
        final_data = f"Max: {max_temp}°C\nMin: {min_temp}°C\nPressure: {pressure}\nHumidity: {humidity}\nSunrise: {sunrise}\nSunset: {sunset}\nWind: {wind_speed}"
        weather_label.config(text=final_info)
        weather_details_label.config(text=final_data)
    except Exception as e:
        weather_label.config(text="Weather error")
        weather_details_label.config(text=str(e))

weather_frame = tk.Frame(root, bg="#2a2a2a", bd=2, relief="ridge")
weather_frame.place(x=770, y=10, width=240, height=300)

textfield = tk.Entry(weather_frame, justify="center", font=("Arial", 14))
textfield.pack(pady=5)
textfield.bind('<Return>', GetWeather)

weather_label = tk.Label(weather_frame, font=("Arial", 18, "bold"), bg="#2a2a2a", fg="white")
weather_label.pack(pady=5)
weather_details_label = tk.Label(weather_frame, font=("Arial", 12), bg="#2a2a2a", fg="white", justify="left")
weather_details_label.pack(pady=5)

root.mainloop()
