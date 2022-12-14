import tkinter as tk
import tkinter.messagebox as tkm
import math 

def button_click(event):
    btn = event.widget
    i = btn["text"]
    if i == "=":
        keisan = entry.get() # 数式の文字列
        res = eval(keisan) # 数式文字列の評価
        entry.delete(0,tk.END) # 表示文字列の削除
        entry.insert(tk.END,res) # 結果の挿入

    elif i == "C": #クリアの設定
        entry.delete(0,tk.END) 
    
    else:
        entry.insert(tk.END,i)
        
root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root,justify="right",width=10,font=("",40))
entry.grid(row=0,column=0,columnspan=3)
entry.delete(tk.END,0)

r, c = 1, 0
for i in range(9, -1, -1): #数字キーのボタン設定
    button = tk.Button(root, text=f"{i}",width=4,height=2,font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

operators = ["+","×","÷","=","C"] #+,=,Cのボタン設定
for ope in operators:
    button = tk.Button(root, text=f"{ope}",width=4,height=2,font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

root.mainloop()