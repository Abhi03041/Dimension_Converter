from tkinter import*

def convert():
    METER = meterdimension.get()
    FEET=feetdimension.get()
    if Dimension_bit.get()==1:
        feet= (int)(METER/0.3048)
        inch= METER/0.3048
        inch=(inch-feet)*12
        print (feet)
        print(inch)
        feetdimension.set(feet)
        inchdimension.set(inch)
    elif Dimension_bit.get()==2:
        feet= (int)(METER*0.3048)
        inch= METER*0.3048
        inch=(inch-feet)*100
        print (feet)
        print(inch)
        feetdimension.set(feet)
        inchdimension.set(inch)

def reset():
    top = Toplevel(padx=50, pady=50)
    top.grid()
    message = Label(top, text = "Reset Complete")
    button = Button(top, text="OK", command=top.destroy)

    message.grid(row = 0, padx = 5, pady = 5)
    button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)

    feetdimension.set(int(0))
    meterdimension.set(int(0))
    inchdimension.set(int(0))
    cmdimension.set(int(0))

def swapped():
    d=Dimension_bit.get()
    if d==1:
        titleLabel['text']='Feet to Meter Dimension'
        meterLabel['text']='Enter Feets: '
        tLabel['text']='ft'
        feetLabel['text']='Meter Result:'
        inchLabel['text']='Remaining in cm result: '
        feet1Label['text']='m'
        inch1Label['text']='cm'
        Dimension_bit.set(2)
    else:
        titleLabel['text']='Meter to Feet Dimension'
        meterLabel['text']='Enter Meter: '
        tLabel['text']='m'
        feetLabel['text']='Feet Result:'
        inchLabel['text']='Remaining in inch result: '
        feet1Label['text']='ft'
        inch1Label['text']='"'
        Dimension_bit.set(1)
    meterdimension.set(0)
    feetdimension.set(0)
    inchdimension.set(0)
    cmdimension.set(0)

home=Tk()  #figure home
home.title("Dimension_Converter")
meterframe=Frame(home)
meterframe.grid()

Dimension_bit=IntVar()
Dimension_bit.set(1)

meterdimension=IntVar()
meterdimension.set(0)
feetdimension=IntVar()
feetdimension.set(0)
inchdimension=IntVar()
inchdimension.set(0)
cmdimension=IntVar()
cmdimension.set(0)

titleLabel = Label (meterframe, text = 'Meter to Feet Dimension', font = ("Arial", 20, "bold"), justify = CENTER)
titleLabel.grid(row = 1, column = 1, columnspan = 3, pady = 10, padx = 20)

meterLabel = Label (meterframe, text = " Enter Meters: ", font = ("Arial", 16), fg = "red")
meterLabel.grid(row = 2, column = 1, pady = 10, sticky = NW)

meterEntry = Entry (meterframe, width = 15, bd = 5, textvariable = meterdimension)
meterEntry.grid(row = 3, column = 1, pady = 10, sticky = NW,padx=10)
        
tLabel = Label (meterframe, text = 'm', font = ("Arial", 15, "bold"), justify = CENTER)
tLabel.grid(row = 3, column = 1)

convertButton =Button (meterframe, text = "Convert", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = convert)
convertButton.grid(row = 4, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 10)

resetButton = Button (meterframe, text = "Reset", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = reset)
resetButton.grid(row = 4, column = 2,ipady = 8, ipadx = 12, pady = 5,padx=10, sticky = NW)

swapButton =Button (meterframe, text = "Swap", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, overrelief = GROOVE, activebackground = "green", activeforeground="blue", command =swapped)
swapButton.grid(row = 5, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 10)

feetLabel = Label (meterframe, text = "Feet result: ", font = ("Arial", 16), fg = "blue")
feetLabel.grid(row = 6, column = 1, pady = 10, sticky = NW)

feetEntry = Entry (meterframe, width = 15, bd = 5, textvariable = feetdimension)
feetEntry.grid(row = 7, column = 1, pady = 10, sticky = NW, padx = 10 )

feet1Label = Label (meterframe, text = 'ft', font = ("Arial", 15, "bold"), justify = RIGHT)
feet1Label.grid(row = 7, column = 1)

inchLabel = Label (meterframe, text = "Remaining in inch result: ", font = ("Arial", 16), fg = "blue")
inchLabel.grid(row = 8, column = 1, pady = 10,sticky = NW)

inchEntry = Entry (meterframe, width = 15, bd = 5, textvariable = inchdimension)
inchEntry.grid(row = 9, column = 1, pady = 10, sticky = NW, padx = 10 )

inch1Label = Label (meterframe, text = '"', font = ("Arial", 15, "bold"), justify = RIGHT)
inch1Label.grid(row = 9, column = 1)
        
home.mainloop()


