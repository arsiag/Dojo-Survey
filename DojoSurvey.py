from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def process_survey():
   
   thisname = request.form['name']
   thisloc = request.form['location']
   thislang = request.form['lang']
   thiscmnt = request.form['comment']
   print "Dojo Survey results:"
   print "Name: " + thisname
   print "Loca: " + thisloc
   print "Lang: " + thislang
   print "Cmnt: " + thiscmnt
   return render_template("results.html", name=thisname, location=thisloc, lang=thislang, comment=thiscmnt)
   #return redirect('/')
   
app.run(debug=True) # run our server