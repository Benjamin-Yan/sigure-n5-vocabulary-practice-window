# -*- coding: utf-8 -*-
"""
日文單字練習系統 GUI 程式
"""
import pandas as pd
from tkinter import *
from tkinter import messagebox
import random

# 資料庫來源 (N5共有21課)
source4 = pd.read_html("https://www.sigure.tw/learn-japanese/vocabulary/n5/04-noun-job.php")  # 第四課資料
sel4 = source4[0] #18個單字
kan_list4 = list(sel4.loc[0: 16, "日文"]) + list(sel4.loc[17: , "假名"])
jap_list4 = list(sel4.loc[0: 16, "假名"]) + list(sel4.loc[17: , "日文"])
chi_list4 = list(sel4.loc[0: , "中文"])
data4 = list()

source5 = pd.read_html('https://www.sigure.tw/learn-japanese/vocabulary/n5/05-noun-place.php')  # 第五課資料
sel5 = source5[0] #49個單字
kan_list5 = list(sel5.loc[0: 41, "日文"]) + list(sel5.loc[42: , "假名"])
jap_list5 = list(sel5.loc[0: 41, "假名"]) + list(sel5.loc[42: , "日文"])
chi_list5 = list(sel5.loc[0: , "中文"])
data5 = list()

kans = kan_list4 + kan_list5
# 分課資料用
for i in range(49):
    data5.append(jap_list5[i] + " (" + kan_list5[i] + ")")
for i in range(18):
    data4.append(jap_list4[i] + " (" + kan_list4[i] + ")")

# 考試字典(分課,對答案)
dic4 = dict(zip(jap_list4, chi_list4))
dic5 = dict(zip(jap_list5, chi_list5))

