import requests
from tkinter import *
# All of the funny dad jokes are from the icanHazdadjoke.com API

def getJoke():
    response = requests.get("https://icanhazdadjoke.com/", headers=
    {
        'Accept': 'application/json',
        'User-Agent': 'My Library (https://github.com/albert3rd/DadJokeGenerator)'
    })
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(joke, text=data['joke'])

root = Tk()
root.title("Dad Joke Generator: Ising icanhazdadjoke API")
root.config(padx=20, pady=25, bg="white")
#Canvas
canvas = Canvas(width=400, height=400)
canvas.config(bg="yellow", highlightthickness=0)
joke = canvas.create_text(200, 200, text="Press Button For a Awesome Dad Joke", font=("Georgia", 30), width=375)
canvas.grid(row=0, column=0, columnspan=3)
#Button
img = PhotoImage(file="DadButton.png")
img_Button = Button(image=img, highlightthickness=0, bg="white", command=getJoke)
img_Button.grid(row=1, column=1)

root.mainloop()

