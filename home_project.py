import os

from tkinter import *
from PIL import ImageTk, Image



root = '/home/q0000041/home_project/'

# for _, _, filelist in os.walk(root):
#     for fname in filelist:
#         asd = root + '\\' + fname
#         print('\t%s' % asd )



tmp = '/home/q0000041/home_project/123.jpeg'

root = Tk()

def left_click(event):
    print( 'left' )

def right_click(event):
    print('right')

def mid(event):
    print('mid')
def scroll(event):
    print('scroll')


frome = Frame(root, width = 800, height  = 600)
img = Image.open( tmp )
width, height = img.size

canvas = Canvas(bg = "black", height = height, width = width)

canvas.pack(expand = YES, fill = BOTH )

canvas.image = ImageTk.PhotoImage(img)
canvas.create_image(0,0,image = canvas.image, anchor = 'nw')
root.mainloop()

