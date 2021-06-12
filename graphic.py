
import tkinter as tk
from tkinter import font
import requests 

W = 500
H = 500
cblue = "#39B7CD"

def test(location):
    print(f"the location is: {location}")

def format_resp(weather):
    try: 
        name = str(weather["name"])
        des = str(weather["weather"][0]["description"])
        weather = str(weather["main"]["temp"])

        final_string = ("City: {}\nDescription: {}\nTemp: {}".format(name, des, weather))

    except: 
        final_string = "There was a problem retrieving your data"
    
    return final_string

def get_weather(location):
    wkey = "135543aaed11ed43e8352e2886ae8705"
    url = "http://api.openweathermap.org/data/2.5/weather"
    par = {"q": location, "appid": wkey, "units": "metric"}
    
    response = requests.get(url, params = par)
    weather= response.json()

    weatheroutput["text"] = format_resp(weather)

window = tk.Tk()
window.title("Weather App")

canvas = tk.Canvas(window, width = W, height = H)
canvas.pack()

back = tk.PhotoImage(file = "back.png")
background = tk.Label(canvas, image = back)
background.place(relwidth = 1, relheight = 1)

searchframe = tk.Frame(canvas, bg = 'black', bd = 5)   
searchframe.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.1)

location = tk.Entry(searchframe, bg = 'white', font = 'Verdana')
location.place(relwidth=0.6, relheight=0.97)

searchbutton = tk.Button(searchframe, text = "Get Weather", bg = cblue, font = 'verdana', command = lambda: get_weather(location.get()))
searchbutton.place(relx=0.61, relwidth = 0.39, relheight = 0.97)

outframe = tk.Frame(canvas, bg = 'black', bd = 5)
outframe.place(relx = 0.1, rely = 0.22, relwidth = 0.8, relheight = 0.6) 

weatheroutput = tk.Label(outframe, bg = 'white', font = ('Verdana', 12), anchor = 'nw', justify = 'left')
weatheroutput.place(relwidth = 1, relheight = 1)

print(tk.font.families())

window.mainloop()