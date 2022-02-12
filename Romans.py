### This program is able to determine the Roman ###
### numerals for numbers from 1 to 3999 inclusive. ###

from tkinter import *

def under100(num):
    test = str(num)
    base = {"1":"I", "2": "II", "3": "III", "4": "IV", "5": "V", "6": "VI", "7": "VII", "8": "VIII", "9": "IX"}
    digits = [x for x in test]
    length = len(digits)
    if length == 1:
        return(base[test])
    elif length == 2:
        if int(digits[0]) > 4 and int(digits[0]) < 9:
            try:
                return("L" + (int(digits[0])-5)*"X" + base[digits[1]])
            except:
                return("L" + (int(digits[0])-5)*"X")
        elif int(digits[0]) <= 3:
            try:
                return(int(digits[0])*"X" + base[digits[1]])
            except:
                return(int(digits[0])*"X")
        elif int(digits[0]) == 4:
            try:
                return("XL" + base[digits[1]])
            except:
                return("XL")
        elif int(digits[0]) == 9:
            try:
                return("XC" + base[digits[1]])
            except:
                return("XC")


def over100(num):
    test = str(num)
    digits = [test[0], test[1::]]
    if int(digits[0]) < 4:
        return("C"*(int(digits[0])) + under100(digits[1]))
    elif int(digits[0]) == 4:
        return("CD" + under100(digits[1]))
    elif int(digits[0]) > 4 and int(digits[0]) < 9:
        return("D" + "C"*(int(digits[0])-5) + under100(digits[1]))
    else:
        return("CM" + under100(digits[1]))

def thous(num):
    test = str(num)
    digits = [test[0], test[1::]]
    if int(digits[0]) < 4:
        return("M"*(int(digits[0])) + over100(digits[1]))
    else:
        return("Nope, badness 10000 on the input")

def calc(num):
    try:
        if len(str(num)) == 1 or len(str(num)) == 2:
            return(under100(num))
        elif len(str(num)) == 3:
            return(over100(num))
        elif len(str(num)) == 4:
            return(thous(num))
        else:
            return("Nope, badness 10000 on the input")
    except:
        return("Nope, badness 10000 on the input")

######################    GUI    ######################

class app(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.detail = Label(self, text = "Numbers to Roman Numerals", borderwidth=0, relief = "solid", padx = 3, width=28) # Title
        self.detail.grid(row = 0, column = 0, columnspan = 2, sticky = W, padx = 3, pady = 30)
        self.detail.config(font=("Arial", 20))

        self.instruction = Label(self, text = "Enter a number between 1 & 3999 inclusive") # Input instruction
        self.instruction.grid(row = 1, column = 0, columnspan = 2, sticky = W, padx = 2)
        self.instruction.config(font=("Arial", 12))
        
        self.input = Entry(self) # Input box
        self.input.grid(row = 2, column = 0, sticky = W, padx=3, pady=5)
        self.input.config(font=("Arial", 20))

        self.instruction = Label(self, text = "") # Adding some blank space
        self.instruction.grid(row = 3, column = 0, columnspan = 2, sticky = W, padx = 3)
        self.instruction.config(font=("Arial", 12))

        self.instruction = Label(self, text = "Output:") # Label for output area
        self.instruction.grid(row = 4, column = 0, columnspan = 2, sticky = W, padx = 3)
        self.instruction.config(font=("Arial", 12))
        
        self.submit_button = Button(self, text = "Convert", command = self.run, padx = 0) # Convert button
        self.submit_button.grid(row = 2, column = 1, sticky = W)
        self.submit_button.config(font=("Arial", 15))
        
        self.text = Text(self, width = 25, height = 1, wrap = WORD) # Output area
        self.text.grid(row = 5, column = 0, columnspan = 2, sticky = W, padx = 3)
        self.text.config(font=("Georgia", 20))
        self.text.configure(state="disabled")
        
    def run(self): # Run the conversion to Roman numerals
        self.text.configure(state="normal")
        self.text.delete(0.0, END) # Remove previous output
        self.text.insert(0.0, calc(self.input.get())) # Display new output
        self.text.configure(state="disabled")

# Interface setup
root = Tk()
root.title("Roman Numberal Converter")
root.geometry("450x290")
app = app(root)
root.mainloop()


for i in range(1,100):
    out = under100(i)
    print(str(i) + " is " + out + " becomes ", end = "")
    for x in out:
        if x == "I":
            print("harder", end = " ")
        elif x == "V":
            print ("daddy", end = " ")
        elif x == "X":
            print("please", end = " ")
        elif x == "L":
            print("", end = " ")
        elif x == "C":
            print("", end = " ")
        else:
            print(x)
    print("")
