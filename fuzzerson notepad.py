import tkinter as tk
from tkinter import filedialog
from tkinter import font
#from tklinenums import TkLineNumbers
import sys


root = tk.Tk()
root.title("fuzzerson notepad")
root.geometry("700x600")
darkmode = 'false'
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

def wordWrapping():
    if text.cget("wrap") == "char":
        text.configure(wrap="none")
        settingsMenu.entryconfig("Disable Word Wrapping", label="Enable Word Wrapping")
        
        
    else:
        text.configure(wrap="char")
        settingsMenu.entryconfig("Enable Word Wrapping", label="Disable Word Wrapping")

def darkMode():
    global darkmode
    global defaultColour
    global defaultafg
    global defaultabg
    dc = defaultColour
    
    if darkmode == 'false':
        root.configure(bg="#2b2b2b")
        text.configure(bg="#3d3d3d",fg="white")
        textFrame.configure(bg="#2b2b2b")
        menuRow.configure(bg="#2b2b2b")
        scrollbar.configure(bg="#3d3d3d",)
        scrollbarx.configure(bg="#3d3d3d",)
        settings.configure(bg="#3d3d3d",foreground="white", activeforeground="white", activebackground="#4d4d4d")
        settingsMenu.configure(bg="#3d3d3d",foreground="white", activeforeground="white", activebackground="#4d4d4d")
        file.configure(bg="#3d3d3d",foreground="white", activeforeground="white", activebackground="#4d4d4d")
        fileMenu.configure(bg="#3d3d3d",foreground="white", activeforeground="white", activebackground="#4d4d4d")
        edit.configure(bg="#3d3d3d",foreground="white", activeforeground="white", activebackground="#4d4d4d")
        editMenu.configure(bg="#3d3d3d",foreground="white", activeforeground="white", activebackground="#4d4d4d")
        notify.configure(bg="#2b2b2b",fg="white")
        settingsMenu.entryconfig("Dark Mode", label="Light Mode")
        darkmode = 'true'
    else:
        root.configure(bg=dc)
        text.configure(bg="white",fg="black")
        textFrame.configure(bg=dc)
        menuRow.configure(bg=dc)
        scrollbar.configure(bg=dc,)
        scrollbarx.configure(bg=dc,)
        settings.configure(bg=dc,foreground="black", activeforeground="black", activebackground=defaultabg)
        settingsMenu.configure(bg=dc,foreground="black", activeforeground="black", activebackground=defaultabg)
        file.configure(bg=dc,foreground="black", activeforeground="black", activebackground=defaultabg)
        fileMenu.configure(bg=dc,foreground="black", activeforeground="black", activebackground=defaultabg)
        edit.configure(bg=dc,foreground="black", activeforeground="black", activebackground=defaultabg)
        editMenu.configure(bg=dc,foreground="black", activeforeground="black", activebackground=defaultabg)
        notify.configure(bg=dc,fg="black")
        settingsMenu.entryconfig("Light Mode", label="Dark Mode")
        darkmode = 'false'


#Text font
font = font.Font(family="Monospace", size=12,)

# file menu
menuRow = tk.Frame(root,)
menuRow.pack(anchor="nw", padx="10", pady=(10, 3))

file = tk.Menubutton(menuRow, text="File", relief="raised",)
file.pack(side="left",)
fileMenu = tk.Menu(file, tearoff=0)
file["menu"] = fileMenu

fileMenu.add_command(label="Save", command=normalSave)
fileMenu.add_command(label="Save As", command=Save)
fileMenu.add_command(label="Open File", command=openFile)

# edit menu
edit = tk.Menubutton(menuRow, text="Edit", relief="raised",)
edit.pack(side="left", padx="5")
editMenu = tk.Menu(edit, tearoff=0)
edit["menu"] = editMenu

editMenu.add_command(label="Copy", command=Copy)
editMenu.add_command(label="Paste", command=Paste)
editMenu.add_command(label="Increase Font Size", command=plusFontSize)
editMenu.add_command(label="Decrease Font Size", command=minusFontSize)

# settings menu
settings = tk.Menubutton(menuRow, text="Settings", relief="raised",)
settings.pack(side="left", padx=(0,5))
settingsMenu = tk.Menu(settings, tearoff=0)
settings["menu"] = settingsMenu

settingsMenu.add_command(label="Disable Word Wrapping", command=wordWrapping)
settingsMenu.add_command(label="Dark Mode", command=darkMode)

#notification

notify = tk.Label(menuRow, text="", anchor="w")
notify.pack()

# non-menu stuff marker
textFrame = tk.Frame(root,)
textFrame.pack(fill="both", expand="True")

scrollbar = tk.Scrollbar(textFrame, orient=tk.VERTICAL,)
scrollbar.pack(side="right", fill="y", padx=(0,10),)

#numbers = tk.Text(textFrame, font=font, width="3", yscrollcommand=scrollbar.set)
#numbers.pack(side="left", fill="y", padx=(10,0), pady=(0,5))
scrollbarx = tk.Scrollbar(root, orient=tk.HORIZONTAL,)
scrollbarx.pack(fill="x", padx=(10,10), pady=(0,10),)

text = tk.Text(textFrame, font=font, yscrollcommand=scrollbar.set, xscrollcommand=scrollbarx.set, wrap="char")


#numbers = TkLineNumbers(textFrame, text, width=1)
#numbers.pack(side="left", fill="y", padx=(5,0))

text.pack(padx=(10,5), pady=(0, 5), fill="both", expand="True", side="left")

scrollbar.config(command=text.yview)


# changing text keybind

root.bind("<Control-equal>", lambda e: plusFontSize())
root.bind("<Control-minus>", lambda e: minusFontSize())
text.bind_class("Text", "<Control-a>", selectAll)
text.bind_class("Text", "<Control-A>", selectAll)
#text.bind("<Key>", lambda event: root.after_idle(numbers.redraw), add=True)


defaultColour = root.cget("bg")
defaultafg = settings.cget("activeforeground")
defaultabg = settings.cget("activebackground")


#open with os
if len(sys.argv) > 1:
    filePath = sys.argv[1]

    with open(filePath, "r") as file:
        text.delete("1.0", tk.END)
        text.insert("1.0", file.read())

    fileName = filePath
    notify.configure(text="File Opened")

root.mainloop()
