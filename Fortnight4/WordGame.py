from tkinter import *
from tkinter import ttk
import tkinter as tk
import nltk
import ssl
from nltk.corpus import wordnet as wn
import random

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
    
#nltk.download('wordnet')
#nltk.download('omw-1.4')

class WordGame:
    
    def __init__(self):
        self.none = None
        self.keywords = []
        self.all_words = []
        
    def generate_matches(self, cq):
        if cq == True:
            self.button1.grid_forget()
            self.button2.grid_forget()
            self.button3.grid_forget()
            self.button4.grid_forget()
            self.button5.grid_forget()
            self.button6.grid_forget()
            self.button7.grid_forget()
            self.button8.grid_forget()
            self.button9.grid_forget()
            self.button10.grid_forget()
            self.button11.grid_forget()
            self.button12.grid_forget()
        #self.matches_found = 0
        self.all_words = []
        for synset in wn.all_synsets():
            self.all_words.extend(synset.lemma_names())
        self.keywords = []
        m = 0
        while m < 6:
            rand_index = random.randint(0, len(self.all_words))
            if len(wn.synsets(self.all_words[rand_index])) > 5:
                self.keywords.append(self.all_words[rand_index])
                m+=1
        self.matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
        random.shuffle(self.matches)
        self.set_1 = wn.synsets(self.keywords[0])
        self.set_2 = wn.synsets(self.keywords[1])
        self.set_3 = wn.synsets(self.keywords[2])
        self.set_4 = wn.synsets(self.keywords[3])
        self.set_5 = wn.synsets(self.keywords[4])
        self.set_6 = wn.synsets(self.keywords[5])
        
        self.button1_done = False
        self.button2_done = False
        self.button3_done = False
        self.button4_done = False
        self.button5_done = False
        self.button6_done = False
        self.row_count = 0
        self.col_count = 1
        index = 0
        for i in self.matches:
            s = 0
            if i == 1:
                if self.button1_done == True:
                    
                    while s == 0:
                        set_name = self.set_1[random.randint(1, len(self.set_1)-1)].name()
                        final_word = ""
                        prev_name = self.set_1[0].name()
                        prev_word = ""
                            
                        for i in set_name:
                            if i == ".":
                                break
                            else:
                                final_word += i
                        for l in prev_name:
                            if l == ".":
                                break
                            else:
                                prev_word += l
                        
                        if final_word != prev_word:
                            s = 1
                        else:
                            s = 0
                    b7_index = index
                    self.button7 = Button(self.my_frame, text=final_word, font=("Times New Roman", 20), height=3, width=12, command=lambda: self.button_selected(self.button7, 7, b7_index))
                    self.button7.grid(row=self.row_count, column=self.col_count)
                else:
                    set_name = self.set_1[0].name()
                    final_word = ""
                    for i in set_name:
                        if i == ".":
                            break
                        else:
                            final_word += i
                    self.button1 = Button(self.my_frame, text=final_word, font=("Times New Roman", 20), height=3, width=12, command=lambda: self.button_selected(self.button1, 1, b1_index))
                    self.button1_done = True
                    b1_index = index
                    self.button1.grid(row=self.row_count, column=self.col_count)
                
            if i == 2:
                if self.button2_done == True:
                    while s == 0:
                        set_name = self.set_2[random.randint(1, len(self.set_2)-1)].name()
                        final_word = ""
                        prev_name = self.set_2[0].name()
                        prev_word = ""
                            
                        for i in set_name:
                            if i == ".":
                                break
                            else:
                                final_word += i
                        for l in prev_name:
                            if l == ".":
                                break
                            else:
                                prev_word += l
                        
                        if final_word != prev_word:
                            s = 1
                        else:
                            s = 0
                    b8_index = index
                    self.button8 = Button(self.my_frame, text=final_word, font=("Times New Roman", 20), height=3, width=12, command=lambda: self.button_selected(self.button8, 8, b8_index))
                    self.button8.grid(row=self.row_count, column=self.col_count)
                else:
                    set_name = self.set_2[0].name()
                    final_word = ""
                    for i in set_name:
                        if i == ".":
                            break
                        else:
                            final_word += i
                    self.button2 = Button(self.my_frame, text=final_word, font=("Times New Roman", 20), height=3, width=12, command=lambda: self.button_selected(self.button2, 2, b2_index))
                    self.button2_done = True
                    b2_index = index
                    self.button2.grid(row=self.row_count, column=self.col_count)
            if i == 3:
                if self.button3_done == True:
                    while s == 0:
                        set_name = self.set_3[random.randint(1, len(self.set_3)-1)].name()
                        final_word = ""
                        prev_name = self.set_3[0].name()
                        prev_word = ""
                            
                        for i in set_name:
                            if i == ".":
                                break
                            else:
                                final_word += i
                        for l in prev_name:
                            if l == ".":
                                break
                            else:
                                prev_word += l
                        
                        if final_word != prev_word:
                            s = 1
                        else:
                            s = 0
                    b9_index = index
                    self.button9 = Button(self.my_frame, text=final_word, font=("Times New Roman", 20), height=3, width=12, command=lambda: self.button_selected(self.button9, 9, b9_index))
                    self.button9.grid(row=self.row_count, column=self.col_count)
                else:
                    set_name = self.set_3[0].name()
                    final_word = ""
                    for i in set_name:
                        if i == ".":
                            break
                        else:
                            final_word += i
                    self.button3 = Button(self.my_frame, text=final_word, font=("Times New Roman", 20), height=3, width=12, command=lambda: self.button_selected(self.button3, 3, b3_index))
                    self.button3_done = True
                    b3_index = index
                    self.button3.grid(row=self.row_count, column=self.col_count)
            if i == 4:
                if self.button4_done == True:
                    while s == 0:
                        set_name = self.set_4[random.randint(1, len(self.set_4)-1)].name()
                        final_word = ""
                        prev_name = self.set_4[0].name()
                        prev_word = ""
                            
                        for i in set_name:
                            if i == ".":
                                break
                            else:
                                final_word += i
                        for l in prev_name:
                            if l == ".":
                                break
                            else:
                                prev_word += l
                        
                        if final_word != prev_word:
                            s = 1
                        else:
                            s = 0
                    b10_index = index
                    self.button10 = Button(self.my_frame, text=final_word, font=("Times New Roman", 20), height=3, width=12, command=lambda: self.button_selected(self.button10, 10, b10_index))
                    self.button10.grid(row=self.row_count, column=self.col_count)
                else:
                    set_name = self.set_4[0].name()
                    final_word = ""
                    for i in set_name:
                        if i == ".":
                            break
                        else:
                            final_word += i
                    self.button4 = Button(self.my_frame, text=final_word, font=("Times New Roman", 20), height=3, width=12, command=lambda: self.button_selected(self.button4, 4, b4_index))
                    self.button4_done = True
                    b4_index = index
                    self.button4.grid(row=self.row_count, column=self.col_count)
            if i == 5:
                if self.button5_done == True:
                    while s == 0:
                        set_name = self.set_5[random.randint(1, len(self.set_5)-1)].name()
                        final_word = ""
                        prev_name = self.set_5[0].name()
                        prev_word = ""
                            
                        for i in set_name:
                            if i == ".":
                                break
                            else:
                                final_word += i
                        for l in prev_name:
                            if l == ".":
                                break
                            else:
                                prev_word += l
                        
                        if final_word != prev_word:
                            s = 1
                        else:
                            s = 0
                    b11_index = index
                    self.button11 = Button(self.my_frame, text=final_word, font=("Times New Roman", 20), height=3, width=12, command=lambda: self.button_selected(self.button11, 11, b11_index))
                    self.button11.grid(row=self.row_count, column=self.col_count)
                else:
                    set_name = self.set_5[0].name()
                    final_word = ""
                    for i in set_name:
                        if i == ".":
                            break
                        else:
                            final_word += i
                    self.button5 = Button(self.my_frame, text=final_word, font=("Times New Roman", 20), height=3, width=12, command=lambda: self.button_selected(self.button5, 5, b5_index))
                    self.button5_done = True
                    b5_index = index
                    self.button5.grid(row=self.row_count, column=self.col_count)
            if i == 6:
                if self.button6_done == True:
                    while s == 0:
                        set_name = self.set_6[random.randint(1, len(self.set_6)-1)].name()
                        final_word = ""
                        prev_name = self.set_2[0].name()
                        prev_word = ""
                            
                        for i in set_name:
                            if i == ".":
                                break
                            else:
                                final_word += i
                        for l in prev_name:
                            if l == ".":
                                break
                            else:
                                prev_word += l
                        
                        if final_word != prev_word:
                            s = 1
                        else:
                            s = 0
                    b12_index = index
                    self.button12 = Button(self.my_frame, text=final_word, font=("Times New Roman", 20), height=3, width=12, command=lambda: self.button_selected(self.button12, 12, b12_index))
                    self.button12.grid(row=self.row_count, column=self.col_count)
                else:
                    set_name = self.set_6[0].name()
                    final_word = ""
                    for i in set_name:
                        if i == ".":
                            break
                        else:
                            final_word += i
                    self.button6 = Button(self.my_frame, text=final_word, font=("Times New Roman", 20), height=3, width=12, command=lambda: self.button_selected(self.button6, 6, b6_index))
                    self.button6_done = True
                    b6_index = index
                    self.button6.grid(row=self.row_count, column=self.col_count)
                    
            if self.col_count == 4:
                self.col_count = 1
                self.row_count += 1
            else:
                self.col_count += 1
            
            index += 1
        
    def wordgame_window(self):
        self.root = Tk()
        self.root.geometry("1000x1000")
        self.my_frame = Frame(self.root)
        self.my_frame.pack(pady=10)
        
        self.generate_matches(False)        
        self.answer_list = []
        self.answer_correct = []
        self.b1 = 0
        self.b2 = 0
        self.but1 = 0
        self.but2 = 0
        self.matches_found = 0
        
        generate_buttom = Button(self.root, text="Generate New Matches", font=("Times New Roman", 12), command=lambda: self.generate_matches(True))
        generate_buttom.pack()
        generate_buttom.place(x=500, y=500)
        
        self.error_label = Label(self.root, text="SELECT A BUTTON THEN FIND ITS MATCH!", font=("Times New Roman", 12))
        self.error_label.pack()
        self.error_label.place(x=350, y=300)
        self.root.mainloop()
        
        
    def button_selected(self, button, num, indexs):
        global count, answer_list
        self.error_label.pack_forget()
        if self.b1 == 0:
            self.b1 = indexs
            self.but1 = button
            #self.error_label = Label(self.root, text="YOU HAVE SELECTED BUTTON NUMBER: " + str(indexs) + ". NOW SELECT IT'S MATCH!", font=("Times New Roman", 12))
            #self.error_label.pack()
            #self.error_label.place(x=350, y=400)
        else:
            self.b2 = indexs
            self.but2 = button
            if self.matches[self.b1] == self.matches[self.b2]:
                self.error_label = Label(self.root, text="YOU HAVE FOUND A MATCH! GOOD JOB!", font=("Times New Roman", 12))
                self.error_label.pack()
                self.error_label.place(x=350, y=300)
                self.but1["text"] = ''
                self.but2["text"] = ''
                self.b1 = 0
                self.b2 = 0
                self.but1 = 0
                self.but2 = 0
                if self.matches_found == 5:
                    self.error_label = Label(self.root, text="YOU HAVE FOUND ALL OF THE MATCHES! GOOD JOB!", font=("Times New Roman", 12))
                    self.error_label.pack()
                    self.error_label.place(x=350, y=300)
                #self.matches_found += 1
            else:
                self.error_label = Label(self.root, text="NOT A MATCH! PLEASE TRY AGAIN", font=("Times New Roman", 12))
                self.error_label.pack()
                self.error_label.place(x=350, y=300)
                self.b1 = 0
                self.b2 = 0
                self.but1 = 0
                self.but2 = 0
                
        
        
wg = WordGame()

wg.wordgame_window()
