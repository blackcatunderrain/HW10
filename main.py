from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = get_candidates()
    data = make_page_candidates(candidates)
    return data


@app.route("/candidates/<int:uid>")
def page_candidates(uid):
    candidates = get_candidates_by_uid(uid)
    data = f"<img src='{candidates['picture']}'>"
    data += make_page_candidates([candidates])
    return data


app.run()
