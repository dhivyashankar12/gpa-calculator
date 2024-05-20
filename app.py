import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "66b58fafa6a470f26fd2adc9de14cef2"

''' PWA Stuff '''
# only trigger SSLify if the app is running on Heroku
if 'DYNO' in os.environ: 
	from flask_sslify import SSLify
	sslify = SSLify(app)

@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('sw.js')

@app.route('/offline.html')
def offline():
	return app.send_static_file('offline.html')

''' Routes/views ''' 

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def index():
	no_of_subjects = 14
	if request.method == 'POST':
		credits = [ int (i) for i in request.form.getlist('credits[]') ]
		grades = request.form.getlist('grades[]')
		FinalGPA = gpa_calc(no_of_subjects, credits, grades)
		return render_template('index.html', no_of_subjects=no_of_subjects, FinalGPA=FinalGPA)
	return render_template('index.html', no_of_subjects=no_of_subjects)

''' Utility functions '''

def gpa_calc(no_of_subjects, credits, grades):
	FinalGPA = 0
	grade_dict = { 'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C': 5, 'P': 4 }
	grade_pts = [ grade_dict[grade] for grade in grades ]
	for c, gp in zip(credits, grade_pts):
		FinalGPA = FinalGPA + float(c*gp)
	return FinalGPA/sum(credits)


if __name__=='__main__': 
    app.run(debug = False) 