# search ()
def search():
    def q():
        chi = enty1.get()
        jap = enty2.get()
        if (jap != "") and (chi != ""):
            texy3.configure(state='normal')
            texy3.delete(1.0,"end")
            texy3.insert(1.0, '請一次輸入一種語言!!', 'tag_1')
            texy3.configure(state='disabled')
        elif (jap == "") and (chi == ""):
            texy3.configure(state='normal')
            texy3.delete(1.0,"end")
            texy3.insert(1.0, '請輸入中文或日文!!', 'tag_1')
            texy3.configure(state='disabled')
        elif (jap != "") and (chi == ""):            #查中文意思
            z = 0
            if jap in jap_list4:
                ind = jap_list4.index(jap)
                c = chi_list4[ind]
                texy3.configure(state='normal')
                texy3.delete(1.0,"end")
                texy3.insert(1.0, jap +'  的中文意思是 : ' + c, 'tag_1')
                texy3.configure(state='disabled')
            elif jap in jap_list5:
                ind = jap_list5.index(jap)
                c = chi_list5[ind]
                texy3.configure(state='normal')
                texy3.delete(1.0,"end")
                texy3.insert(1.0, jap +'  的中文意思是 : ' + c, 'tag_1')
                texy3.configure(state='disabled')
            else:
                texy3.configure(state='normal')
                texy3.delete(1.0,"end")
                for i in jap_list4:
                    if jap in i:
                        z += 1
                        if z == 1:
                            texy3.insert(END, '可能的日文單字有 : ', 'tag_1')
                        texy3.insert(END, i + ", ", 'tag_1')
                for i in jap_list5:
                    if jap in i:
                        z += 1
                        if z == 1:
                            texy3.insert(END, '可能的日文單字有 : ', 'tag_1')
                        texy3.insert(END, i + ", ", 'tag_1')
                if z == 0:
                    texy3.insert(END, '沒有符合的項目QQ', 'tag_1')
                texy3.configure(state='disabled')
        elif (jap == "") and (chi != ""):            #查日文單字
            z = 0
            if chi in chi_list4:
                ind = chi_list4.index(chi)
                j = jap_list4[ind]
                texy3.configure(state='normal')
                texy3.delete(1.0,"end")
                texy3.insert(1.0, chi +'  的日文單字是 : ' + j, 'tag_1')
                texy3.configure(state='disabled')
            elif chi in chi_list5:
                ind = chi_list5.index(chi)
                j = jap_list5[ind]
                texy3.configure(state='normal')
                texy3.delete(1.0,"end")
                texy3.insert(1.0, chi +'  的日文單字是 : ' + j, 'tag_1')
                texy3.configure(state='disabled')
            else:
                texy3.configure(state='normal')
                texy3.delete(1.0,"end")
                for i in chi_list4:
                    if chi in i:
                        z += 1
                        if z == 1:
                            texy3.insert(END, '可能的中文意思有 : ', 'tag_1')
                        texy3.insert(END, i + ", ", 'tag_1')
                for i in chi_list5:
                    if chi in i:
                        z += 1
                        if z == 1:
                            texy3.insert(END, '可能的中文意思有 : ', 'tag_1')
                        texy3.insert(END, i + ", ", 'tag_1')
                if z == 0:
                    texy3.insert(END, '沒有符合的項目QQ', 'tag_1')
                texy3.configure(state='disabled')
    
    fra3 = Frame(win, bg = "#e58947")
    fra3.pack()
    labe = Label(fra3, text = '單字查詢', fg = "#e0e094", width = 600, font = ('Arial', 25), bg = "#e58947")
    labe.pack(pady = 10)
    fray1 = Frame(fra3, bg = "#e58947", height=100)
    fray1.pack(padx = 5, side=TOP, fill = "x")
    fray1.propagate(0)
    laby1 = Label(fray1, text="中文  :", bg = "#e58947", font = 1)
    laby1.pack(padx = 10, side = LEFT)
    enty1 = Entry(fray1, font = 1)
    enty1.pack(padx = 10, side = LEFT)
    by1 = Button(fray1,text="查詢", width=10, command = q)
    by1.pack(padx = 10, side = LEFT)
    fray2 = Frame(fra3, bg = "#e58947", height=100, width = 300)
    fray2.pack(padx = 5, side=TOP, fill = "x")
    fray2.propagate(0)
    laby2 = Label(fray2, text="日文  :", bg = "#e58947", font = 1)
    laby2.pack(padx = 10, side = LEFT)
    enty2 = Entry(fray2, font = 1)
    enty2.pack(padx = 10, side = LEFT)
    by2 = Button(fray2,text="查詢", width=10, command = q)
    by2.pack(padx = 10, side = LEFT)
    texy3 = Text(fra3, fg = "#e0e094", bg = "#e58947", font = ('Arial', 15), wrap = 'word', state='disabled', exportselection = 0, relief = 'flat', cursor='arrow', width = 30, height = 9)
    texy3.pack()
    texy3.tag_config("tag_1", background="#e58947")# 設定 tag
    by3 = Button(fra3, text = '返回', bg = '#66FFE6', activebackground = '#66FFE6', width = 10, font = 1, command = lambda:fra3.destroy())
    by3.pack(side = "bottom")

