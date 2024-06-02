from tkinter import *
App=Tk()
App.title('length con')
App.geometry('400x200')
App['background']='cyan'
menu_ch=StringVar()
options={'Inches','Metres','Foot'}
menu=OptionMenu(App,menu_ch,*options)
menu.grid(row=0,column=0,padx=15,pady=5)
lbl=Label(App,text=' convert to ')
lbl.grid(row=0,column=1,padx=15,pady=5)
menu_ch2=StringVar()
menu2=OptionMenu(App,menu_ch2,*options)
menu2.grid(row=0,column=2,padx=15,pady=5)
lbl2=Label(App,text='Enter the number')
lbl2.grid(row=2,column=0,columnspan=2,padx=15,pady=5)
val=Entry(App,width=10)
val.grid(row=2,column=2,padx=15,pady=5)
def con():
    val1=menu_ch.get()
    val2=menu_ch2.get()
    num=int(val.get())
    if val1=='Metres' and val2=='Inches':
        convertednum=num*39.37
    elif val1=='Inches' and val2=='Metres':
        convertednum=num/39.37
    elif val1=='Metres' and val2=='Foot':
        convertednum=num*3.28
    elif val1=='Foot' and val2=='Metres':
        convertednum=num/3.28
    elif val1=='Metres' and val2=='Inches':
        convertednum=num*3.28*12
    elif val1=='Inches' and val2=='Metres':
        convertednum=num/(3.28*12)
    elif val1=='Foot' and val2=='Inches':
        convertednum=num*12
    elif val1=='Inches' and val2=='Foot':
        convertednum=num/12
    else:
        convertednum=num
    display=Label(App,text=round(convertednum,2))
    display.grid(row=2,column=3,padx=15,pady=5)
B=Button(App,text='Convert',command=con)
B.grid(row=3,column=0,padx=15,pady=5)
App.mainloop()