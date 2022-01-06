from flask import Flask, render_template, send_file
app = Flask('app')

@app.route('/')
def homePage():
  return render_template("index.html")
  
@app.route('/favicon.ico')
def favicon():
  return send_file("static/assets/favicon/logo.png")

app.run(host='0.0.0.0', port=8080, debug=True)
