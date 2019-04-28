class Person(object):

    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name
        self.gun = None
        self.hp = 100

    def anzhuang_zidan(self, dan_jia_temp, zi_dan_temp):
        dan_jia_temp.baocun_zidan(zi_dan_temp)
        
    def anzhuang_zidan(self, gun_temp, dan_jia_temp):
        gun_temp.baocun_danjia(dan_jia_temp)

    def naqiang(self, gun_temp):
        self.gun = gun_temp

    def kou_ban_ji(self, di_ren_temp):
        self.gun.fire(di_ren_temp)
        
        

class Gun(object):
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name
        self.dan_jia = None
        
    def baocun_danjia(self, dan_jia_temp):
        self.dan_jia = dan_jia_temp
        
    def fire(self, diren):
        zidan_temp = self.danjia.tanchu_zidan()
        

class Danjia(object):
    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num
        self.zidan_list = []

    def baocun_zidan(self,zi_dan_temp):
        self.zidan_list.append(zi_dan_temp)
        

class Zidan(object):
    def __init__(self, sha_shang_li):
        super(Zidan, self).__init__()
        self.sha_shang_li = sha_shang_li




def main():

    

    #1.创建老王对象
    laowang = Person("老王")

    #2.创建枪对象
    ak47 = Gun("AK47")

    #3.创建弹夹对象
    danjia = Danjia(20)

    #4.子弹
    zidan = Zidan(10)

    #5.安装子弹
    laowang.anzhuang_zidan(danjia, zidan)

    #6.安装弹夹
    laowang.anzhuang_danjia(ak47, danjia)

    #7.拿枪
    laowang.naqiang(ak47)

    #8.创建敌人
    diren = Person("老宋")

    #9.老王开枪射击
    laowang.kou_ban_ji(diren)



if __name__=='__main__':

    main()

