from flask import Flask, jsonify
import psycopg2
from psycopg2 import OperationalError
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS

app = Flask(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return conn
    except OperationalError as e:
        print(f"Error: {e}")
        return None

@app.route('/happiness', methods=['GET'])
def get_happiness_data():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500

    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM world_happiness")
        result = cur.fetchall()
        column_names = [desc[0] for desc in cur.description]
        data = [dict(zip(column_names, row)) for row in result]
        cur.close()
    except Exception as e:
        return jsonify({"error": f"Error fetching data: {e}"}), 500
    finally:
        conn.close()

    return jsonify(data)

@app.route('/tables', methods=['GET'])
def get_tables():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500

    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """)
        result = cur.fetchall()
        tables = [row[0] for row in result]
        cur.close()
    except Exception as e:
        return jsonify({"error": f"Error fetching table names: {e}"}), 500
    finally:
        conn.close()

    return jsonify(tables)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
