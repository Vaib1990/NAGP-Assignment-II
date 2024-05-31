# This Flask application connects to a PostgreSQL database to fetch and return all records from the
# 'items' table as a JSON response. Database credentials are securely obtained from environment
# variables, which are expected to be set by Kubernetes secrets and config maps. This ensures that
# sensitive information is not hard-coded into the application. The '/items' endpoint handles GET
# requests by connecting to the database, executing a query to retrieve all records, and returning
# the results as a JSON array. If an error occurs during this process, an error message with a 500
# status code is returned.

from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Get DB credentials from environment (injected by Kubernetes secrets and config Map)
DB_HOST = os.environ.get('POSTGRES_HOST') 
DB_NAME = os.environ.get('POSTGRES_DB')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')

@app.route('/items', methods=['GET'])
def get_items():
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cur = conn.cursor()
        
        # Execute SQL query to fetch all records from the 'items' table
        cur.execute("SELECT * FROM items") 
        rows = cur.fetchall()  # Fetch all results from the executed query
        
        # Close the database connection
        conn.close()
        
        # Return the results as a JSON response
        return jsonify(rows) 
    except Exception as e:
         # Return an error message and a 500 status code if an exception occurs
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application on all available IP addresses on port 5000
    app.run(host='0.0.0.0', port=5000)
