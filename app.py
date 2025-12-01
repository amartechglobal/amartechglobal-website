from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    
    # Ab database save nahi kar rahe
    print("Form Submitted:", name, email, message)  # Console par dikhega
    
    return redirect("/success")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/admin")
def admin():
    return "Database remove hone ke baad admin panel available nahi hai."

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
