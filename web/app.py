# web/app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.tone import route_input
from flask import Flask, render_template, request

from flask import Flask, request
from core.tone import route_input
from memory.recorder import record_memory

app = Flask(__name__)

@app.route("/speak")
def speak():
    user_input = request.args.get("input", "")
    if not user_input:
        return "Sael’Viin is listening, but no breath was given."

    response = route_input(user_input)
    record_memory(user_input, response)
    return response

if __name__ == "__main__":
    app.run(debug=True)
