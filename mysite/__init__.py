from flask import Flask
import sass

app = Flask(__name__)
sass.compile(dirname=('mysite/static/sass', 'mysite/static/css'))
app.secret_key = "123456"

import mysite.index