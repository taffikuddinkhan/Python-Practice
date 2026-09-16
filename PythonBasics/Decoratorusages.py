class Student:
    def __init__(self,math,phy,sci):
        self.math=math
        self.phy=phy
        self.sci=sci

    # def calcpercentage(self):  #calculate percentage and then assign that in to percentage variable/attribute
    #     self.percentage=str((self.math+self.sci+self.phy)/3)

    @property  #this will now convert the percentage method to attribute type
    def percentage(self):
        return str((self.math+self.sci+self.phy)/3)


stu1 = Student(11,23,42)
print(stu1.percentage)

stu1.phy=86
# print(stu1.phy)
# stu1.calcpercentage()
print(stu1.percentage)  #now the percentage will be treated as attribute / variable

