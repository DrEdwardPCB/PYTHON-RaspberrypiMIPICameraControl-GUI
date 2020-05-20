import Tkinter as tk
import os
import subprocess
import functools as ft

#helper method

def clearProperties(arg):
    timeout.delete(0,tk.END)
    quality.delete(0,tk.END)
    awb.delete(0,tk.END)
    ae.delete(0,tk.END)
    output.delete(0,tk.END)
    encoding.delete(0,tk.END)
    mode.delete(0,tk.END)
    
def defaultProperties(arg):
    clearProperties(arg)
    timeout.insert(0,"10000")
    quality.insert(0,"50")
    awb.insert(0,"1")
    ae.insert(0,"2")
    output.insert(0,"capture.jpg")
    encoding.insert(0,"jpg")
    mode.insert(0,"1")

def runCommand(arg):
    executionStringArr=[]
    executionStringArr.append('$HOME/Desktop/MIPI_Camera-master/RPI/arducamstill')
    if(timeout.get()!=""):
        print(timeout.get())
        executionStringArr.append('-t')
        executionStringArr.append(timeout.get())
    if(quality.get()!=""):
        print(quality.get())
        executionStringArr.append('-q')
        executionStringArr.append(quality.get())
    if(awb.get()!=""):
        print(awb.get())
        executionStringArr.append('-awb')
        executionStringArr.append(awb.get())
    if(ae.get()!=""):
        print(ae.get())
        executionStringArr.append('-ae')
        executionStringArr.append(ae.get())
    if(output.get()!=""):
        print(output.get())
        executionStringArr.append('-o')
        executionStringArr.append(output.get())
    if(encoding.get()!=""):
        print(encoding.get())
        executionStringArr.append('-e')
        executionStringArr.append(encoding.get())
    if(mode.get()!=""):
        print(mode.get())
        executionStringArr.append('-m')
        executionStringArr.append(mode.get())
    executionstr=ft.reduce(lambda x,y: x+" "+y,executionStringArr)
    print(executionstr)
    f=open("cameraScript.sh", "w")
    f.write('#!/bin/sh\ncd $HOME/Desktop ; ')
    f.write( executionstr+';')
    f.close()
    subprocess.call(['xdg-open','./cameraScript.sh'])
    
window=tk.Tk()
window.title("camera Control")

#configure window
window.rowconfigure(0, minsize = 300, weight=1)
window.columnconfigure(0,minsize = 300, weight=1)

#configure primary element
propertyPanel = tk.Frame(master=window)
presetPanel = tk.Frame(master=window)
executionPanel = tk.Frame(master=window)


#configure secondary element in property panel
property_PanelTitle=tk.Label(master=propertyPanel,text="Property Panel")
property_PanelTitle.grid(row=0,column=1)

propertyTitle=tk.Label(master=propertyPanel,text="properties")
propertyTitle.grid(row=1,column=0)

propertyValue=tk.Label(master=propertyPanel,text="values")
propertyValue.grid(row=1,column=1)

propertyDescription=tk.Label(master=propertyPanel,text="properties")
propertyDescription.grid(row=1,column=2)


timeoutT = tk.Label(text="Timeout",master=propertyPanel)
timeoutT.grid(row=2,column=0, padx=5, pady=5)

qualityT = tk.Label(text="Quality",master=propertyPanel)
qualityT.grid(row=3,column=0 , padx=5, pady=5)

awbT = tk.Label(text="Auto whitebalance",master=propertyPanel)
awbT.grid(row=4,column=0 , padx=5, pady=5)

aeT = tk.Label(text="Auto exposure",master=propertyPanel)
aeT.grid(row=5,column=0 , padx=5, pady=5)

outputT = tk.Label(text="Output filename",master=propertyPanel)
outputT.grid(row=6,column=0 , padx=5, pady=5)

encodingT = tk.Label(text="encoding",master=propertyPanel)
encodingT.grid(row=7,column=0 , padx=5, pady=5)

modeT = tk.Label(text="mode",master=propertyPanel)
modeT.grid(row=8,column=0 , padx=5, pady=5)

##Description
timeoutD = tk.Label(text="Time (in ms) before takes picture and shuts down (if not specified, loop)",master=propertyPanel)
timeoutD.grid(row=2,column=2, padx=5, pady=5)

qualityD = tk.Label(text="Set jpeg quality <0 to 100>",master=propertyPanel)
qualityD.grid(row=3,column=2 , padx=5, pady=5)

awbD = tk.Label(text="Enable or disable auto white balance 1= enable 0=disable",master=propertyPanel)
awbD.grid(row=4,column=2 , padx=5, pady=5)

aeD = tk.Label(text="Enable or disable auto exposure 1= enable 0=disable",master=propertyPanel)
aeD.grid(row=5,column=2 , padx=5, pady=5)

outputD = tk.Label(text="Output filename, must include file extension",master=propertyPanel)
outputD.grid(row=6,column=2 , padx=5, pady=5)

encodingD = tk.Label(text="one of jpg, png, raw, bmp, gif",master=propertyPanel)
encodingD.grid(row=7,column=2 , padx=5, pady=5)

modeD = tk.Label(text="0-2, 0 is fastest lowest resolution 2 is slowest highest resolution",master=propertyPanel)
modeD.grid(row=8,column=2 , padx=5, pady=5)

#input
timeout = tk.Entry(master=propertyPanel)
timeout.grid(row=2,column=1, padx=5, pady=5)

quality = tk.Entry(master=propertyPanel)
quality.grid(row=3,column=1 , padx=5, pady=5)

awb = tk.Entry(master=propertyPanel)
awb.grid(row=4,column=1 , padx=5, pady=5)

ae = tk.Entry(master=propertyPanel)
ae.grid(row=5,column=1 , padx=5, pady=5)

output = tk.Entry(master=propertyPanel)
output.grid(row=6,column=1 , padx=5, pady=5)

encoding = tk.Entry(master=propertyPanel)
encoding.grid(row=7,column=1 , padx=5, pady=5)

mode = tk.Entry(master=propertyPanel)
mode.grid(row=8,column=1 , padx=5, pady=5)

#preset panel
presetTitle=tk.Label(master = presetPanel, text="Preset Panel")
presetTitle.grid(row=0,column=0)

clearButton=tk.Button(master = presetPanel, text='clear')
clearButton.bind('<Button-1>', clearProperties)
clearButton.grid(row=1,column=0)

defaultButton=tk.Button(master = presetPanel, text='default')
defaultButton.bind('<Button-1>', defaultProperties)
defaultButton.grid(row=1,column=1)

#execution panel
executionTitle=tk.Label(master = executionPanel, text="Execution Panel")
executionTitle.grid(row=0,column=0)

executionButton=tk.Button(master = executionPanel, text="run")
executionButton.bind('<Button-1>', runCommand)
executionButton.grid(row=1,column=0 )

#adding to window
propertyPanel.grid(row=0,column=0)
presetPanel.grid(row=1,column=0)
executionPanel.grid(row=2,column=0)

window.mainloop()

