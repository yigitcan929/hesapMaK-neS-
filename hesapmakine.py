import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("hesap makinesi yigido")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_821=tk.Button(root)
        GButton_821["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_821["font"] = ft
        GButton_821["fg"] = "#000000"
        GButton_821["justify"] = "center"
        GButton_821["text"] = "-"
        GButton_821.place(x=260,y=400,width=35,height=25)
        GButton_821["command"] = self.GButton_821_command

        GButton_796=tk.Button(root)
        GButton_796["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_796["font"] = ft
        GButton_796["fg"] = "#000000"
        GButton_796["justify"] = "center"
        GButton_796["text"] = "+"
        GButton_796.place(x=50,y=400,width=35,height=25)
        GButton_796["command"] = self.GButton_796_command

        GButton_371=tk.Button(root)
        GButton_371["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_371["font"] = ft
        GButton_371["fg"] = "#000000"
        GButton_371["justify"] = "center"
        GButton_371["text"] = "/"
        GButton_371.place(x=150,y=400,width=35,height=25)
        GButton_371["command"] = self.GButton_371_command

        GButton_299=tk.Button(root)
        GButton_299["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_299["font"] = ft
        GButton_299["fg"] = "#000000"
        GButton_299["justify"] = "center"
        GButton_299["text"] = "*"
        GButton_299.place(x=370,y=390,width=35,height=25)
        GButton_299["command"] = self.GButton_299_command

        GLineEdit_220=tk.Entry(root)
        GLineEdit_220["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_220["font"] = ft
        GLineEdit_220["fg"] = "#333333"
        GLineEdit_220["justify"] = "center"
        GLineEdit_220["text"] = "Entry"
        GLineEdit_220.place(x=70,y=210,width=70,height=25)

        GLineEdit_467=tk.Entry(root)
        GLineEdit_467["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_467["font"] = ft
        GLineEdit_467["fg"] = "#333333"
        GLineEdit_467["justify"] = "center"
        GLineEdit_467["text"] = "Entry"
        GLineEdit_467.place(x=440,y=210,width=70,height=25)

        GLineEdit_884=tk.Entry(root)
        GLineEdit_884["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_884["font"] = ft
        GLineEdit_884["fg"] = "#333333"
        GLineEdit_884["justify"] = "center"
        GLineEdit_884["text"] = "Entry"
        GLineEdit_884.place(x=210,y=210,width=70,height=25)

        GLabel_871=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_871["font"] = ft
        GLabel_871["fg"] = "#333333"
        GLabel_871["justify"] = "center"
        GLabel_871["text"] = "raKAM1"
        GLabel_871.place(x=70,y=170,width=70,height=25)

        GLabel_399=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_399["font"] = ft
        GLabel_399["fg"] = "#333333"
        GLabel_399["justify"] = "center"
        GLabel_399["text"] = "rakam2"
        GLabel_399.place(x=200,y=170,width=70,height=25)

        GLabel_231=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_231["font"] = ft
        GLabel_231["fg"] = "#333333"
        GLabel_231["justify"] = "center"
        GLabel_231["text"] = "sonuç"
        GLabel_231.place(x=440,y=170,width=70,height=25)

    def GButton_821_command(self):
        print("buton 3 basildi")


    def GButton_796_command(self):
        print("buton 1 basildi")


    def GButton_371_command(self):
        print("buton 2 yazildi")


    def GButton_299_command(self):
        print("buton  4 basildi ")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)

    textBoxYazilanlar1=tk.StringVar()
    textBoxYazilanlar2=tk.StringVar()
    textBoxYazilanlar3=tk.StringVar()
    root.mainloop()
