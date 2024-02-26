from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # Redirect to the '/profile' route
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    return render_template('page.html')

if __name__ == '__main__':
    app.run(debug=True)

