from tkinter import*
import pandas
import random
BACKGROUND_COLOR="#B1DDC6"


data=pandas.read_csv("data.csv")
to_learn=data.to_dict(orient="records")
currect_card={}

def next_card():
    global currect_card,flip_timer
    window.after_cancel(flip_timer)
    currect_card=random.choice(to_learn)
    canvas.itemconfig(cord_title,text="English",fill="black")
    canvas.itemconfig(cord_word,text=currect_card["English"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer=window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(cord_title,text="Hindi",fill="white")
    canvas.itemconfig(cord_word,text=currect_card["Hindi"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)

def is_known():
    to_learn.remove(currect_card)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)
    next_card()

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)
card_front_img=PhotoImage(file="card_front.png")
card_back_img=PhotoImage(file="card_back.png")
card_background=canvas.create_image(400,263,image=card_front_img)
cord_title=canvas.create_text(400,150, text="",font=("Ariel",40,"italic"))
cord_word=canvas.create_text(400,263, text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


cross_image=PhotoImage(file="wrong.png")
unkonwn_button=Button(image=cross_image,highlightthickness=0,command=next_card)
unkonwn_button.grid(row=1,column=0)


check_image=PhotoImage(file="right.png")
konwn_button=Button(image=check_image,highlightthickness=0,command=is_known)
konwn_button.grid(row=1,column=1)

next_card()
window.mainloop()