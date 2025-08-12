from flask import *
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        f=request.files['files']
        f.save(f.filename)
        return render_template('ack.html',name=f.filename)

if __name__  =='__main__':
    app.run(debug=True)