ra = 0
wa = 0
# practice mode (OK)
def practice():
    # 考試字典(全部,出題)
    database = dict()
    database.update(dic4)
    database.update(dic5)
    fra2 = Frame(win, bg = "green", height = 500, width = 600)
    fra2.pack()
    fra2.propagate(0)  #固定大小不隨便變動
    def RZ():
        fra2.destroy()
        global ra,wa
        ra = 0
        wa = 0
    def pri():
        def answ():
            ans = entx.get()
            if ans == "":
                labx2.config(text = "請作答!!")
            else:
                global ra,wa
                if japp in dic4.keys():
                    ind = jap_list4.index(japp)
                    if ans == japp:
                        labx2.config(text = "Right!!\n\n(按下按鈕以繼續下一題)")
                        ra += 1
                    else:
                        labx2.config(text = "wrong! The ans is   "+ japp + " (" + kan_list4[ind] + ")" +"\n\n(按下按鈕以繼續下一題)")
                        wa += 1
                else:   #in dic5.keys()
                    ind = jap_list5.index(japp)
                    if ans == japp:
                        labx2.config(text = "Right!!\n\n(按下按鈕以繼續下一題)")
                        ra += 1
                    else:
                        labx2.config(text = "wrong! The ans is   "+ japp + " (" + kan_list5[ind] + ")" +"\n\n(按下按鈕以繼續下一題)")
                        wa += 1
                        
                if ra + wa == 10:
                    messagebox.showinfo("作答結果", "本次測驗共答對 "+ str(ra) +" 題,答錯 "+str(wa)+" 題\n勝率為 "+str(ra*10)+" %")
                    ra = 0
                    wa = 0
        labx = Label(fra2, text = '單字測驗', height = 2, width = 600, font = ('Arial', 15), bg = '#dcdc3d')
        labx.pack()
        frax1 = Frame(fra2, bg = "green", height=200)
        frax1.pack(fill = "x")
        frax1.propagate(0)
        labx1 = Label(frax1, font = ('Arial', 20), bg = 'green')
        labx1.pack(pady = 10)
        japp = random.choice(list(database.keys()))
        chii = database[japp]
        labx1.config(text = "請輸入  "+ chii +"  的日文")
        entx = Entry(frax1, width = 30)
        entx.pack()
        butx = Button(frax1, width = 10, text = '送出', command = answ)
        butx.pack(pady = 10)
        butx1 = Button(frax1, text = "下一題", width = 10, command = lambda: [labx.pack_forget(),labx1.pack_forget(),labx2.pack_forget(),entx.delete(0,END),pri(),entx.forget(),butx1.forget(),butx2.forget(),butx.forget(),frax1.destroy()])
        butx1.pack()
        labx2 = Label(fra2,bg = 'green', fg = 'yellow', font = ('Arial', 15))
        labx2.pack(pady = 58)
        butx2 = Button(fra2, text = '返回', bg = '#66FFE6', activebackground = '#66FFE6', width = 10, font = 1, command = RZ)
        butx2.pack(side = "bottom")
    pri()

# show all (ok)
def all_():
    database_cop = dict()
    database_cop.update(dic4)
    database_cop.update(dic5)
    k = 1
    m = 0
    fra1 = Frame(win, bg = "blue")
    fra1.pack()
    l = Label(fra1, text = '收錄之詞庫(四,五回)', font = ('Arial', 11), width = 600, bg = 'pink')
    l.pack()
    sc = Scrollbar(fra1)
    sc.pack(side = RIGHT, fill = Y)
    lib = Listbox(fra1, height = 28,bg = '#4066ff',yscrollcommand=sc.set)
    for i,j in database_cop.items():
        lib.insert(END, str(k)+".  "+ i + " (" + kans[m] + ")" +"   :      "+ j)
        m += 1
        k += 1
    lib.pack(fill = BOTH)
    sc.config(command = lib.yview)
    bu = Button(fra1, text = '返回', bg = '#66FFE6', activebackground = '#66FFE6', width = 10, font = 1, command = lambda:fra1.destroy())
    bu.pack()
    
def apart_4():
    a_k4 = 1
    a_m4 = 0
    a_fra4 = Frame(win, bg = "blue")
    a_fra4.pack()
    a_l4 = Label(a_fra4, text = '第四回', font = ('Arial', 11), width = 600,bg = 'pink')   #改名字
    a_l4.pack()
    a_sc4 = Scrollbar(a_fra4)
    a_sc4.pack(side = RIGHT, fill = Y)
    a_lib4 = Listbox(a_fra4, height = 28,bg = '#4066ff',yscrollcommand=a_sc4.set)
    for j in dic4.values():                                      #改字典
        a_lib4.insert(END, str(a_k4)+".  "+ data4[a_m4]  +"   :      "+ j) #改資料
        a_m4 += 1
        a_k4 += 1
    a_lib4.pack(fill = BOTH)
    a_sc4.config(command = a_lib4.yview)
    a_bu4 = Button(a_fra4, text = '返回', bg = '#66FFE6', activebackground = '#66FFE6', width = 10, font = 1, command = lambda:a_fra4.destroy())
    a_bu4.pack()

