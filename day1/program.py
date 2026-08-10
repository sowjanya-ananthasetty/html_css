class father:
    def show(self):
        print("father class")
    def property(self):
        print("father property")
class mother:
    def show(self):
        print("mother class")
    def property(self):
        print("mother property")
class son(father,mother):
    def show1(self):
        print("son class")
    def property1(self):
        print("son property")
c1=son()
c1.show
c1.property