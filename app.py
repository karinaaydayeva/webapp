from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Подключение к базе данных
conn = psycopg2.connect(
    host="db-karina.ct6ei6agkus4.ap-south-1.rds.amazonaws.com",
    database="db-karina",
    user="postgres",
    password="postgres"
)

def safe_int(value):
    try:
        return int(value)
    except:
        return 0

@app.route('/data', methods=['GET'])
def get_data():
    cur = conn.cursor()
    cur.execute("""
        SELECT student_id, math, music, physical_ed, economics, english,
               biology, chemistry, physics, history, geography, computer_science, art
        FROM tbl_karina_marks
        ORDER BY student_id
        LIMIT 100;
    """)
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    result = [dict(zip(colnames, row)) for row in rows]
    cur.close()
    return jsonify(result)

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO tbl_karina_marks (
            student_id, math, music, physical_ed, economics, english,
            biology, chemistry, physics, history, geography, computer_science, art
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        safe_int(data.get('student_id')),
        safe_int(data.get('math')),
        safe_int(data.get('music')),
        safe_int(data.get('physical_ed')),
        safe_int(data.get('economics')),
        safe_int(data.get('english')),
        safe_int(data.get('biology')),
        safe_int(data.get('chemistry')),
        safe_int(data.get('physics')),
        safe_int(data.get('history')),
        safe_int(data.get('geography')),
        safe_int(data.get('computer_science')),
        safe_int(data.get('art'))
    ))
    conn.commit()
    cur.close()
    return jsonify({"status": "success"})

@app.route('/delete', methods=['POST'])
def delete_data():
    data = request.json
    cur = conn.cursor()
    cur.execute("DELETE FROM tbl_karina_marks WHERE student_id = %s", (data['student_id'],))
    conn.commit()
    cur.close()
 return jsonify({"status": "deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)