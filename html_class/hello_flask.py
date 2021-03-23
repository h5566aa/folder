from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template, request
app = Flask(__name__)
@app.route('/login')
def login():
    
    return render_template('87.html')

@app.route('/aaa')
def aaa():
    data = request.args
    str_s="帳號:"+str(data['fname'])
    str_l="密碼:"+str(data['lname'])
    return str_s+'<br>'+str_l


if __name__ == '__main__':
    app.debug = True
    app.run()