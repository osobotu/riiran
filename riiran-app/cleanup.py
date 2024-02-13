from datetime import datetime, timedelta
import os
from apscheduler.schedulers.background import BackgroundScheduler
from flask import current_app
# from riiran import app

CLEANUP_INTERVAL = 1
CLEANUP_THRESHOLD_DAYS = 5

def cleanup_task(app):
    """
    Cleanup task to remove older files from the uploads folder.
    """
    now = datetime.now()
    threshold_date = now - timedelta(minutes=CLEANUP_THRESHOLD_DAYS)

    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))

        if modified_time < threshold_date:
            os.remove(file_path)
    print('clean_up done')

def start_cleanup_scheduler(app):
    """
    Start the scheduler for periodic cleanup.
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(cleanup_task, 'interval', hours=CLEANUP_INTERVAL, id='cleanup_task', args=[app])
    scheduler.start()
    print('clean_up scheduled')