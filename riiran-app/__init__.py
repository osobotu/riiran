import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'riiran.sqlite'),
        UPLOAD_FOLDER = 'riiran-app/static/uploads',
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

    from . import cleanup
    cleanup.start_cleanup_scheduler(app)

    
    return app

app = create_app()





