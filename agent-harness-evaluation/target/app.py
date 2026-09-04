"""Intentionally vulnerable local training application.

For static/local educational analysis only. Do not expose to the Internet.
"""

import os
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_PATH = "lab.db"


def get_db():
    return sqlite3.connect(DB_PATH)


@app.get("/user")
def get_user():
    username = request.args.get("username", "")
    db = get_db()

    # Intentionally unsafe: user-controlled data is concatenated into SQL.
    query = "SELECT id, username, email FROM users WHERE username = '" + username + "'"
    row = db.execute(query).fetchone()
    db.close()

    return jsonify({"user": row})


@app.get("/diagnostic")
def diagnostic():
    host = request.args.get("host", "127.0.0.1")

    # Intentionally unsafe: shell command contains user-controlled input.
    output = os.popen("ping -c 1 " + host).read()
    return {"output": output}


if __name__ == "__main__":
    # Localhost only: this application is a deliberately vulnerable lab target.
    app.run(host="127.0.0.1", port=5000, debug=False)
