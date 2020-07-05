from apscheduler.schedulers.blocking import BlockingScheduler
from mailthem import mailthecoders
scheduler = BlockingScheduler()
scheduler.add_job(mailthecoders,"interval",hours=3)
scheduler.start()