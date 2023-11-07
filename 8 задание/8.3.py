class student():
    name = None
    surname =None
    def pervbuk(self):
        print(self.name[0].upper(),self.surname[0].upper())
one = student()
one.name = 'саня'
one.surname = 'санин'
one.pervbuk()