from flask import Flask, render_template, request, session
import sqlite3
import datetime
from user_agents import parse

app = Flask(__name__)
app.secret_key = 'carbon_countdown_secret_key_2024'

def get_db_connection():
    conn = sqlite3.connect('analytics.db')
    conn.row_factory = sqlite3.Row
    return conn

def track_page_view(page):
    if 'user_id' not in session:
        return
    
    conn = get_db_connection()
    
    # Get user agent info
    user_agent = parse(request.headers.get('User-Agent'))
    browser = user_agent.browser.family
    os = user_agent.os.family
    
    # Get or create device
    device = conn.execute(
        'SELECT device_id FROM Devices WHERE browser = ? AND os = ?',
        (browser, os)
    ).fetchone()
    
    if device is None:
        conn.execute(
            'INSERT INTO Devices (browser, os) VALUES (?, ?)',
            (browser, os)
        )
        device_id = conn.lastrowid
    else:
        device_id = device['device_id']
    
    # Record page view
    conn.execute(
        'INSERT INTO PageViews (user_id, device_id, page, view_time) VALUES (?, ?, ?, ?)',
        (session['user_id'], device_id, page, datetime.datetime.now())
    )
    
    conn.commit()
    conn.close()

def create_user_session():
    if 'user_id' not in session:
        conn = get_db_connection()
        ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', request.environ['REMOTE_ADDR'])
        
        # Check if user already exists
        user = conn.execute(
            'SELECT user_id FROM Users WHERE ip_address = ?',
            (ip_address,)
        ).fetchone()
        
        if user is None:
            conn.execute(
                'INSERT INTO Users (ip_address, session_start) VALUES (?, ?)',
                (ip_address, datetime.datetime.now())
            )
            session['user_id'] = conn.lastrowid
        else:
            session['user_id'] = user['user_id']
        
        conn.commit()
        conn.close()

@app.before_request
def before_request():
    create_user_session()

@app.route('/')
def index():
    track_page_view('index')
    return render_template('index.html')

@app.route('/data')
def data():
    track_page_view('data')
    return render_template('data.html')

@app.route('/help')
def help_page():
    track_page_view('help')
    return render_template('help.html')

@app.route('/about')
def about():
    track_page_view('about')
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)