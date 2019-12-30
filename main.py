from flask import Flask, render_template, request
import pymysql
app = Flask(__name__)

@app.route('/')
def home():
    name="Facebook"
    return render_template("index.html",name_template=name);
@app.route('/db')
def db():
    connection = pymysql.connect(host='localhost',user='root',password='',db='facebook')
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `signup`")
        data = cursor.fetchall()
        for i in data:

            print(i[1]);
        
    return data[1][1]
@app.route('/register')
def register():
    return render_template('signup.html')
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        print("Submitted");
        fname = request.form.get('fname')
        uemail = request.form.get('uemail')
        cpassword = request.form.get('cpassword')
        
        connection = pymysql.connect(host='localhost',user='root',password='',db='facebook')
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO `signup` (`name`, `email`, `password`) VALUES(%s,%s,%s)", (fname, uemail, cpassword))
            connection.commit()
            return "successfulll"
app.run(debug = True);
