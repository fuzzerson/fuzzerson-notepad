import tkinter as tk
from tkinter import filedialog
from tkinter import font

root = tk.Tk()
root.title("fuzzerson notepad")
root.geometry("700x600")

fileName = None

def Save():    
        filePath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Choose where to save your file"
        )
        
        if filePath:
            with open(filePath,"w") as file:
                content = text.get("1.0", tk.END)
                file.write(f"{content}")
                notify.configure(text="File Saved")

def normalSave():
    global fileName
    
    if not fileName == None:
        with open(fileName,"w") as file:
            content = text.get("1.0", tk.END)
            file.write(f"{content}")
            notify.configure(text="File Saved")
    else:
    
        filePath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Choose where to save your file"
        )
        
        if filePath:
            with open(filePath,"w") as file:
                content = text.get("1.0", tk.END)
                file.write(f"{content}")
                notify.configure(text="File Saved")

def Copy():
    root.clipboard_clear()
    root.clipboard_append(text.get("1.0", tk.END))
    root.update()

def Paste():
    try:
        pastedText = root.clipboard_get()
        text.insert('insert', pastedText)
    except tk.TclError:
        pass
    
def plusFontSize():
    fontSize = font['size']
    font.configure(size=fontSize + 2)
    text.configure(font=font)
    
def minusFontSize():
    fontSize = font['size']
    font.configure(size=fontSize - 2)
    text.configure(font=font)

def openFile():
    global fileName
    print("Opened")
    
    filePath = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        title="Pick which file to open."
    )
    
    if filePath:
        with open(filePath,"r") as file:
            text.delete(1.0,tk.END)
            text.insert(1.0, file.read())
        fileName = filePath
        notify.configure(text="File Opened")

def selectAll(event):
    event.widget.event_generate("<<SelectAll>>")
    return "break"

#Text font
font = font.Font(family="Arial", size=18,)

menuRow = tk.Frame(root,)
menuRow.pack(anchor="nw", padx="10", pady=(10, 3))

save = tk.Button(menuRow, text="Save As", command=Save)
save.pack(side="left",)

normalsave = tk.Button(menuRow, text="Save", command=normalSave)
normalsave.pack(side="left", padx=(5,0))

openFile = tk.Button(menuRow, text="Open File", command=openFile)
openFile.pack(side="left", padx=(5,0))

# first time ever using menubutton in tk... Kinda nervous :D
edit = tk.Menubutton(menuRow, text="Edit", relief="raised",)
edit.pack(side="left", padx="5")
editMenu = tk.Menu(edit, tearoff=0)
edit["menu"] = editMenu

editMenu.add_command(label="Copy", command=Copy)
editMenu.add_command(label="Paste", command=Paste)
editMenu.add_command(label="Increase Font Size", command=plusFontSize)
editMenu.add_command(label="Decrease Font Size", command=minusFontSize)

#notification

notify = tk.Label(menuRow, text="", anchor="w")
notify.pack()


# non-menu stuff marker
text = tk.Text(root, font="font",)
text.pack(padx="10", pady=(0, 10), fill="both", expand="True")

# changing text keybind

root.bind("<Control-equal>", lambda e: plusFontSize())
root.bind("<Control-minus>", lambda e: minusFontSize())
text.bind_class("Text", "<Control-a>", selectAll)
text.bind_class("Text", "<Control-A>", selectAll)

root.mainloop()
