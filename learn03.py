class Game():
    #类属性
    num = 0
    def __init__(self):
        #实例属性
        self.name ="laowang"
    #类方法
    @classmethod
    def add_num(cls):
        cls.num = 100
    #静态方法
    @staticmethod
    def print_menu():
        print("=============")
        print("穿越火线")
        print("============")

game = Game()
Game.add_num()#改写类属性 
print(Game.num)
print(Game.print_menu())#通过类去调用静态方法
print(game.print_menu())#通过实例对象调用静态方法