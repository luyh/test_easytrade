import easytrader

# 导入华宝油气网格表

f = open("hbyq.txt")             # 返回一个文件对象

lines = f.readlines() #读取全部内容
f.close()

hbyq = []

for i in range(len(lines)):
    hbyq.append((float(lines[i][:-1])))

print(hbyq)


# 设置网格交易量
amount = 300

