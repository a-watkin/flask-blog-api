#!/usr/bin/env python
import os
from app import create_app

if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_CONFIG', 'development'))
    print(app)
    app.run()
