class Game:

    def __init__(self,hp,power):
        # 定义我的状态初始值
        self.power = power
        self.hp = hp

    def fight(self, enemy_power, enemy_hp):
        # 计算我的hp
        hp = self.hp - enemy_power
        # 计算敌人hp
        enemy_hp = enemy_hp - self.power
        # 比较hp
        if hp > enemy_hp:
            print("w我赢了")
        elif hp < enemy_hp:
            print("我输了")
        else:
            print("平手")


if __name__ == '__main__':
    game = Game(hp=1000, power=300)
    game.fight(enemy_hp=1000, enemy_power=200)
