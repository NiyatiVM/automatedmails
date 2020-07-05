from apscheduler.schedulers.blocking import BlockingScheduler
from mailthem import mailthecoders
scheduler = BlockingScheduler()
scheduler.add_job(mailthecoders,"interval",hours=24,start_date='2020-07-06 06:00:00')
scheduler.start()