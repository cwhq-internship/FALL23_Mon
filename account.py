import sqlite3
from hashlib import sha256

# Function to create a database and table
def create_database():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Function to add a new user to the database
def add_user(username, password):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # Hash the password before storing
    hashed_password = sha256(password.encode()).hexdigest()

    # Insert the user into the database
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))

    conn.commit()
    conn.close()

# Function to authenticate a user
def authenticate_user(username, password):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # Hash the provided password for comparison
    hashed_password = sha256(password.encode()).hexdigest()

    # Check if the username and hashed password match
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hashed_password))
    user = cursor.fetchone()

    conn.close()

    return user is not None

# Create the database and table
create_database()

# Add a new user
add_user('user1', 'password1')

# Authenticate the user
username_to_check = 'user1'
password_to_check = 'password1'
if authenticate_user(username_to_check, password_to_check):
    print(f'User {username_to_check} is authenticated.')
else:
    print('Invalid username or password.')
