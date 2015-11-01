from flask import Flask,render_template,request
app_lulu = Flask(__name__)
app_lulu.vars={}
@app_lulu.route('/', methods=['GET','POST'])

def index_lulu():
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == "__main__":
    app_lulu.run(debug=True)
