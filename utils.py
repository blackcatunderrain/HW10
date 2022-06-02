import json

FILENAME = "candidates.json"


def load_candidates(filename: str) -> list[dict]:
    """Загружаем JSON из файла"""
    with open(filename, encoding='UTF-8') as file:
        data = json.load(file)
    return data


def get_candidates() -> list[dict]:
    return load_candidates(FILENAME)


def get_candidates_by_uid(uid: int) -> dict | None:
    candidates = get_candidates()
    for i in candidates:
        if i["id"] == uid:
            return i
    return None


def make_page_candidates(candidates: list) -> str:
    data = "<pre>"

    for i in candidates:
        data += f"{i['name']}\n {i['position']}\n{i['skills']}\n"

    data += "</pre>"
    return data
