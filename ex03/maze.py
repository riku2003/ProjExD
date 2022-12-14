import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
from random import randint

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    if key == "Up": my -= 1
    elif key == "Down": my += 1
    elif key == "Right": mx += 1
    elif key == "Left": mx -= 1
    if maze_lst[mx][my] == 1: # 移動先が壁なら
        if key == "Up":
            my += 1
            tkm.showwarning("enterで終了","そこ壁だから")
        elif key == "Down":
            my -= 1
            tkm.showinfo("enterで終了","そこ壁だから")
        elif key == "Right":
            mx -= 1
            tkm.showerror("enterで終了","そこ壁だから")
        elif key == "Left":
            mx += 1
            tkm.askquestion("enterで終了","そこ壁だから")
    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)

if __name__=="__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15, 9)
    # print(maze_lst)
    mm.show_maze(canvas, maze_lst)
    
    tori = tk.PhotoImage(file= f"fig/{randint(0,9)}.png") # 実行する毎にこうかとんの画像がlstからランダムに選ばれる
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag="kokaton")
    key = ""        
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()