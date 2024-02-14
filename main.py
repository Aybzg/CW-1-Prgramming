from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from io import BytesIO
import  os

class Stegno:

    art ='''¯\_(ツ)_/¯'''
    art2 = '''
||'''
    output_image_size = 0

    def main(self,root):
        root.title('ImageSteganography')
        root.geometry('800x600')
        root.resizable(width =False, height=False)
        f = Frame(root)

        title = Label(f,text='Image Steganography')
        title.config(font=('courier',33))
        title.grid(pady=10)

        b_encode = Button(f,text="Encode",command= lambda :self.frame1_encode(f), padx=14)
        b_encode.config(font=('courier',14))
        b_decode = Button(f, text="Decode",padx=14,command=lambda :self.frame1_decode(f))
        b_decode.config(font=('courier',14))
        b_decode.grid(pady = 12)

        ascii_art = Label(f,text=self.art)
        # ascii_art.config(font=('MingLiU-ExtB',50))
        ascii_art.config(font=('courier',60))

        ascii_art2 = Label(f,text=self.art2)
        # ascii_art.config(font=('MingLiU-ExtB',50))
        ascii_art2.config(font=('courier',12,'bold'))

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        f.grid()
        title.grid(row=1)
        b_encode.grid(row=2)
        b_decode.grid(row=3)
        ascii_art.grid(row=4,pady=10)
        ascii_art2.grid(row=5,pady=5)
        
def home(self,frame):
            frame.destroy()
            self.main(root)

    def frame1_decode(self,f):
        f.destroy()
        d_f2 = Frame(root)
        label_art = Label(d_f2, text='٩(^‿^)۶')
        label_art.config(font=('courier',90))
        label_art.grid(row =1,pady=50)
        l1 = Label(d_f2, text='Select Image with Hidden text:')
        l1.config(font=('courier',18))
        l1.grid()
        bws_button = Button(d_f2, text='Select', command=lambda :self.frame2_decode(d_f2))
        bws_button.config(font=('courier',18))
        bws_button.grid()
        back_button = Button(d_f2, text='Cancel', command=lambda : Stegno.home(self,d_f2))
        back_button.config(font=('courier',18))
        back_button.grid(pady=15)
        back_button.grid()
        d_f2.grid()