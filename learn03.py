#购买一栋房子，把家具放进去，打印出面积
#创建房子的类
class Home:
    def __init__(self,new_area,new_info,new_address):
        self.area = new_area
        self.info = new_info
        self.address = new_address
        self.left_area = new_area
        self.contact_item = []
    
    def __str__(self):
       msg = "房子的面积是：%d,剩余面积是：%d,户型是：%s,地址是：%s"%(self.area,self.left_area,self.info,self.address)
       msg += "当前房子的家具有%s"%(str(self.contact_item))
       return msg

    def add_item(self,item):
        self.contact_item.append(item.get_name())
        self.left_area -=item.get_area()
        #self.contact_item.append(item.name)
        #self.left_area -=item.area
    def __del__(self):
        print("...结束对象，释放空间...")


#创建家具床的类
class Bed:
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area
    
    def __str__(self):
        return "%s面积是%d平方"%(self.name,self.area)
    def get_area(self):
        return self.area
    def get_name(self):
        return self.name


#创建对象
jia = Home(120,"三房一厅","北京市 朝阳区 长安街 666号")
print(jia)
bed_1 = Bed("席梦思",4)
print(bed_1)
jia.add_item(bed_1)#这里调用的对象指向home的函数add_item的参数里
print(jia)
bed_2 = Bed("三人床",6)
jia.add_item(bed_2)
print(jia)