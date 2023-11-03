class Person:
    def __init__(self,fname,lname,blood):
        self.fname = fname
        self.lname = lname
        self.blood = blood

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self,fname):
        self.__fname = fname.strip().title()

    @property
    # * Getter
    def blood(self):
        return self.__blood

    # * Setter
    @blood.setter
    def blood(self,blood):
        if blood.upper() in ["A","B","C","O","AB"]:
            self.__blood = blood.upper()
        else:
            raise ValueError("Type Error")
    
    def __str__(self):
        return "{!r} {}, blood group: {}".format(self.fname,self.lname,self.blood)

if __name__ == '__main__':
    p1 = Person(" JoJo ","Start","O")
    print(p1)
    p1.blood = "B"
    print(p1)
