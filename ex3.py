# 三、猜数字的AI

# 和猜数字一样，不过这次是设计一个能猜数字的AI。

# 功能描述：用户输入一个单位以内的数字，AI要用最少的次数猜中，并且显示出猜的次数和数字。

import random

digit = int(input("input a digit:"))
times = 0
answer = 100//2
middle = 100//4
times = times + 1

while digit != answer:
	if answer < digit:
		print(answer, " too small")
		answer = answer + middle
		times = times + 1
	if answer > digit:
		print(answer, " too big")
		answer = answer - middle
		times = times + 1
	middle = middle//2
	if middle == 0:
		middle = 1

print(answer, " is right! you have tried for ", times, " times!")
