##coded by SegentThomasKelly for a school project
#started the 24th November 2017, at 09:29 AM
#first version finished the 25th of November 2017 at 9:33 PM
#second version finished the 9th of December 2017 at 2:17 PM

# =========================== INITIALISATION ================================= #
from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox
from tkinter.colorchooser import askcolor
import tkinter.ttk as ttk
from PIL import Image, ImageDraw, ImageFont
import os
Transparency=TheSizePolice=RotationAngle=0

# ========================== FUNCTIONS ======================================= #
#>>> A FUNCTION TO HANDLE ERRORS <<<
def errorReported(error):
    if error == 'fields':
        tkinter.messagebox.showerror("Something went wrong", "You did not set all fields required\nTry again...")
    elif error == 'noPathWatermark':
        tkinter.messagebox.showerror("An error occured", "It seems that something didn't end well...\nVisibly you didn't choose the directory and name you want to save the watermark...\nWatermark file will be deleted when finished.")
    elif error == 'noPathOpenSave':
        tkinter.messagebox.showerror("An error occured", "It seems that something didn't end well...\nPlease try again and be careful to set everything needed.")
    elif error == 'allDoneWell':
        tkinter.messagebox.showinfo("That's all done !", "It's done !")

#>>> UPDATE THE VALUE OF TRANSPARENCY SCALE WIDGET <<<
def updateTransparency(x):
    global Transparency
    Transparency=int(x)

#>>> UPDATE THE VALUE OF POLICE SIZE SCALE WIDGET <<<
def updateSizePolice(x):
    global TheSizePolice
    TheSizePolice=int(x)

#>>> UPDATE THE VALUE OF ROTATION SCALE WIDGET <<<
def updateRotation(x):
    global RotationAngle
    RotationAngle=int(x)

#>>> ASSIGN VARIABLES <<<
def getVars():
    global Transparency, TheSizePolice, root
    WatermarkImagePath = ''
    if TheSizePolice == 0:
        TheSizePolice=10
    if PoliceSelect.get() != '' and WatermarkText.get() != '':
        TheFont=str(PoliceSelect.get())
        TheWatermark=str(WatermarkText.get())
        RVB=askcolor()[1]
        if TheFont == 'verdana (normal)':
            TheFont='verdana'
        elif TheFont == 'verdana (italic)':
            TheFont='verdanai'
        elif TheFont == 'verdana (bold)':
            TheFont='verdanab'
        root.fileopen = askopenfilename(defaultextension=".png", parent=root,
                title="Choose a file to open...", filetypes=[("PNG, Portable Network Graphics (Image)","*.png"), ("JPEG, Joint Photographic Experts Group (Image)",".jpg")])
        root.filesave = asksaveasfilename(defaultextension=".png",
                parent=root, title="Where to save this ?", filetypes=[("PNG, Portable Network Graphics (Image)","*.png")])
        if saveme.get() == 1:
            errorWatermarkPath=0
            WatermarkImagePath = asksaveasfilename(defaultextension=".png",
                parent=root, title="The watermark you want to save...", filetypes=[("PNG, Portable Network Graphics (Image)","*.png")])
            if WatermarkImagePath == '':
                errorReported('noPathWatermark')
        if WatermarkImagePath == '':
            errorWatermarkPath=1
            WatermarkImagePath= 'rotated.png'
        coreOfTheProgramm(TheSizePolice, TheWatermark, TheFont, RVB, WatermarkImagePath, errorWatermarkPath)
    else:
        errorReported('fields')

#>>> HELP AND ABOUT WINDOW <<<
def helpAbout():
    helpAbout = Tk()
    helpAbout.title("Help/About")
    helpAbout.configure(background='lavender')
    helpAbout.resizable(width=False, height=False)
    if os.path.isfile('iconAddWatermark.ico') == True:
        helpAbout.iconbitmap('iconAddWatermark.ico')
    mainLabelHelp= Label (helpAbout, text='This program has been made for a school project.\nWe added some nice features to make it better and played with it.\nIn order to use it, you have to tell the program the text you want to watermark\nThen you choose a font, a police size, the opacity you want\nto apply, the opacity (let at 0% to make it full, like 100%)\nthen you select rotation if you want, and tick the checkbox if you want to save\nthe watermark which will be generated, then click on start and voila !', bg='lavender').pack(padx=10, pady=5)
    leaveHelp= Button(helpAbout, text='RETURN', command=helpAbout.destroy, bg='orange red').pack(side=BOTTOM,padx=5, pady=5)
    mainloop()

