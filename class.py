# def getDetail(name, sec, roll, Social, English):
#     return name, sec, roll, Social, English

# def avgmarks(Social,English):
#     return Social + English
    

# def printDetail(name, sec, roll):
#     print(name)
#     print(roll)
#     print(sec)
    


# print(getDetail('lithi', 'b', 55, 98, 56 ))
# print(avgmarks(98, 56))
# printDetail('lithi', 'b', 55)


# print(getDetail('loge', 'b', 55, 98, 56))
# print(avgmarks(98, 56))
# printDetail('lithi', 'b', 55)
class Student:

    def __init__(self,name,sec,roll, sem1, sem2):
        self.name = name
        self.roll = roll
        self.sec = sec
        self.sem1 = sem1
        self.sem2 = sem2

    def avgMarks(self):
        return int(self.sem1) + int(self.sem2)
    
    def printDetails(self):
        print("Name : ", self.name)
        print("sec : ", self.sec)
        print("roll : ", self.roll)


std1 = Student('lithi', 'b', 55, 98, 56)
print(std1.avgMarks())
std1.printDetails()

std2 = Student('Lokesh', 'a', 55, 98, 56)
print(std2.avgMarks())
std2.printDetails()






