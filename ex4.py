# 四、整点报时

# 老式挂钟会在整点的报时，响铃的次数和时间相等。我们设计一个在电脑上运行的报时器。

# 功能描述：运行后，在每一个整点长响一声，半个整点短响两声。实现睡眠模式，晚上十二点到早上六点不响铃。

import time
import winsound

running = True

def long_Beep():
#	music = "music.mp3"
#	winsound.PlaySound(music, winsound.SND_ALIAS)
	winsound.Beep(370, 4000)
def short_Beep():
	winsound.Beep(370, 2000)

	
while running:

	t = time.localtime()
	# fomat = "%H %M"
	# now = time.strftime(fomat, t).split(' ')
	# hour = int(now[0])
	# minute = int(now[1])
	hour = t.tm_hour
	minute = t.tm_min
	second = t.tm_sec
	if hour >= 6 and minute == 0:
		long_Beep()
		time.sleep(60 - second)
	if hour >= 6 and minute == 30:
		short_Beep()
		short_Beep()
		time.sleep(60 - second)
	if hour == 22 and minute == 32:
		long_Beep()
		short_Beep()
		time.sleep(60 - second)
	




