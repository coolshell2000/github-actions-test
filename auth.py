from flask_login import UserMixin
import sqlite3
import os
from config import DATABASE_PATH

# User model for Flask-Login
class User(UserMixin):
    def __init__(self, id_, email, name, profile_pic, provider=None, provider_user_id=None):
        self.id = id_
        self.email = email or ''
        self.name = name
        self.profile_pic = profile_pic
        self.provider = provider
        self.provider_user_id = provider_user_id

def get_user(user_id):
    """Retrieve a user from the database by ID."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, email, name, profile_pic, provider, provider_user_id FROM users WHERE id = ?", (user_id,))
    user_data = cursor.fetchone()
    conn.close()

    if user_data:
        return User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5])
    return None

def get_user_by_email(email):
    """Retrieve a user from the database by email."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, email, name, profile_pic, provider, provider_user_id FROM users WHERE email = ?", (email,))
    user_data = cursor.fetchone()
    conn.close()

    if user_data:
        return User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5])
    return None

def get_user_by_provider(provider, provider_user_id):
    """Retrieve a user from the database by provider and provider_user_id."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, email, name, profile_pic, provider, provider_user_id FROM users WHERE provider = ? AND provider_user_id = ?", 
                   (provider, provider_user_id))
    user_data = cursor.fetchone()
    conn.close()

    if user_data:
        return User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5])
    return None

def create_user(email, name, profile_pic, provider=None, provider_user_id=None):
    """Create a new user in the database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (email, name, profile_pic, provider, provider_user_id) VALUES (?, ?, ?, ?, ?)",
                   (email, name, profile_pic, provider, provider_user_id))
    user_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return User(user_id, email or '', name, profile_pic, provider, provider_user_id)

def init_users_table():
    """Initialize the users table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        name TEXT NOT NULL,
        profile_pic TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        provider TEXT DEFAULT 'local',
        provider_user_id TEXT,
        UNIQUE(provider, provider_user_id)
    )""")
    conn.commit()
    conn.close()
