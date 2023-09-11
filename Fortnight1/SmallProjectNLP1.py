from tkinter import *
from tkinter import ttk
import tkinter as tk
from transformers import pipeline


class NLPProject1:
    
    def __init__(self):
        self.total_text = ""
        self.overall_score = 0
        self.counter = 0

    def App(self):
        #classifier_emo = pipeline("sentiment-analysis", model="SamLowe/roberta-base-go_emotions")
        self.classifier = pipeline("sentiment-analysis")

        self.root= tk.Tk()
        self.box_text = tk.StringVar()
        self.canvas1 = tk.Canvas(self.root, width=400, height=300)
        self.canvas1.pack()

        self.entry1 = tk.Entry(self.root, textvariable=self.box_text) 
        self.canvas1.create_window(200, 140, window=self.entry1)
        #user_input.place(x=300, y=105)


        self.full_text = tk.Label(self.root, text=self.total_text)
        self.canvas1.create_window(200, 220, window=self.full_text)
        self.text_tone = tk.Label(self.root, text="Unknown")
        self.canvas1.create_window(200, 100, window=self.text_tone)
        self.overall_emotion = tk.Label(self.root, text="None")
        self.canvas1.create_window(200, 280, window=self.overall_emotion)
        self.submit_button = tk.Button(self.root, text="Submit", command= lambda: self.submit_text())
        self.canvas1.create_window(200, 180, window=self.submit_button)
        self.root.mainloop()
    def submit_text(self):
        self.counter += 1
        b_text = self.box_text.get()
        results = self.classifier(b_text)
        if results[0]['label'] == "POSITIVE":
            self.text_tone = tk.Label(self.root, text="That was a positive sentence!")
        else:
            self.text_tone = tk.Label(self.root, text="That was a negative sentence...")
            
        self.canvas1.create_window(200, 100, window=self.text_tone)
        self.overall_score += results[0]['score']
        self.total_text = self.total_text + b_text
        self.full_text = tk.Label(self.root, text=self.total_text)
        self.canvas1.create_window(200, 220, window=self.full_text)
        final_emotion_score = self.overall_score / self.counter
        if final_emotion_score > .50:
            self.overall_emotion = tk.Label(self.root, text="All of your sentences combined give an overall POSITIVE emotion!")
        else:
            self.overall_emotion = tk.Label(self.root, text="All of your sentences combined give an overall NEGATIVE emotion!")
        self.canvas1.create_window(200, 280, window=self.overall_emotion)

inter = NLPProject1()

inter.App()
