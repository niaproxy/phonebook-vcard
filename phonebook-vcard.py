#!/usr/bin/python3
#-*- coding: utf-8 -*-
from Tkinter import *  
import tkFileDialog as filedialog
import tkMessageBox as messagebox  

def convert_csv():  
	try:
	    #infile.configure(text=selected.get()) 
	    infile = open(infilename)
	    
	    line = infile.readline()
	    outfile = open(outfilename, "w")
	    
	    while line:
		    outfile.write("BEGIN:VCARD\nVERSION:3.0\nCHARSET:UTF-8\n")
		    # print (line)
		    lst=line.split(';')
		    name = "N:%s\n" % lst[1]
		    fname = "FN:%s\n" % lst[1]
		    phone = "TEL;WORK;VOICE:%s" % lst[2]
		    title = "TITLE:%s\n" % lst[0]
		    org = "ORG;TYPE=work:ACME\n"
		    
		    outfile.write(name)
		    outfile.write(fname)
		    outfile.write(phone)
		    outfile.write(title)
		    if len(lst) > 3:
		       alt = "TEL;CELL;VOICE:%s\n" % lst[3]
		       outfile.write(alt)
		    outfile.write(org)
		    outfile.write("END:VCARD\n")
		    line = infile.readline()    
	    infile.close()
	    outfile.close()
	    messagebox.showinfo('', 'Converted successfully') 
	except Exception:
		messagebox.showerror('', 'Error occured')
		
def get_csv(): 
    global infilename 
    infilename = filedialog.askopenfilename(title = "Select",filetypes = (("CSV","*.csv"),("all files","*.*")))
    res = format(infilename)
    infile_lbl.configure(text=res)
def get_vcf(): 
    global outfilename 
    outfilename = filedialog.asksaveasfilename(title = "Save as",defaultextension='.vcf',filetypes = (("Vcard","*.vcf"),("all files","*.*")))
    res = format(outfilename)
    outfile_lbl.configure(text=res)    
    

window = Tk()  
window.title("Создание списка контактов")  
window.geometry('550x350')
back_text = Label(window, text="Укажи исходный файл в формате CSV", font=("Arial Bold", 14))  
back_text.grid(column=0, row=0)  

back_text2 = Label(window, text="Укажи файл для Vcard", font=("Arial Bold", 14))
back_text2.grid(column=0, row=6)
btn_vcf = Button(window, text="Сохранить как", command=get_vcf)
btn_vcf.grid(column=1, row=7)
outfile_lbl = Label(window,text="Конвертированый файл:",width=40)  
outfile_lbl.grid(column=0, row=7)  
btn_conv = Button(window, text="Конвертировать", command=convert_csv)
btn_conv.grid(column=0, row=8)
btn_file = Button(window, text="Обзор", command=get_csv)
btn_file.grid(column=1, row=5)
sample_text = Label(window, text="\nОбразец исходный данных:\nМонтер;Иванов Иван;123456;654321", font=("Arial Bold", 10)) 
sample_text.grid(column=0, row=9)
infile_lbl = Label(window,text="Исходный файл:",width=40)  
infile_lbl.grid(column=0, row=5)  

window.mainloop()
