from datetime import datetime
import time

while (1) :
	now = datetime.now()
	print ('►' + str(now.hour).zfill(2) + ':' + str(now.minute).zfill(2) + ':' + str(now.second).zfill(2) + '◄', end='\r')
	time.sleep(0.5)