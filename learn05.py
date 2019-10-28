#定义人的类
class Dog():
    def print_self(self):
         print("大家好，我是XXX,希望以后多多关照")

class Xiaotq(Dog):
    def __init__(self,name):
        self.name = name
        print("大家安静下，听我说我叫%s"%self.name)
    def print_self(self):
        print("我是你们的老大，听我的")

def introduce(temp):
    temp.print_self()

dog_1 = Dog()

A = introduce(dog_1)

print(A)
dog_2 = Xiaotq("啸天神犬")
B = introduce(dog_2)
print(B)