#>>> PROGRAMM'S CORE <<<
def coreOfTheProgramm(TheSizePolice, TheWatermark, TheFont, RVB, WatermarkImagePath,errorWatermarkPath):
    global RotationAngle, Transparency
    if root.fileopen == '' or root.filesave == '':
        errorReported('noPathOpenSave')
    else:
        pass
    monImage = Image.open(root.fileopen)
    monImage.convert('RGBA')
    WIDTH, HEIGHT= monImage.size
    monWatermark= Image.new("RGBA", (WIDTH, HEIGHT), (125, 252, 156, 0))
    font = ImageFont.truetype(TheFont,TheSizePolice)
    CentreHauteur = (HEIGHT/2) - (font.getsize(TheWatermark)[1]/2)
    CentreLargeur = (WIDTH/2) - (font.getsize(TheWatermark)[0]/2)
    draw = ImageDraw.Draw(monWatermark)
    draw.text((int(CentreLargeur),int(CentreHauteur)),TheWatermark, font=font, fill=RVB)
    monWatermark.rotate(RotationAngle).save(WatermarkImagePath)
    monWatermarkRotated=Image.open(WatermarkImagePath)
    if Transparency != 0:
        TransparencyA= int((255*int(Transparency))/100)
        widthW, heightW = monWatermarkRotated.size
        for x in range(widthW):
            for y in range(heightW):
                pixelData = monWatermarkRotated.getpixel((x,y))
                if pixelData[3] != 0:
                    monWatermarkRotated.putpixel ( (x,y), (pixelData[0], pixelData[1], pixelData[2], TransparencyA))
    monImage.paste(monWatermarkRotated, (0,0), monWatermarkRotated)
    monImage.save(root.filesave, "PNG")
    monWatermarkRotated.save(WatermarkImagePath)
    if saveme.get() == 0 or errorWatermarkPath == 1:
        os.remove(WatermarkImagePath)
    monImage.show()
    monImage.close()
    monWatermarkRotated.close()
    monWatermark.close()
    errorReported('allDoneWell')

# ========================== WINDOW AND MAIN OPTIONS ========================= #
def start():
    global PoliceSelect, WatermarkText, saveme, root
    root=Tk()
    root.title("Add watermarks to your images")
    root.resizable(width=False, height=False)
    root.configure(background='lavender')
    if os.path.isfile('iconAddWatermark.ico') == True:
        root.iconbitmap('iconAddWatermark.ico')
    mainLabel= Label(root, text="- This program allows you to add watermarks to your pictures -\n", bg='lavender').pack()
    menuLabel= Label(root, text="Enter the text you want to watermak :", bg='lavender').pack()
    WatermarkText=StringVar()
    entryWatermarkText= Entry(menuLabel, textvariable=WatermarkText, width=65).pack(padx=20)
    PoliceLabel=Label(root, text="Choose the police you want:", bg='lavender').pack()
    PoliceSelect= StringVar()
    PoliceChoix= ('arial', 'georgia', 'impact', 'tahoma', 'verdana (normal)', 'verdana (italic)', 'verdana (bold)')
    ListePolice= ttk.Combobox(root, textvariable=PoliceSelect, values=PoliceChoix,
                state='readonly').pack()
    scaleSizePolice= Scale(root, orient='horizontal', from_=10, to=150, resolution=1,
                tickinterval=20, length=390, label='Police Size',
                command=updateSizePolice, bg='lavender').pack()
    TransparencyScale= Scale(root, orient='horizontal', from_=0, to=100, resolution=1,
                tickinterval=10, length=390, label='Opacity (%)',
                command=updateTransparency, bg='lavender').pack()
    RotationScale= Scale(root, orient='horizontal', from_=0, to=360, resolution=1,
                tickinterval=45, length=390, label='Rotation angle',
                command=updateRotation, bg='lavender').pack()
    saveme=IntVar()
    toSaveOrNotToSave= Checkbutton (root, text='Save the watermark file', variable=saveme, bg='lavender').pack()
    buttonContinue= Button(root, text="START", command=getVars, bg= 'chartreuse').pack(side=RIGHT, padx=50, pady=5)
    buttonQuit= Button(root, text="QUIT", command=root.destroy, bg='orange red').pack(side=LEFT, padx=50, pady=5)
    buttonHelp= Button(root, text="HELP/ABOUT", command=helpAbout, bg='deepskyblue2').pack()
    mainloop()

start()

##END
