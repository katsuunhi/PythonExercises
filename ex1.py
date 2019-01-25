# 一、猜数字
# 经典的猜数字游戏，几乎所有人学编程时都会做。
# 功能描述：随机选择一个三位以内的数字作为答案。用户输入一个数字，程序会提示大了或是小了，直到用户猜中
	
import random
digit = int(input("input a digit:"))
answer = random.randint(0,100)
while digit != answer:
	if answer > digit:
		print(answer, " too big")
	else:
		print(answer, " too small")
	answer = random.randint(0,100)
print("you are right! it is ", digit)
