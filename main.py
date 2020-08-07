from scrapy import cmdline
import schedule
import time
import os

print('Scheduler initialised')
schedule.every(12).hours.do(lambda: os.system('scrapy crawl soriana'))
print('Next job is set to run at: ' + str(schedule.next_run()))

while True:
    schedule.run_pending()
    time.sleep(1)