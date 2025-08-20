from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.url_map.strict_slashes = False   # accept /login and /login/

# demo creds
SECRET_USERNAME = "admin"
SECRET_PASSWORD = "admin123"

@app.route('/')
def home():
    return render_template('login.html')

# handle both GET (direct URL) and POST (form submit)
@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # user opened /login directly -> send them to the form
        return redirect(url_for('home'))

    username = (request.form.get('username') or '').strip()
    password = (request.form.get('password') or '').strip()
    success = (username == SECRET_USERNAME and password == SECRET_PASSWORD)
    return render_template('result.html', success=success, user=username)

if __name__ == '__main__':
    app.run(debug=True)
