import datetime 
import tkinter as tk 
from PIL import Image, ImageTk 

# window 
window = tk.Tk() 
window.geometry("620x780") 
window.title("Age Calculator App") 

# labels 
nlabel = tk.Label(text="Name") 
nlabel.grid(column=0, row=1) 
ylabel = tk.Label(text="Year")
ylabel.grid(column=0, row=2) 
mlabel = tk.Label(text="Month") 
mlabel.grid(column=0, row=3) 
dlabel = tk.Label(text="Day") 
dlabel.grid(column=0, row=4) 

# entry_fields 
nentry = tk.Entry() 
nentry.grid(column=1, row=1) 
yentry = tk.Entry() 
yentry.grid(column=1, row=2) 
mentry = tk.Entry() 
mentry.grid(column=1, row=3) 
dentry = tk.Entry() 
dentry.grid(column=1, row=4) 

class Person:
    def __init__(self, name, birthdate): 
        self.name = name 
        self.birthdate = birthdate 
        
    def age(self): 
        today = datetime.date.today() 
        age = today.year - self.birthdate.year 
        return age

def calculate_age(): 
    name = nentry.get() 
    birthdate = datetime.date(int(yentry.get()), int(mentry.get()), int(dentry.get()))
    person = Person(name, birthdate)
    
    # text
    texter = tk.Text(master=window, height=10, width=25) 
    texter.grid(column=1, row=6) 
    answer = "Hey, {name}! You are {age} years old.".format(name=name, age=person.age()) 
    texter.insert(tk.END, answer) 

# button 
button = tk.Button(window, text="Calculate Age", command=calculate_age, bg="pink") 
button.grid(column=1, row=5) 

# image 
image = Image.open('app_image.jpeg') 
image.thumbnail((300, 300), Image.LANCZOS) 
photo = ImageTk.PhotoImage(image) 
label_image = tk.Label(image=photo) 
label_image.grid(column=1, row=0) 

window.mainloop()
