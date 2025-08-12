from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('login.html')
@app.route('/login',methods=['POST'])
def login():
    uname=request.form['uname']
    passwrd=request.form['pass']
    if uname=="hai" and passwrd=='abcd':
        return 'welcome'


if __name__ =='__main__':
    app.run(debug=True)
