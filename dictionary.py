from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
import requests

root = Tk()

e = 3
count = 0
nw = 0
c = 5
pad = 10

root.title("Dictonary")

def error():
    # global e
    # error = Label(root,text="Couldnt find any defination for the given word- X {}".format(str(e-2)))
    # error.grid(row=3,column=0,columnspan=3)
    # e += 1
    messagebox.showerror("Error","Couldnt find any defination for the given word")

def search():
    global nw
    global c
    global count
    global pad
    word = input.get()

    if(nw==3):
        c += 3
        count = 0
        pad = 0

    if(nw>5):
        r.set(1)
        Radiobutton(root,text="Same window",variable=r,state=DISABLED).grid(row=1,column=2)

    if r.get() == 1:
        try:
            
            response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word))
            json_data = json.loads(response.text)
            try:
                json_data = json_data[1]

            except:
                json_data = json_data[0]

            subroot1 = Tk()
            subroot1.title("Result Window")

            meanings = json_data['meanings'][0]
            pos= meanings['partOfSpeech']
            defin = meanings['definitions'][0]
            defination = defin['definition']

            word1 = Label(subroot1,text="WORD: {}".format(json_data['word']),wraplength=500)
            phonetic = Label(subroot1,text="PHONETIC: {}".format(json_data['phonetic']),wraplength=500)
            origin = Label(subroot1,text="ORIGIN: {}".format(json_data['origin']),wraplength=500)
            posi = Label(subroot1,text="PART OF SPEECH: {}".format(pos),wraplength=500)
            defina = Label(subroot1,text="DEFINATION: {}".format(defination),wraplength=500)

            word1.grid(row=0,column=3)
            phonetic.grid(row=1,column=3)
            origin.grid(row=2,column=3)
            posi.grid(row=3,column=3)
            defina.grid(row=4,column=3)

        except:
            error()

    else:
        try:
            
            subroot1 = LabelFrame(root,padx=10,pady=10)
            response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word))
            json_data = json.loads(response.text)
            try:
                json_data = json_data[1]

            except:
                json_data = json_data[0]

            meanings = json_data['meanings'][0]
            pos= meanings['partOfSpeech']
            defin = meanings['definitions'][0]
            defination = defin['definition']

            word1 = Label(subroot1,text="WORD: {}".format(json_data['word']),wraplength=500)
            phonetic = Label(subroot1,text="PHONETIC: {}".format(json_data['phonetic']),wraplength=500)
            origin = Label(subroot1,text="ORIGIN: {}".format(json_data['origin']),wraplength=500)
            posi = Label(subroot1,text="PART OF SPEECH: {}".format(pos),wraplength=500)
            defina = Label(subroot1,text="DEFINATION: {}".format(defination),wraplength=500)

        

            subroot1.grid(row=count,column=c,rowspan=3,columnspan=3,padx=0)
            word1.grid(row=0,column=3)
            phonetic.grid(row=1,column=3)
            origin.grid(row=2,column=3)
            posi.grid(row=3,column=3)
            defina.grid(row=4,column=3)
            count += 3
            nw += 1
        

        except:
            error()
        


# {'word': 'hello', 'phonetic': 'həˈləʊ', 'phonetics': [{'text': 'həˈləʊ', 'audio': '//ssl.gstatic.com/dictionary/static/sounds/20200429/hello--_gb_1.mp3'}, {'text': 'hɛˈləʊ'}], 'origin': 'early 19th century: variant of earlier hollo ; related to holla.', 'meanings': [{'partOfSpeech': 'exclamation', 'definitions': [{'definition': 'used as a greeting or to begin a phone conversation.', 'example': 'hello there, Katie!', 'synonyms': [], 'antonyms': []}]}, {'partOfSpeech': 'noun', 'definitions': [{'definition': 'an utterance of ‘hello’; a greeting.', 'example': 'she was getting polite nods and hellos from people', 'synonyms': [], 'antonyms': []}]}, {'partOfSpeech': 'verb', 'definitions': [{'definition': 'say or shout ‘hello’.', 'example': 'I pressed the phone button and helloed', 'synonyms': [], 'antonyms': []}]}]}]

r = IntVar()
r.set(1)
label = Label(root,text="Enter a word")
input = Entry(root,width=20,borderwidth=5,fg="white",bg="black")
searchButton = Button(root,text="Search",width=30,command=search)

# bar = Scrollbar(root,orient=VERTICAL)
# bar.grid(row=0,column=7,sticky=NS)

Radiobutton(root,text="New window",variable=r,value=1).grid(row=1,column=1)
Radiobutton(root,text="Same window",variable=r,value=0).grid(row=1,column=2)
label.grid(row=0,column=0)
input.grid(row=0,column=1,columnspan=2)
searchButton.grid(row=2,column=0,columnspan=3)



root.mainloop()