# import os
# from flask import Flask
# import cleanup
# import index

# app = Flask(__name__, instance_relative_config=True)

# app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'riiran.sqlite'),
#         UPLOAD_FOLDER = 'riiran/static/uploads',
#     )

# # if test_config is None:
# #     app.config.from_pyfile('config.py', silent=True)
# # else:
# #     app.config.from_mapping(test_config)
# #     try:
# #         os.makedirs(app.instance_path)
# #     except OSError:
# #         pass 

#     # # make upload directory
#     # try:
#     #     os.makedirs(os.path.join(app.instance_path, UPLOAD_FOLDER))
#     # except FileExistsError:
#     #     pass
    

# @app.route('/health')
# def health():
#     return 'Flask is running successfully'


# app.register_blueprint(index.bp)


# cleanup.start_cleanup_scheduler(app)

# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5001))
#     app.run(debug=True, host='0.0.0.0', port=port)



