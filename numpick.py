import random

up = input("請輸入猜數字上限")
up = int(up)
r = random.randint(1, up)
low = 1
i = 1
while True:
	print("第", i, "次猜題！")
	print("數字範圍為", low, "<正解<", up)
	x = input("請輸入數字")
	x = int(x)
	i += 1
	if x == r:
		print("恭喜正確！")
		break
	elif x > r:
		print(x, "太大")
		up = x
	elif x < r:
		print(x, "太小")
		low = x
	