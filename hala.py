from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session 
import pyrebase

count = 0

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


config={
	"apiKey": "AIzaSyC2MtYElQPx9k05stxcwCf6Ex3XAk6Xh18",
	"authDomain": "authentication-81c17.firebaseapp.com",
	"projectId": "authentication-81c17",
	"storageBucket": "authentication-81c17.appspot.com",
	"messagingSenderId": "687020370548",
	"appId": "1:687020370548:web:cefd5dcdac2fd18d1bbf21",
	"measurementId": "G-WP2CGR3024",
	"databaseURL": "https://authentication-81c17-default-rtdb.europe-west1.firebasedatabase.app/"
  }


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db =firebase.database()


@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method=='POST':
		return redirect(url_for("signup"))
	return render_template("main.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method=='POST':
		email = request.form['email']
		password = request.form['password']
		username= request.form['username']
		users={"email":email, "username":username}
		try: 
			session['user']=auth.create_user_with_email_and_password(email,password)
			user_id = session['user']['localId']
			session.modified = True 
			db.child("users").child(user_id).set(users)
			print(users['username'])
			return redirect(url_for("home"))
		except Exception as e:
			error="Error, try again!!"
			print(e)
			return render_template("signup.html", error=error)
		

	return render_template("signup.html")



@app.route('/signin', methods=['GET', 'POST'])
def signin():
	if request.method=='POST':
		email = request.form['email']
		password = request.form['password']
		try: 
			session['user']=auth.sign_in_with_email_and_password(email,password)
			user_id = session['user']['localId']
			return redirect(url_for("home"))
		except Exception as e:
			error="Error, try again!!"
			print(e)
			return render_template("signin.html", error=error)


	return render_template("signin.html")



@app.route('/quiz1', methods=['GET', 'POST'])
def quiz1():
	return render_template("quiz1.html")

@app.route('/quiz2', methods=['GET', 'POST'])
def quiz2():
	return render_template("quiz2.html")

@app.route('/quiz3', methods=['GET', 'POST'])
def quiz3():
	return render_template("quiz3.html")

@app.route('/home', methods=['GET', 'POST'])
def home():
	user_id = session['user']['localId']
	user=(db.child("users").child(user_id).get().val())
	return render_template("home.html", user=user['username'])

@app.route('/question1', methods=['GET', 'POST'])
def question1():
	return render_template("question1.html")

@app.route('/question2', methods=['GET', 'POST'])
def question2():
	return render_template("question2.html")

@app.route('/question3', methods=['GET', 'POST'])
def question3():
	return render_template("question3.html")

@app.route('/question4', methods=['GET', 'POST'])
def question4():
	return render_template("question4.html")


@app.route('/question5', methods=['GET', 'POST'])
def question5():
	return render_template("question5.html")

@app.route('/question6', methods=['GET', 'POST'])
def question6():
	return render_template("question6.html")


@app.route('/question7', methods=['GET', 'POST'])
def question7():
	return render_template("question7.html")


@app.route('/question8', methods=['GET', 'POST'])
def question8():
	return render_template("question8.html")


@app.route('/question9', methods=['GET', 'POST'])
def question9():
	return render_template("question9.html")


@app.route('/Q1', methods=['GET', 'POST'])
def Q1():
	return render_template("Q1.html")


@app.route('/Q2', methods=['GET', 'POST'])
def Q2():
	return render_template("Q2.html")


@app.route('/Q3', methods=['GET', 'POST'])
def Q3():
	return render_template("Q3.html")


@app.route('/Q4', methods=['GET', 'POST'])
def Q4():
	return render_template("Q4.html")

@app.route('/Q5', methods=['GET', 'POST'])
def Q5():
	return render_template("Q5.html")

@app.route('/Q6', methods=['GET', 'POST'])
def Q6():
	return render_template("Q6.html")

@app.route('/Q7', methods=['GET', 'POST'])
def Q7():
	return render_template("Q7.html")


@app.route('/Q8', methods=['GET', 'POST'])
def Q8():
	return render_template("Q8.html")

@app.route('/Q9', methods=['GET', 'POST'])
def Q9():
	return render_template("Q9.html")

@app.route('/Qu1', methods=['GET', 'POST'])
def Qu1():
	return render_template("Qu1.html")

@app.route('/Qu2', methods=['GET', 'POST'])
def Qu2():
	return render_template("Qu2.html")

@app.route('/Qu3', methods=['GET', 'POST'])
def Qu3():
	return render_template("Qu3.html")

@app.route('/Qu4', methods=['GET', 'POST'])
def Qu4():
	return render_template("Qu4.html")

@app.route('/Qu5', methods=['GET', 'POST'])
def Qu5():
	return render_template("Qu5.html")

@app.route('/Qu6', methods=['GET', 'POST'])
def Qu6():
	return render_template("Qu6.html")

@app.route('/Qu7', methods=['GET', 'POST'])
def Qu7():
	return render_template("Qu7.html")

@app.route('/Qu8', methods=['GET', 'POST'])
def Qu8():
	return render_template("Qu8.html")

@app.route('/Qu9', methods=['GET', 'POST'])
def Qu9():
	return render_template("Qu9.html")


@app.route('/correct', methods=['GET', 'POST'])
def correct():
	return render_template("correct.html")

@app.route('/wrong', methods=['GET', 'POST'])
def wrong():
	return render_template("wrong.html")
@app.route('/wrong1', methods=['GET', 'POST'])
def wrong1():
	return render_template("wrong1.html")

@app.route('/correct1', methods=['GET', 'POST'])
def correct1():
	return render_template("correct1.html")

@app.route('/signout', methods=['GET', 'POST'])
def signout():
	if request.method=="POST":
		session['user']=None
		auth.current_user = None
		print("the user is signed out")
		return redirect((url_for('signin')))
	return render_template("signout.html")


if __name__ == '__main__':
	app.run(debug=True)

