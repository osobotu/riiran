import os

from flask import Flask 
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from flask import current_app


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'riiran.sqlite'),
        UPLOAD_FOLDER = 'riiran/static/uploads',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass 

    # # make upload directory
    # try:
    #     os.makedirs(os.path.join(app.instance_path, UPLOAD_FOLDER))
    # except FileExistsError:
    #     pass
    

    @app.route('/health')
    def health():
        return 'Flask is running successfully'
    
    from . import index
    app.register_blueprint(index.bp)

    def cleanup_task():
        """
        Cleanup task to remove older files from the uploads folder.
        """
        now = datetime.now()
        threshold_date = now - timedelta(days=CLEANUP_THRESHOLD_DAYS)
    
        for filename in os.listdir(app.config['UPLOAD_FOLDER']):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))

            if modified_time < threshold_date:
                os.remove(file_path)
        print('clean_up done')

    def start_cleanup_scheduler():
        """
        Start the scheduler for periodic cleanup.
        """
        scheduler = BackgroundScheduler()
        scheduler.add_job(cleanup_task,  'interval', hours=CLEANUP_INTERVAL, id='cleanup_task')
        scheduler.start()
        print('clean_up scheduled')
   
    start_cleanup_scheduler()
    
    return app


CLEANUP_INTERVAL = 1
CLEANUP_THRESHOLD_DAYS = 1

