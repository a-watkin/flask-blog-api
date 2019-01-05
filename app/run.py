import os
from app import create_app
from database import blog_db

if __name__ == '__main__':
    print(os.environ.get('FLASK_CONFIG', 'development'))

    app = create_app(os.environ.get('FLASK_CONFIG', 'development'))

    app.run()
