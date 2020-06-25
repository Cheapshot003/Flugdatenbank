from tkinter import *
import sqlite3



root = Tk()
root.title("Flugdatenbank 0.01")

def checkdb():
    popup = Tk()
    try:
        conn = sqlite3.connect("flugdata.db")
        cursor = conn.execute("SELECT * FROM fluege")
        for row in cursor:
            print(row)
        msg = "Datenbank verfügbar"
        title = "Verbindung erfolgreich" 
        label0 = Label(popup, text=msg, font=(None, 30), fg="green")
        label0.pack()
    except sqlite3.Error as e:
        msg = "Fehler: ", e.args[0]
        title = "Verbindung fehlgeschlagen"
        label0 = Label(popup, text=msg, font=(None, 30), fg="red")
        label0.pack()
    finally:    
        conn.close()
        popup.title(title)
        
        
        button0 = Button(popup, text="OK", command=popup.destroy)
        button0.pack()
        popup.mainloop()

def numberGen():
    conn = sqlite3.connect("flugdata.db")
    cursor = conn.execute("SELECT max(id) FROM fluege")
    soos = cursor.fetchone()
    number = soos[0] +1
    input1.delete(0,"end")
    input1.insert(0, str(number))
    conn.close()
def getFlight():
    if input1.get() == "":
        popup1 = Tk()
        popup1.title("Fehler")
        label000 = Label(popup1, text="Bitte Nummer eingeben",font=(None, 15))
        button000 = Button(popup1, text="Ok", command=popup1.destroy)

        label000.pack()
        button000.pack()
        popup1.mainloop()
    else:
        try:
            conn = sqlite3.connect("flugdata.db")
            cursor = conn.execute("SELECT * FROM fluege WHERE id=" + input1.get())
            row = cursor.fetchall()
            input2a = row[0][1]
            input3a = row[0][2]
            input4a = row[0][3]
            input5a = row[0][4]
            input6a = row[0][5]
            input7a = row[0][6]
            input8a = row[0][7]
            input9a = row[0][8]
            input10a = row[0][9]
            input11a = row[0][10]
            input12a = row[0][11]
            input2.delete(0,"end")
            input3.delete(0,"end")
            input4.delete(0,"end")
            input5.delete(0,"end")
            input6.delete(0,"end")
            input7.delete(0,"end")
            input8.delete(0,"end")
            input9.delete(0,"end")
            input10.delete(0,"end")
            input11.delete(0,"end")
            input12.delete(0,"end")
            input2.insert(0, input2a)
            input3.insert(0, input3a)
            input4.insert(0, input4a)
            input5.insert(0, input5a)
            input6.insert(0, input6a)
            input7.insert(0, input7a)
            input8.insert(0, input8a)
            input9.insert(0, input9a)
            input10.insert(0, input10a)
            input11.insert(0, input11a)
            input12.insert(0, input12a)
            conn.close()
        except IndexError as e:
            conn.close()
            popup2 = Tk()
            popup2.title("Fehler")
            labela = Label(popup2, text="Kein Flug mit dieser Nummer gefunden", font=(None, 15))
            buttona = Button(popup2, text="Ok", command=popup2.destroy)
            labela.pack()
            buttona.pack()
            popup2.mainloop()

def addFlight():
    conn = sqlite3.connect("flugdata.db")
    feld1 = input1.get()
    feld2 = input2.get()
    feld3 = input3.get()
    feld4 = input4.get()
    feld5 = input5.get()
    feld6 = input6.get()
    feld7 = input7.get()
    feld8 = input8.get()
    feld9 = input9.get()
    feld10 = input10.get()
    feld11 = input11.get()
    feld12 = input12.get()
    try:

        cursor = conn.execute("INSERT INTO fluege (id, muster, kennzeichen, pic, begleiter, startart, startort, landeort, startzeit, landezeit, gesamtzeit, anmerkungen) \
            VALUES (\"" + feld1 + "\", \"" + feld2 +"\", \"" + feld3 +"\", \"" + feld4 +"\", \"" + feld5 +"\", \"" + feld6 +"\", \"" + feld7 +"\", \"" + feld8 +"\", \"" + feld9 +"\", \"" + feld10 +"\", \"" + feld11 +"\", \"" + feld12 + "\")") 
        conn.commit()
        conn.close()
        popup4 = Tk()
        popup4.title("Eingabe erfolgreich")
        soos = "Daten erfolgreich eingefügt"
        labelq = Label(popup4, text=soos, font=(None, 15))
        buttonq = Button(popup4, text="Ok", command=popup4.destroy)
        labelq.pack()
        buttonq.pack()
        popup4.mainloop()
    except sqlite3.Error as e:
        conn.close()
        popup4 = Tk()
        soos = "Fehler" + e
        labelq = Label(popup4, text=soos, font=(None, 15))
        buttonq = Button(popup4, text="Ok", command=popup4.destroy)
        labelq.pack()
        buttonq.pack()
        popup4.mainloop()

