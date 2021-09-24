from flask import Flask


import admin,reader,author,editor,index

app = Flask(__name__)


admin.init_app(app)
reader.init_app(app)
author.init_app(app)
editor.init_app(app)
index.init_app(app)

print(app.url_map)
app.run(host='0.0.0.0',port=8000)
