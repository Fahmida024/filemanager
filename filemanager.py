from tkinter import*
import tkinter.font as font
from tkinter.filedialog import*
gui=Tk()
gui. geometry('500x500')
gui.title('File manager')


def openfile():
    f=askopenfile(title='open file')
    list.delete(0,END)
    items=f.readlines()
    print(items)

    for i in items:
        list.insert(END,i)

def add():
    x=entrybox.get()
    list.insert(END,x)

def delete():
    index=list.curselection()
    list.delete(index)
    
def save():
    s=asksaveasfile(defaultextension='.txt')
    for i in list.get(0,END):
        print(i,file=s)
    list.delete(0,END)




savebutton=Button(gui,text='Save', command=save)
entrybox=Entry(gui)
addbutton=Button(gui, text='Add', command=add)
openbutton=Button(gui, text='Open', command=openfile)
deletebutton=Button(gui, text='Delete', command=delete)


frame=Frame(gui)
scrollbar=Scrollbar(frame,orient='vertical')
list=Listbox(frame, width=20, bg='gray',yscrollcommand=scrollbar.set)
frame.place(x=200, y=100)
list.pack(side=LEFT)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=list.yview)


list.insert(END,'List1')
for i in range(100):
    list.insert(END,'List'+str(i))


savebutton.place(x=250, y=20)
entrybox.place(x=200, y=60)
addbutton.place(x=150, y=60)
openbutton.place(x=350, y=60)
deletebutton.place(x=250, y=360)



gui.mainloop()
