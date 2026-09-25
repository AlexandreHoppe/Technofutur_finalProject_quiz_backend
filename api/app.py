import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from flask import Flask, jsonify
from flask_cors import CORS
from api.routes.user_routes import user_blueprint
from api.routes.score_routes import score_blueprint
from api.routes.quiz_routes import quiz_blueprint
from api.routes.question_routes import question_blueprint

from dal.database import init_db, test_connection, seed_data

load_dotenv()

app = Flask(__name__)
app.json.sort_keys = False
CORS(app, origins=["http://localhost:4200"])

def startup():
    if test_connection():
        init_db(delete=False)
        seed_data()
        print("Database ready")

startup()

@app.route("/")
def test():
    return jsonify({
        "test" : "testing"
    })

app.register_blueprint(user_blueprint)
app.register_blueprint(score_blueprint)
app.register_blueprint(quiz_blueprint)
app.register_blueprint(question_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=5000)