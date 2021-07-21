#Digital Clock GUI

#import the Tkinter module for creating our GUI
from tkinter import *
from tkinter.ttk import *


#Import strftime from time to extract our current system time as a string
from time import strftime

root = Tk()
root.title('DigiClock')

def time():
    current_time = strftime('%H : %M : %S %p')
    label.config(text = current_time)
    label.after(1000,time)   #Time function is called after 1000 ms or 1 s to change the label, i.e., the time displayed of our clock 

#Customise the label to make the GUI look more beautiful
label = Label(root, font = ('arial',40,'bold'),background='black',foreground='white')

#Pack the label into our root to be displayed
label.pack()

#Call the time function to customise our label widget
time()

#Run the mainloop so that the clock keeps on running, i.e., the GUI keeps on running, without stopping abruptly
mainloop()
