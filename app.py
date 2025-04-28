import requests
import time
import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import ttk

load_dotenv()

def get_weather(city_name):
    api_key = os.getenv('API_KEY')
    if not api_key:
        print("API Key not found.")
        return None

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=en"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        sys = data['sys']
        
        return {
            'city': data['name'],
            'country': sys['country'],
            'temp': main['temp'],
            'feels_like': main['feels_like'],
            'description': weather['description'],
            'humidity': main['humidity'],
            'wind_speed': wind['speed']
        }
    else:
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

def display_weather(weather):
    for widget in result_frame.winfo_children():
        widget.destroy()

    city_label = ttk.Label(result_frame, text=f"City: {weather['city']}, {weather['country']}", font=("Helvetica", 14), anchor="w")
    city_label.pack(pady=5, anchor="w")

    temp_label = ttk.Label(result_frame, text=f"Temperature: {weather['temp']}°C", font=("Helvetica", 12), anchor="w")
    temp_label.pack(pady=3, anchor="w")

    feels_like_label = ttk.Label(result_frame, text=f"Feels Like: {weather['feels_like']}°C", font=("Helvetica", 12), anchor="w")
    feels_like_label.pack(pady=3, anchor="w")

    description_label = ttk.Label(result_frame, text=f"Condition: {weather['description'].capitalize()}", font=("Helvetica", 12), anchor="w")
    description_label.pack(pady=3, anchor="w")

    humidity_label = ttk.Label(result_frame, text=f"Humidity: {weather['humidity']}%", font=("Helvetica", 12), anchor="w")
    humidity_label.pack(pady=3, anchor="w")

    wind_speed_label = ttk.Label(result_frame, text=f"Wind Speed: {weather['wind_speed']} m/s", font=("Helvetica", 12), anchor="w")
    wind_speed_label.pack(pady=3, anchor="w")

def fetch_weather():
    city_name = city_entry.get()
    if city_name:
        weather = get_weather(city_name)
        if weather:
            display_weather(weather)
        else:
            error_label = ttk.Label(result_frame, text="Failed to retrieve weather data.", font=("Helvetica", 12, "italic"), foreground="red")
            error_label.pack(pady=10)
    else:
        error_label = ttk.Label(result_frame, text="Please enter a city name.", font=("Helvetica", 12, "italic"), foreground="red")
        error_label.pack(pady=10)

root = tk.Tk()
root.title("Weather App")
root.geometry("800x500")
root.config(bg="#f0f0f0")

frame = ttk.Frame(root, padding="20")
frame.pack(fill="both", expand=True)

title_label = ttk.Label(frame, text="Weather App", font=("Helvetica", 24, "bold"), foreground="#4B9CD3")
title_label.pack(pady=10)

city_label = ttk.Label(frame, text="Enter City:", font=("Helvetica", 12))
city_label.pack(pady=5)
city_entry = ttk.Entry(frame, font=("Helvetica", 14), width=25)
city_entry.pack(pady=10)

style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 12),
                padding=6,
                relief="flat",
                background="#4B9CD3",
                foreground="black")

search_button = ttk.Button(frame, text="Get Weather", command=fetch_weather, style="TButton")
search_button.pack(pady=10)

result_frame = ttk.Frame(frame)
result_frame.pack(pady=20, fill="both", expand=True)

root.mainloop()
