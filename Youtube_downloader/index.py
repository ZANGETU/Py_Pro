import youtube_dl
import tkinter
from tkinter import messagebox

# 画面作成
tkk = tkinter.Tk()
tkk.geometry('400x300')
tkk.title('YouTube動画保存ツール')

def hozon(url):
    try:
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("成功", "保存が成功しました")
    except:
        messagebox.showinfo("失敗", "保存できませんでした")

# ボタン作成
btn_down = tkinter.Button(tkk, text='ダウンロード', command=lambda:hozon(txt_box.get()))
btn_down.place(x=170, y=210)

# テキストボックス作成
txt_box = tkinter.Entry(width=40)
txt_box.place(x=85, y=180)

tkk.mainloop()