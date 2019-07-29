import os
from tkinter import *
from PIL import ImageTk, Image, ImageOps

tmp = 'C:\\Users\\jfgffju\\Pictures\\test\\123.jpg'


class Xz():
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0

    event_x =0
    event_y = 0

    width = 0
    height = 0
    root = None
    img = None
    canvas = None

    image_on_canvas = None

    dir_root =  'C:\\Users\\jfgffju\\Pictures\\test'

    img_set = []
    img_index = 0
    rect = None

    rect_size = 25
    cur_index = 0




    def __init__(self):
        for _, _, filelist in os.walk(self.dir_root):
            for fname in filelist:
                asd = self.dir_root + '\\' + fname
                self.img_set.append( asd )
                # print('\t%s' % asd )

        self.root = Tk()
        self.img = Image.open(self.img_set[0])
        self.width, self.height = self.img.size

        self.canvas = Canvas(bg="black")
        self.canvas.focus_set()
        self.canvas.bind("<Key>", self.key1)
        self.canvas.bind("<Button-1>", self.left_click)
        self.canvas.bind("<Motion>", self.motion)
        self.canvas.bind("<MouseWheel>", self.scroll_up)

        self.canvas.pack(expand=YES, fill=BOTH)

        self.canvas.image = ImageTk.PhotoImage(self.img)
        self.image_on_canvas = self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')
        self.rect = self.canvas.create_rectangle(0, 0, 50, 50, outline='red')


        self.root.mainloop()

    def left_click(self, event):

        border = (self.x0, self.y0, self.x1, self.y1)

        new_image = self.img.crop( border )
        self.cur_index += 1
        new_image = new_image.resize((512,512), Image.ANTIALIAS)
        new_image.save( self.dir_root + '2\\{:0>7d}.jpeg'.format(self.cur_index), 'JPEG' )
        self.next_image()
        # print('left', event.x, event.y)

        # self.x0 = event.x - self.rect_size
        # self.x1 = event.x + self.rect_size
        # self.y0 = event.y - self.rect_size
        # self.y1 = event.y + self.rect_size
        #
        # self.canvas.coords(self.rect,self.x0,self.y0,self.x1,self.y1)

    def motion(self, event):
        # print('left', event.x, event.y)

        self.x0 = event.x - self.rect_size
        self.x1 = event.x + self.rect_size
        self.y0 = event.y - self.rect_size
        self.y1 = event.y + self.rect_size

        self.canvas.coords(self.rect,self.x0,self.y0,self.x1,self.y1)


    def scroll_up(self, event):
        print('scroll_up', event.x, event.y, event.delta)

        # if self.event_x != event.x or self.event_y != event.y:
        #     self.event_x = event.x
        #     self.event_y = event.y
        # else:

        if event.delta > 0:
            self.rect_size += 20
        else:
            self.rect_size -= 20
            if self.rect_size < 25:
                self.rect_size = 25

        self.motion(event)



    def next_image(self):
        self.img_index += 1

        if  self.img_index >= len( self.img_set ):
            self.img_index = 0

        self.img = Image.open(self.img_set[self.img_index])
        self.canvas.image = ImageTk.PhotoImage(self.img)
        self.canvas.itemconfig(self.image_on_canvas, image = self.canvas.image )

    def key1(self,event):
        print("pressed", repr(event.char))
        self.next_image()







xz = Xz(  )







