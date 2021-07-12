from flask import Flask, render_template, url_for

# gets the name of the file so Flask knows it's name
app = Flask(__name__)

# tells you the URL method below is related to
@app.route("/")
#@app.route("/home")
def home():
  return render_template('home.html', subtitle='Home Page', text='Welcome to my homepage!')


@app.route("/about")
def about():
  return render_template('about.html', subtitle='About Page', text='Learn more about me!')
  

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')