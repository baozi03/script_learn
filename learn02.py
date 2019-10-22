

#烤地瓜
#cookedLevel : 这是数字；0~3表示还是生的，超过3表示半生不熟，超过5表示已经烤好了，超过8表示已经烤成木炭了！我们的地瓜开始时时生的
#cookedString : 这是字符串；描述地瓜的生熟程度
#condiments : 这是地瓜的配料列表，比如番茄酱、芥末酱等
#conding = utf-8

#创建一个类
class Sweetpot:
    #初始化配置
    def __init__(self):
        self.cookedLevel = 0#默认的程度
        self.cookedstring = "生的"
        self.condiments = []

    def __str__(self):
        return "烤地瓜的程度：%d(%s)%s"%(self.cookedLevel,self.cookedstring,str(self.condiments))
    def cook(self,time):
        self.cookedLevel += time
        if self.cookedLevel >= 8:
            self.cookedstring = "烤焦啦"
        elif self.cookedLevel >= 5:
            self.cookedstring = "烤熟了"
        elif self.cookedLevel >= 3:
            self.cookedstring = "半生不熟"
        else:
            self.cookedstring = "生的"

    def addcondiments(self,item):
        self.condiments.append(item)
#创建对象

di_gua = Sweetpot()
di_gua.cook(1)
di_gua.addcondiments("花生油")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addcondiments("孜然")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addcondiments("芥末")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)