# a = {}
# b = a.fromkeys(("a", "b","c"),1)
# print(b)

# a = "tom"
# b = 2
# lili = [1, 23, "a"]
# dict = {"food":'apple','drink':'water'}
# print (f"i'm {a} i'm {b}")
# print ("i'm {} i'm {}".format(a,b))
# print(f"you're {lili}")
# # 列表插值
# print(f"you're {lili[2]}")
# print("you're {2}".format(*lili))
# # 字典插值
# print('i like eat {food}, drink {drink}'.format(**dict))
# print(f'i like eat {dict["food"]}, drink {dict["drink"]}')
import os
#
# print(os.listdir('..'))


import yaml

# 输出列表
# print(yaml.load('''
# - a
# - b
# - c
# ''', Loader=yaml.FullLoader))
# # 输出字典
# print(yaml.load('''
# a: 1
# ''', Loader=yaml.FullLoader))
# 读取yaml文件
# print(yaml.load(open("demo.yml"), Loader=yaml.FullLoader))

print(yaml.dump([1, 2, 3, 4, 5]))
print(yaml.dump({"a": 1, "b": [1, 2, 3, 4, 5]}))
with open("demo.yml","w+")as f:
    yaml.dump({"a": 1, "b": [1, 2, 3, 4, 5]},stream=f)