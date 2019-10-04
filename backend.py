import json
from tkinter import *
from difflib import get_close_matches
import sqlite3

# Load the data from dataset
data = json.load(open("data.json"))

#connecting to database sqlite3
def connect_db():
    conn = sqlite3.connect("dictionary3.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dictionary3(id INTEGER PRIMARY KEY,word TEXT)")
    conn.commit()
    conn.close()

#insert data to database
def insert(word):
    connect_db()
    conn = sqlite3.connect("dictionary3.db")
    cur = conn.cursor()
    cur.execute("insert into dictionary3 values (NULL,?)",[word])
    conn.commit()
    conn.close()

#display data from database
def view():
    conn = sqlite3.connect("dictionary3.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM dictionary3")
    rows = cur.fetchall()
    conn.close()
    return rows

# finding best possible match
def match(word):
    li=[]
    msg = "Did you mean '%s'? " % (get_close_matches(word, data.keys())[0])
    li.append(msg)
    li.append("Enter 'Y': Yes")
    li.append("Enter 'N': No")
    return li


# searching for other matching word like that
def get_responce(responce, word):
    # elif len(get_close_matches(word, data.keys())) > 0:
    # close_match = match(word)

    if responce == 'y' or responce == "Y":
        return data[get_close_matches(word, data.keys())[0]]

    elif responce == 'n' or responce == "N":
        return "Sorry the word doesn't exist in dictionary, try another one."

    else:
        return "Incorrect enter only Y or N "


# User given word is searching in database
def translate(word):
    if word in data:
        return data[word]

    elif word.upper() in data:
        return data[word.upper()]

    elif word.title() in data:
        return data[word.title()]

    else:
        return 'Not found word'


# display the output
def display(result):
    return result

connect_db()