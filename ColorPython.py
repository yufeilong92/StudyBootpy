#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 20:15
# @Author  : backpacker
# @File    : ColorPython.py
# @Description : 颜色选择器

from tkinter import Tk,messagebox,filedialog
from tkinter.colorchooser import *
from tkinter import *

from PIL import ImageGrab

def hex2rgb(hex_color):
    h = hex_color
    rgb = (int((h[1:3]), 16), int((h[3:5]), 16), int((h[5:7]), 16))
    return rgb

def rgb2hex(rgb):
    hex_color = "#" + hex(rgb[0])[2:].zfill(2) + hex(rgb[1])[2:].zfill(2) + hex(rgb[2])[2:].zfill(2)
    return hex_color.upper()

def callback(event,root,colorHex, colorRGB, colorTv,w,h):
    root.destroy()
    img = ImageGrab.grab()
    img = img.resize((w, h))# 对截图大小重置为窗口大小。
    px = img.load()
    img.close()
    rgbroot = px[event.x, event.y]

    rgb_hex = rgb2hex(rgbroot)

    rgb_1 = hex2rgb(rgb_hex)

    setTvContent(colorHex,rgb_hex)
    setTvContent(colorRGB,rgb_1)
    colorTv.config(background=f"{rgb_hex}")


def gatherColor(colorHex:Text,colorRGB:Text,colorTv:Label):
    root =Toplevel()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.geometry(f"{w}x{h}+0+0")
    root.overrideredirect(True) # 隐藏窗口栏
    root.attributes('-alpha',0.01)# 设置透明度 最小0.01 设置为0 界面会消失掉
    root.configure(cursor="crosshair") # 设置鼠标样式
    root.bind("<Button-1>",lambda event:callback(event,root,colorHex,colorRGB,colorTv,w,h))
    root.bind("<Button-3>",lambda event:callback(event,root,colorHex,colorRGB,colorTv,w,h))
    mainloop()


def selectColor(colorHex:Text,colorRGB:Text,colorLB:Label):
    selectColor = askcolor()

    setTvContent(colorHex,selectColor.__getitem__(1))

    setTvContent(colorRGB,selectColor.__getitem__(0))

    colorLB.config(background=f"{selectColor.__getitem__(1)}")

    pass

def setTvContent(tv:Text,char:str):
    tv.delete(0.0,END)
    tv.insert(END,char)



def showDialog():
    root=Tk()
    root.geometry("640x540")
    root.title("颜色采集")

    withd=20
    height=1

    Label(root,text="颜色值HEX: ",width=withd,height=height,font=10,background="light gray").grid(row=0,column=0,pady=8)
    Label(root,text="颜色值RGB: ",width=withd,height=height,font=10,background="light gray").grid(row=1,column=0,pady=8)
    Label(root,text="颜色     : ",width=withd,height=height,font=10,background="light gray").grid(row=2,column=0,pady=8)
    Label(root,text="选择颜色值: ",width=withd,height=height,font=10,background="light gray").grid(row=3,column=0,pady=8)
    Label(root,text="选择颜色值: ",width=withd,height=height,font=10,background="light gray").grid(row=4,column=0,pady=8)

    colorHex = Text(root, width=withd,height=height,font=10, background="light gray")
    colorHex.grid(row=0,column=1,pady=8,padx=4)

    colorRGB = Text(root,width=withd,height=height, font=10, background="light gray")
    colorRGB.grid(row=1,column=1,pady=8,padx=4)

    colorTv = Label(root, width=withd,height=height,font=10, background="light gray")
    colorTv.grid(row=2,column=1,pady=8,padx=4)

    Button(root,text="点击采集", width=withd,height=height,font=10, background="light gray",
                      command=lambda :gatherColor(colorHex,colorRGB,colorTv)).grid(row=3,column=1,pady=8,padx=4)
    Button(root,text="点击选择", width=withd,height=height,font=10, background="light gray",
                      command=lambda :selectColor(colorHex,colorRGB,colorTv)).grid(row=4,column=1,pady=8,padx=4)
    mainloop()

if __name__ == '__main__':
    showDialog()
