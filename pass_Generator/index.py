import random
import pyperclip
import webbrowser
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
 
#entryの値を削除
def low():
    text_box.delete(0, END)
 
    #パスワードの長さを取得する
    length = var1.get()
    komoji = "abcdefghijklmnopqrstuvwxyz"
    oomoji = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    suuji = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
 
    #もし選択したのがlowerだっだら
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(komoji)
        return password
 
    #もし選択したのがupperだったら
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(oomoji)
        return password
 
    #もし選択したのがdigitsだったら
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(suuji)
        return password
 
# パスワード作成
def generate():
    password1 = low()
    text_box.insert(10, password1)

#テキストボックス表示された値をコピーする
def copy_text():
    random_password = text_box.get()
    messagebox.showinfo("成功", "コピーしました")
    pyperclip.copy(random_password)

#ファイルへの書き込み
def write_text():
    input_txt = text_box.get()
    messagebox.showinfo("成功", "書き込みました")
    with open("passcode.txt", mode='w') as f: 
        f.write(input_txt) 
    return 0

#ブラウザ開く
def backnet(url):
    webbrowser.open_new(url)   
 
#ウィンドウ作成など
root = Tk()
var = IntVar()
var1 = IntVar()
 
#タイトルとウィンドウサイズ
root.title("パスワードジェネレーター的なやつ")
root.geometry("400x300")
root.resizable(0,0)

#アイコン表示
iconimg = 'img\icon001.ico'
root.iconbitmap(default=iconimg)
 
#ラベル表示
Random_password = Label(root, text="パスワード")
Random_password.place(x = 90, y = 80)
mojisuu_label = Label(root, text="文字数")
mojisuu_label.place(x = 90, y = 105)
op_label = Label(root, text="オプション")
op_label.place(x = 90, y = 130)
title_label = Label(root, text="パスワードジェネレーター的なやつ", font=("MSゴシック", "15", "bold"))
title_label.place(x = 35, y = 30)
link_label = Label(root, text="参考", foreground='#0000FF')
link_label.place(x = 355, y = 275)
#ラベルにリンクを指定する
link_label.bind("<Button-1>", lambda e: backnet("https://www.geeksforgeeks.org/python-random-password-generator-using-tkinter/"))

#テキストボックス作成
text_box = Entry(root)
text_box.place(x = 140, y = 80, width=130, height=20)

#作成ボタンを作成する
generate_button = Button(root, text="作成", command=generate)
generate_button.place(x = 140, y = 200, width=130, height=30)

#コピーボタンを作成する
copy_button = Button(root, text="コピー", command=copy_text)
copy_button.place(x = 140, y = 230, width=130, height=30)

#書き出しボタンを作成する
write_button = Button(root, text="書き出し", command=write_text)
write_button.place(x = 140, y = 260, width=130, height=30)
 
#ラジオボタンの配置
radio_low = Radiobutton(root, text="小文字のみ", variable=var, value=1)
radio_low.place(x = 140, y = 130)
radio_middle = Radiobutton(root, text="大文字・小文字", variable=var, value=0)
radio_middle.place(x = 140, y = 150)
radio_strong = Radiobutton(root, text="大文字・小文字・数字", variable=var, value=3)
radio_strong.place(x = 140, y = 170)

#Comboboxを置き読み取り専用に設定する
combo = Combobox(root, state="readonly", textvariable=var1)
 
#パスワードの長さを指定する
combo['values'] = (4, 6, 8, 10, 12, 14, 16,
                   18, 20, 22, 24,
                   26, 28, 30)  #"Length"
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.place(x = 140, y = 105, width=130, height=20)

root.mainloop()
