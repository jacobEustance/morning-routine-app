import tkinter as tk
import requests
import time

def GetWeather(canvas):
    location = textfield.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q=Holmfirth&appid=2abb1ec02008546569362504212b0b21"
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
    label1.config(text = final_info)
    label2.config(text = final_data)



canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather app")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, justify= "center", font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', GetWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()
