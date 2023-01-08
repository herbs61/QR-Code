from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/index',methods=['GET','POST'])
def index():
    if request.method=='POST':
        # Handle POST Request here
        return index('index.html')
    return index('index.html')

@app.route('/profile',methods=['GET','POST'])
def profile():
    if request.method=='POST':
        # Handle POST Request here
        return profile('profile.html')
    return profile('profile.html')

@app.route('/code',methods=['GET','POST'])
def QRcode():
    if request.method=='POST':
        # Handle POST Request here
        return QRcode('QRcode.html')
    return QRcode('QRcode.html')







if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
    