from tkinter import *
import googletrans
from tkinter import ttk, messagebox

root = Tk()
root.attributes('-type', 'dialog')
translator = googletrans.Translator()

def translate_it():
    translated_text.delete(1.0, END)
    words = original_text.get(1.0, END)
    words = translator.translate(words, dest="ru") 
    translated_text.insert(1.0, words.text)
    root.after(1000, translate_it)

# Text Boxes
original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)
translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=1, pady=20, padx=10)

root.after(1000, translate_it)
root.mainloop()
