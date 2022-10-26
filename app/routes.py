from datetime import datetime
from flask import (Blueprint, render_template)
import sqlite3
import os
bp = Blueprint("main", __name__, url_prefix='/')
DB_FILE = os.environ.get("DB_FILE")

@bp.route('/')
def main():
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute("""
                        SELECT id, name, start_datetime, end_datetime
                        FROM appointments
                        ORDER BY start_datetime;
                        """)
        data = curs.fetchall()
        rows = []
        for row in data:
            start = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
            end = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
            rows.append(([row[0], row[1], start, end]))
        return render_template('main.html', rows=rows)
