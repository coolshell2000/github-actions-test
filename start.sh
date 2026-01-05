#!/bin/bash
# Start the Flask application with social login features

# Load environment variables
export $(cat .env | xargs)

# Run the application
cd app
python main.py