def apart_5():
    a_k5 = 1
    a_m5 = 0
    a_fra5 = Frame(win, bg = "blue")
    a_fra5.pack()
    a_l5 = Label(a_fra5, text = '第五回', font = ('Arial', 11), width = 600,bg = 'pink')   #改名字
    a_l5.pack()
    a_sc5 = Scrollbar(a_fra5)
    a_sc5.pack(side = RIGHT, fill = Y)
    a_lib5 = Listbox(a_fra5, height = 28,bg = '#4066ff',yscrollcommand=a_sc5.set)
    for j in dic5.values():                                      #改字典
        a_lib5.insert(END, str(a_k5)+".  "+ data5[a_m5]  +"   :      "+ j) #改資料
        a_m5 += 1
        a_k5 += 1
    a_lib5.pack(fill = BOTH)
    a_sc5.config(command = a_lib5.yview)
    a_bu5 = Button(a_fra5, text = '返回', bg = '#66FFE6', activebackground = '#66FFE6', width = 10, font = 1, command = lambda:a_fra5.destroy())
    a_bu5.pack()

win = Tk()
win.geometry('600x500')
win.title("日文單字練習")
win.config(bg = 'gold')  #太亮眼可以換顏色

def a():
    global fra1, fra2, fra3
    try:
        if fra1.exit():
            fra1.destroy()
        if fra2.exit():
            fra2.destroy()
        if fra3.exit():
            fra3.destroy()
    except:
        print("到底為什麼選單不會覆蓋==")

def bind(event):
    lab1.config(text = "作者 : 楊秉樺")

def bind1(event):
    lab1.config(text = "準備好來練習單字了嗎 ?")

menubar = Menu(win)   #選單欄位
# 第一個選單
function = Menu(menubar, tearoff = 0, bg = "pink") #空選單
menubar.add_cascade(label = 'func', menu = function)
function.add_command(label = '查詢單字', command = lambda: [search(), a()])
function.add_command(label = '單字練習', command = practice)
function.add_command(label = '所有單字', command = all_)
function.add_separator()    # 新增一條分隔線
function.add_command(label = '離開', command = lambda: win.destroy())

#第二個選單
databasic = Menu(menubar, tearoff = 0, bg = "pink") #空選單
menubar.add_cascade(label = 'data', menu = databasic)
databasic.add_command(label = '第四回', command = apart_4)
databasic.add_command(label = '第五回', command = apart_5)

# 內容
lab1 = Label(win, text = '準備好來練習單字了嗎 ?', fg = 'blue', bg = 'gold', font = 1)
but1 = Button(win, text = '查詢單字', fg = 'green', bg = '#66FFE6', activebackground = '#66FFE6', width = 10, font = 1, command = search)
but2 = Button(win, text = '單字練習', fg = 'green', bg = '#66FFE6', activebackground = '#66FFE6', width = 10, font = 1, command = practice)
but3 = Button(win, text = '所有單字', fg = 'green', bg = '#66FFE6', activebackground = '#66FFE6', width = 10, font = 1, command = all_)

lab1.bind("<Enter>", bind) # 滑鼠進入小部件事件
lab1.bind("<Leave>", bind1)

win.config(menu = menubar)
lab1.place(x = 190, y = 80)
but1.place(x = 80, y = 250)
but2.place(x = 240, y = 250)
but3.place(x = 400, y = 250)
win.mainloop()



