from Lagou.game import Game


class HouYi(Game):
    # 子类的init方法会覆盖父类的init 方法, 用super函数解决
    def __init__(self):
        super().__init__(1000, 200)
        self.defense = 50

    def houyi_fight(self, enemy_hp, enemy_power):
        # 设置为多回合制,利用while实现
        count = 1
        while True:

            self.hp = self.hp + self.defense - enemy_power
            # 计算敌人hp
            enemy_hp = enemy_hp - self.power
            # 比较hp

            if self.hp <=0:
                print("我被干掉了")
                break
            elif enemy_hp <= 0:
                print("敌人被干掉了")
                break
            print(f"这是第{count}轮,我的血量{self.hp},敌人的血量{enemy_hp}")
            count+=1
            # 多轮比赛不存在平手
            # else:
            #     raise Exception('平手异常')

if __name__ == '__main__':
    houyi = HouYi()
    houyi.houyi_fight(1000,240)