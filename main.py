from flask import Flask, request, render_template, url_for
import sqlite3

app = Flask(__name__)
def init_db():
    conn = sqlite3.connect('emails.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']
        if email:
            try:
                conn = sqlite3.connect('emails.sqlite')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO emails (email) VALUES (?)", (email,))
                conn.commit()
                conn.close()
                return render_template('index.html', message='Email saved successfully!')
            except sqlite3.IntegrityError:
                return render_template('index.html', message='This email is already registered.')
        else:
            return render_template('index.html', message='Please enter a valid email')

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

def init_db2():
    conn = sqlite3.connect('services_data.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            text TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db2()

@app.route('/services', methods=['GET', 'POST'])
def services():
    if request.method == 'POST':
        email = request.form['email']
        text = request.form['text']
        if email and text:
            try:
                conn = sqlite3.connect('services_data.sqlite')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO services (email, text) VALUES (?, ?)", (email, text))
                conn.commit()
                conn.close()
                return render_template('services.html', message='Record saved successfully!')
            except sqlite3.Error as e:
                return render_template('services.html', message=f'An error occurred: {e}')
        else:
            return render_template('services.html', message='Please enter valid information.')
    return render_template('services.html')


@app.route('/departments')
def departments():
    return render_template('departments.html')

if __name__ == '__main__':
    app.run(debug=True)