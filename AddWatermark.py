##coded by SegentThomasKelly for a school project
#started the 24th November 2017, at 09:29 am
#first version finished the 25th of November 2017 at 9:33 PM

# =========================== INITIALISATION ================================= #
from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# ========================== FUNCTIONS ======================================= #
#>>> ASSIGN VARIABLES <<<
def getVars():
    TheSizePolice=int(SizePolice.get())
    ThePixelTop=int(PixelTop.get())
    ThePixelLeft=int(PixelLeft.get())
    TheWatermark=str(WatermarkText.get())
    root.fileopen = askopenfilename(defaultextension=".png", parent=root,
            title="Choose a file to open...", filetypes=[("PNG","*.png")])
    if int(TheSizePolice) >= 10 and int(TheSizePolice) <= 150:
        root.filesave = asksaveasfilename(defaultextension=".png",
                parent=root, title="Where to save this ?", filetypes=[("PNG","*.png")])
        coreOfTheProgramm(TheSizePolice, TheWatermark, ThePixelTop, ThePixelLeft)
    else:
        tkinter.messagebox.showerror("Something went wrong", "We told you to set the police size between 10 and 150 !\n Try again...")
        root.destroy()

#>>> PROGRAMM'S CORE <<<
def coreOfTheProgramm(TheSizePolice, TheWatermark, ThePixelTop, ThePixelLeft):
    monImage = Image.open(root.fileopen)
    font = ImageFont.truetype('verdanai.ttf',TheSizePolice)
    draw = ImageDraw.Draw(monImage)
    draw.text((ThePixelLeft,ThePixelTop),TheWatermark, font=font)
    del draw
    monImage.save(root.filesave, "PNG")
    monImage.show()
    tkinter.messagebox.showinfo("That's all done !", "It's done !")

# ========================== WINDOW AND MAIN OPTIONS ========================= #
root=Tk()
root.title("Add watermarks to your images")
mainLabel= Label(root, text="This programm allows you to add watermarks to your pictures\n").pack()
menuLabel= Label(root, text="Enter the text you want to watermak :").pack()
WatermarkText=StringVar()
entryWatermarkText= Entry(root, textvariable=WatermarkText, width=100).pack()
labelSizePolice= Label(root, text="Enter the police size you want (10 => 150) :").pack()
SizePolice=StringVar()
entrySizePolice= Entry(root, textvariable=SizePolice, width=10).pack()
labelPixelTop= Label(root, text="Enter how many pixel from the top you want :").pack()
PixelTop=StringVar()
entryPixelTop= Entry(root, textvariable=PixelTop, width=10).pack()
labelPixelLeft= Label(root, text="Same thing for the left :").pack()
PixelLeft=StringVar()
entryPixelLeft= Entry(root, textvariable=PixelLeft, width=10).pack()
buttonContinue= Button(root, text="START", command=getVars).pack()
buttonQuit= Button(root, text="QUIT", command=root.destroy).pack()
mainloop()

##END
