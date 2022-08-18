from tkinter import *
from googletrans import Translator, LANGUAGES
from tkinter import ttk, messagebox

root = Tk()
root.title('Herms (googleAPI-translator)')
root.attributes('-type', 'dialog')

translator = Translator()

def translate_it():
    translated_text.delete(1.0, END) # del previous translation
    # Get the To Language Key
    for key, value in languages.items():
        if (value == translated_combo.get()):
            language_key = key

    original = original_text.get(1.0, END)
    translation = translator.translate(original, dest=language_key)
    translated_text.insert(1.0, translation.text)
    root.after(1000, translate_it) # repeat every 1 second

language_list = (1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,16,1,1,1,1,1,1,1,1,1,1,1,1,1)
languages = LANGUAGES
language_list = list(languages.values()) # convert to list



# Text Boxes
original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=10, padx=10)
translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=1, pady=10, padx=10)

# Combo box
translated_combo = ttk.Combobox(root, width=38, value=language_list)
translated_combo.current(21)
translated_combo.grid(row=1, column=1, pady=5, padx=10)

root.after(1000, translate_it)
root.mainloop()