def clearStuff():
    input1.delete(0,"end")
    input2.delete(0,"end")
    input3.delete(0,"end")
    input4.delete(0,"end")
    input5.delete(0,"end")
    input6.delete(0,"end")
    input7.delete(0,"end")
    input8.delete(0,"end")
    input9.delete(0,"end")
    input10.delete(0,"end")
    input11.delete(0,"end")
    input12.delete(0,"end")
def deleteFlight():
    try:
        conn =sqlite3.connect("flugdata.db")
        cursor = conn.execute("DELETE FROM fluege WHERE id = " + input1.get() + ";")
        conn.commit()
        conn.close()
        popup5 = Tk()
        labelw = Label(popup5, text="Flug wurde gelöscht", font=(None, 15))
        buttonw = Button(popup5, text="Ok", command=popup5.destroy)
        labelw.pack()
        buttonw.pack()
        popup5.mainloop()
    except sqlite3.Error as e:
        popup5 = Tk()
        soos = "Fehler: " + e
        labelw = Label(popup5, text=soos, font=(None, 15))
        buttonw = Button(popup5, text="Ok", command=popup5.destroy)
        labelw.pack()
        buttonw.pack()
        popup5.mainloop()

buttonclear = Button(root, text="Felder leeren", command=clearStuff)
button1 = Button(root, text="Flug hinzufügen", command=addFlight)
label1 = Label(root, text="Flugdatenbank", font=(None, 30))
label2 = Label(root, text="Version 0.01", font=(None, 15))
label3 = Label(root, text="Nummer:", font=(None, 10))
label4 = Label(root, text="Muster:", font=(None, 10))
label5 = Label(root, text="Kennzeichen:", font=(None, 10))
label6 = Label(root, text="PIC:", font=(None, 10))
label7 = Label(root, text="Begleiter:", font=(None, 10))
label8 = Label(root, text="Startart:", font=(None, 10))
label9 = Label(root, text="Startort:", font=(None, 10))
label10 = Label(root, text="Landeort:", font=(None, 10))
label11 = Label(root, text="Startzeit:", font=(None, 10))
label12 = Label(root, text="Landezeit:", font=(None, 10))
label13 = Label(root, text="Gesamtzeit in Minuten:", font=(None, 10))
label14 = Label(root, text="Anmerkungen:", font=(None, 10))
input1 = Entry(root)
input2 = Entry(root)
input3 = Entry(root)
input4 = Entry(root)
input5 = Entry(root)
input6 = Entry(root)
input7 = Entry(root)
input8 = Entry(root)
input9 = Entry(root)
input10 = Entry(root)
input11 = Entry(root)
input12 = Entry(root)
box= Button(root, text="Nummer erzeugen", command=numberGen)
box2 = Button(root, text="Flug abrufen", command=getFlight)
box3 = Button(root, text="Flug löschen", command=deleteFlight)
box4 = Button(root, text="Datenbank prüfen", command=checkdb)

buttonclear.grid(row=14, column=4)
box4.grid(row=14, column=3)
box3.grid(row=2, column=4)
box2.grid(row=2, column=3)
box.grid(row=2, column=2)
button1.grid(row=14, column=2)
label1.grid(row=0, column=1)
label2.grid(row=1, column=1)
label3.grid(row=2, column=0)
label4.grid(row=3, column=0)
label5.grid(row=4, column=0)
label6.grid(row=5, column=0)
label7.grid(row=6, column=0)
label8.grid(row=7, column=0)
label9.grid(row=8, column=0)
label10.grid(row=9, column=0)
label11.grid(row=10, column=0)
label12.grid(row=11, column=0)
label13.grid(row=12, column=0)
label14.grid(row=13, column=0)
input1.grid(row=2, column=1)
input2.grid(row=3, column=1)
input3.grid(row=4, column=1)
input4.grid(row=5, column=1)
input5.grid(row=6, column=1)
input6.grid(row=7, column=1)
input7.grid(row=8, column=1)
input8.grid(row=9, column=1)
input9.grid(row=10, column=1)
input10.grid(row=11, column=1)
input11.grid(row=12, column=1)
input12.grid(row=13, column=1)







root.mainloop()
