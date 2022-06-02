from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = get_candidates()
    result = make_page_candidates(candidates)
    return result


@app.route("/candidates/<int:uid>")
def page_candidates(uid):
    candidates = get_candidates_by_uid(uid)
    result = f"<img src='{candidates['picture']}'>"
    result += make_page_candidates([candidates])
    return result


@app.route("/skills/<skill>")
def page_skills(skill):
    candidates = get_candidates_by_skill(skill)
    result = make_page_candidates(candidates)
    return result


app.run()
