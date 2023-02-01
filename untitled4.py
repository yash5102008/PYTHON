from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog
import os 

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background='darkblue')

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

file_name = Label(root, text="File Name")
file_name.place(relx=0.28, rely=0.03, anchor=CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46, rely=0.03, anchor=CENTER)

my_text = Text(root, height=35, width=80)
my_text.place(relx=0.5, rely=0.55, anchor=CENTER)


name=""
def openFile() :
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0,END)
    file_name = filedialog.askopenfilename(title= "Open File Name" , fileTypes=(("Texts Files ", "*.txt"),))
    print(file_name)
    name = os.path.basename(text_file)
    formatted_name = name.split('_')[0]
    input_file_name.insert(END, formatted_name)
    root.title(formatted_name)
    file_name = open(name, 'r')
    paragraph = file_name.read()
    my_text.insert(END, paragraph)
    file_name.close()
    
def save():
    input_name = input_file_name.get()
    file = open(input_name+".txt", "w")
    data = my_text.get("1.0",END)
    print(data)
    file.write(data)
    input_file_name.delete(0, END)
    my_text.delete(1.0, END)
    messagebox.showinfo("Update", "Success")
    
def closeWindow():
        root.destroy()
    
open_button = Button(root,image=open_img, text="Open File", command = openFile)
open_button.place(relx = 0.05, rely= 0.03, anchor=CENTER)
root.mainloop()
