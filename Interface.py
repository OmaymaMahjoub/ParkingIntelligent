from tkinter import * 

homePage = Tk()
homePage['bg']='gray'

#Etage Name
label = Label(homePage, text="E1", bg="gray", fg="SlateBlue4")
label.config(font=("Roman bold", 30))
label.grid(row=0, column=3)

#cars
reserve1 = PhotoImage(file = r".\images\BCarDown.png")
reserve2 = PhotoImage(file = r".\images\BCarUp.png")
libre1= PhotoImage(file = r".\images\GCarDown.png")
libre2= PhotoImage(file = r".\images\GCarUp.png")
occupe1= PhotoImage(file = r".\images\RCarDown.png")
occupe2= PhotoImage(file = r".\images\RCarUp.png")

#Car button exeample row1
button1=Button(homePage, text = "Button", image = reserve1, bg='gray')
button1.grid(row=1,column=0)
button2=Button(homePage, text = "Button", image = reserve1, bg='gray')
button2.grid(row=1,column=1)
button3=Button(homePage, text = "Button", image = libre1, bg='gray')
button3.grid(row=1,column=2)
button4=Button(homePage, text = "Button", image = occupe1, bg='gray')
button4.grid(row=1,column=3)

#Car button exeample row1
button11=Button(homePage, text = "Button", image = reserve2, bg='gray')
button11.grid(row=3,column=0)
button22=Button(homePage, text = "Button", image = reserve2, bg='gray')
button22.grid(row=3,column=1)
button33=Button(homePage, text = "Button", image = libre2, bg='gray')
button33.grid(row=3,column=2)
button44=Button(homePage, text = "Button", image = occupe2, bg='gray')
button44.grid(row=3,column=3)

homePage.mainloop()
