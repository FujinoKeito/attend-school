from tkinter import *
from tkinter import ttk
import datetime

#現在時刻取得.
dt_now = datetime.datetime.now()
now = dt_now.time()
#比較時刻.
AM = datetime.time(6, 0, 0)
PM = datetime.time(12, 10, 0)
END = datetime.time(14, 50, 0)

root = Tk()
root.title("自動登校登録")#タイトル.

if(AM <= now <PM):#午前登録.
    label_1 = ttk.Label(root,text ='登校登録をします')
elif(PM <= now <END):#午後登録.
    label_1 = ttk.Label(root,text ='中間登録をします')
elif(END <= now):#下校登録.
    label_1 = ttk.Label(root,text ='下校登録をします')
else:#時間外
    label_1 = ttk.Label(root,text ='時間外です')

button_1 = ttk.Button(root,text = 'OK',command=lambda:())

#レイアウト
label_1.pack()
button_1.pack()

##ウィンドウの表示.
root.mainloop()