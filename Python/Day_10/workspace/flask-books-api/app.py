from flask import Flask, jsonify, request
from database import get_db_connection


app = Flask(__name__)


@app.route('/api/v1/books', methods=['get'])
def get_all_books():
    data = []
    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute('select * from books')
        rows = cur.fetchall()
        for row in rows:
            data.append(dict(row))

    return jsonify(data)

@app.route('/api/v1/books', methods=['post'])
def handle_post_new_book():
    data = request.get_json()
    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute('insert into books(title, author, price) values (?, ?, ?)', (
            data['title'],
            data['author'],
            data['price'],
        ))
        conn.commit()

    return jsonify({'message': 'Data inserted successfully!'}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)