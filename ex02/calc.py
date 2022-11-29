import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    i = btn["text"]
    if i == "=":
        keisan = entry.get()
        res = eval(keisan)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    else:
        entry.insert(tk.END,i)

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root,justify="right",width=10,font=("",40))
entry.grid(row=0,column=0,columnspan=3)

#練習2
#button = tk.Button(root,text="9",width=4,height=2,font=("",30)).pack()
#button = tk.Button(root,text="8",width=4,height=2,font=("",30)).pack()
#button = tk.Button(root,text="7",width=4,height=2,font=("",30)).pack()
#button = tk.Button(root,text="6",width=4,height=2,font=("",30)).pack()
#button = tk.Button(root,text="5",width=4,height=2,font=("",30)).pack()
#button = tk.Button(root,text="4",width=4,height=2,font=("",30)).pack()
#button = tk.Button(root,text="3",width=4,height=2,font=("",30)).pack()
#button = tk.Button(root,text="2",width=4,height=2,font=("",30)).pack()
#button = tk.Button(root,text="1",width=4,height=2,font=("",30)).pack()
#button = tk.Button(root,text="0",width=4,height=2,font=("",30)).pack()

r, c = 1, 0
for i in range(9, -1, -1):
    button = tk.Button(root, text=f"{i}",width=4,height=2,font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

operators = ["+","="]
for ope in operators:
    button = tk.Button(root, text=f"{ope}",width=4,height=2,font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

root.mainloop()