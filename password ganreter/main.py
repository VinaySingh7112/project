
from tkinter import*
from tkinter import messagebox
from random import choice, randint,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    webside=webside_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        webside:{
            "email":email,
            "password":password,
        }
    }

    if len(webside)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fildas empty.")
    else:
        try:
            with open("data.jaon","r") as data_file:
                #Reading old data
                data=json.load(data_file)
                # update old data with new data

        except FileNotFoundError:
            with open("data.json","w")as data_file:
                json.dump(new_data,data_file,indent=4)
        else:        
            data.update(new_data)

            with open("data.jaon","w") as data_file:
                #saving update data
                json.dump(data,data_file,indent=4)
        finally:        
            webside_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD------------------------------- #
def find_password():
    webside=webside_entry.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        
        messagebox.showinfo(title="Error",message=f"No data file found.") 

    else:    
        if webside in data:
            email=data[webside]["email"]
            password=data[webside]["password"]
            messagebox.showinfo(title="webside",message=f"email:{email} \n password:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"No datails for {webside} exists.")



# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Password manager")
window.config(padx=50,pady=50)


canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)


#Label

webside_label=Label(text="webside:")
webside_label.grid(column=0,row=1)

email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

#Entry
webside_entry=Entry(width=32)
webside_entry.grid(row=1,column=1,columnspan=1)
webside_entry.focus()

email_entry=Entry(width=32)
email_entry.grid(row=2,column=1,columnspan=1)
email_entry.insert(0,"vinaysinghraksel@gmail.com",)

password_entry=Entry(width=32)
password_entry.grid(row=3,column=1,columnspan=1)


#Buttons
search_buttons=Button(text="search",width=14,command=find_password)
search_buttons.grid(row=1,column=2)

generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)

add_button=Button(text="Add",width=27,command=save)
add_button.grid(row=4,column=1,columnspan=1)




window.mainloop()