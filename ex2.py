# 二、FizzBuzz

# 功能描述：
# 遍历并打印0到100，
# 如果数字能被3整除，显示Fizz；
# 如果数字能被5整除，显示Buzz；
# 如果能同时被3和5整除，就显示FizzBuzz。
# 结果应该类似：0,1,2，Fizz，4，Buzz，6……14，FizzBuzz，16……

for i in range(0, 101):
	if i%3 == 0 and i%5 != 0:
		print("Fizz", end = " ")
	if i%5 == 0 and i%3 != 0:
		print("Buzz", end = " ")
	if i%3 == 0 and i%5 == 0:
		print("FizzBuzz", end = " ")
	if i%3 != 0 and i%5 != 0:
		print(i, end = " ")