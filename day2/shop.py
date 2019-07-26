class Shop:
    name = None
    sel_item = 0

    def __init__(self, name, sel_item):
        self.name = name
        self.sel_item = sel_item

        Shop.sel_item += sel_item

    def sel(self, sel_item):
        self.sel_item += sel_item
        Shop.sel_item += sel_item

    def get_stat(self):
        print(Shop.sel_item)

    def  get_name(self):
        print(self.name)

    def  get_self_stat(self):
        print(self.sel_item)




mag_1 = Shop('У дома', 5)
mag_2 = Shop('все по 10 ', 10)



mag_1.sel(5)

mag_2.sel( 5 )

mag_1.get_name()
mag_1.get_self_stat()

mag_2.get_name()
mag_2.get_self_stat()

mag_1.get_stat()