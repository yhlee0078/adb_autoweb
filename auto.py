import time
import random
import sys

#from utils import check_adb
from utils import *

#from utils import start_log, end_log
from web import open_web, flush_web
from config import RESOLUTION, LOGGING_TIME, START_IDX, TRIAL

import logging
import coloredlogs
import pprint as pp
#os.environ['DISPLAY'] = ':0'

if len(sys.argv)!=3:
	print("usage : python auto.py timestotest interval")
	print("ex) python auto.py 200 1")
	sys.exit()

times = int(sys.argv[1])
interval = float(sys.argv[2])
logger = logging.getLogger(__name__)
coloredlogs.install(level=logging.INFO)

def start_test(idx, link, interval):

	logger.info("===============================")
	logger.info("{}: {}".format(idx, link))
	logger.info("===============================")

	status = open_web(link, interval)


orig_links = get_links("web_link.txt")
#logger.debug(pp.pformat(orig_links))
print(orig_links[0][1])

thelinks = []

for i in  range (len(orig_links)):
	thelinks.append(orig_links[i][1][1::])

#print(thelinks)


check_adb()
close_all_app()
'''
close_all_alogger.info("It starts after 5 seconds. "
                "Please move the mouse cursor to the Optis-S screen")
'''
time.sleep(1)
#push_clear()

#print(type(orig_links))

#40????
for idx in range(0, times):
	#flush_web()
	#links = orig_links
	res = random.shuffle(thelinks)
	#print(thelinks)
	#print(res)
	start_test(idx, thelinks[0], interval)

close_all_app()
