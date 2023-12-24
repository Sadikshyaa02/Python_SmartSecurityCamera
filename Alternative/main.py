# Media Tech Assignment - Emily Fletcher 18410839
# Import Statements

import motion
from tkinter import *
from tkvideo import tkvideo
import tkinter as tk
from tkinter import ttk

videoPath1 = 'nv232.MOV'
# video1 = motion.motion_detection(videoPath1)

# Raw Videos
video1 = videoPath1
video2 = videoPath1
video3 = videoPath1
video4 = videoPath1

# Videos with motion detection, 
# Calls the motion detection function from the motion class
MDVideo1 = motion.motion_detection(videoPath1)
MDVideo2 =  motion.motion_detection(videoPath1)
MDVideo3 =  motion.motion_detection(videoPath1)
MDVideo4 =  motion.motion_detection(videoPath1)

root = tk.Tk()
# sets title
root.title("Warehouse Security Camera")

#GUI set up for tabs
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

# Setting titles for tabs and adding tabs to the window
tabControl.add(tab1, text='Live Feed')
tabControl.add(tab2, text='Motion Detection')
tabControl.add(tab3, text='Saved Motion')
tabControl.pack(expand=1, fill="both")

# Live Feed Tab
# set up for video source one
LFLabel = tk.Label(tab1, text="Live Feed")
VSource1Pos = tk.Label(tab1, text="Source 1")
VSource1Lb = tk.Label(tab1, text="Source 1")
source1 = tkvideo(video1, VSource1Pos, size=(300, 150))
source1.play()

# set up forvideo source two
VSource2Pos = tk.Label(tab1, text="Source 2")
VSource2Lb = tk.Label(tab1, text="Source 2")
source2 = tkvideo(video2, VSource2Pos, size=(300, 150))
source2.play()

# set up forvideo source three
VSource3Pos = tk.Label(tab1, text="Source 3")
VSource3Lb = tk.Label(tab1, text="Source 3")
source3 = tkvideo(video3, VSource3Pos, size=(300, 150))
source3.play()

# set up forvideo source four
VSource4Pos = tk.Label(tab1, text="Source 4")
VSource4Lb = tk.Label(tab1, text="Source 3")
source4 = tkvideo(video4, VSource4Pos, size=(300, 150))
source4.play()

# code for action log
actionLogLb = tk.Label(tab1, text="Action Log")
actionLog = tk.Text(tab1, height=5)

#assigning Live Feed Elements in a grid layout to the live feed tab
LFLabel.grid(row=0, column=0)
VSource1Lb.grid(row=1, column=0)
VSource1Pos.grid(row=2, column=0)
VSource2Lb.grid(row=1, column=1)
VSource2Pos.grid(row=2, column=1)
VSource3Lb.grid(row=3, column=0)
VSource3Pos.grid(row=4, column=0)
VSource4Lb.grid(row=3, column=1)
VSource4Pos.grid(row=4, column=1)
actionLogLb.grid(row=5, column=0)

# action log is stick so it spreads across two columns
actionLog.grid(row=6, column=0, columnspan=2, sticky=tk.W+tk.E)

# Motion Detection Tab
MDLabel = tk.Label(tab2, text="Motion Detection")

#Motion detection for source 1
MDSource1Pos = tk.Label(tab2, text="Source 1")
MDSource1Lb = tk.Label(tab2, text="Source 1")
MDSource1 = tkvideo(MDVideo1, MDSource1Pos, size=(300, 150))
MDSource1.play()

#Motion detection for source 2
MDSource2Pos = tk.Label(tab2, text="Source 2")
MDSource2Lb = tk.Label(tab2, text="Source 2")
MDSource2 = tkvideo(MDVideo2, MDSource2Pos, size=(300, 150))
MDSource2.play()

#Motion detection for source 3
MDSource3Pos = tk.Label(tab2, text="Source 3")
MDSource3Lb = tk.Label(tab2, text="Source 3")
MDSource3 = tkvideo(MDVideo3, MDSource3Pos, size=(300, 150))
MDSource3.play()

#Motion detection for source 4
MDSource4Pos = tk.Label(tab2, text="Source 4")
MDSource4Lb = tk.Label(tab2, text="Source 4")
MDSource4 = tkvideo(MDVideo4, MDSource4Pos, size=(300, 150))
MDSource4.play()

#Motion detection action log
MDactionLogLb = tk.Label(tab2, text="Action Log")
MDactionLog = tk.Text(tab2, height=5)

#adding motion detection elements to the tab using a grid based layout
MDLabel.grid(row=0, column=0)
MDSource1Lb.grid(row=1, column=0)
MDSource1Pos.grid(row=2, column=0)
MDSource2Lb.grid(row=1, column=1)
MDSource2Pos.grid(row=2, column=1)
MDSource3Lb.grid(row=3, column=0)
MDSource3Pos.grid(row=4, column=0)
MDSource4Lb.grid(row=3, column=1)
MDSource4Pos.grid(row=4, column=1)
MDactionLogLb.grid(row=5, column=0)
MDactionLog.grid(row=6, column=0, columnspan=2, sticky=tk.W+tk.E)

#Save Motion tab
SMLabel = tk.Label(tab3, text="Saved Motion")
myLabel14 = tk.Label(tab3, text="Scroll Box")

SMLabel.grid(row=0, column=0)
myLabel14.grid(row=1, column=0)


root.mainloop()
