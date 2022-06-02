import json

FILENAME = "candidates.json"


def load_candidates(filename: str) -> list[dict]:
    """Загружаем JSON из файла"""
    with open(filename, encoding='UTF-8') as file:
        data = json.load(file)
    return data


def get_candidates() -> list[dict]:
    """Получить кандидатов"""
    return load_candidates(FILENAME)


def get_candidates_by_uid(uid: int) -> dict | None:
    """Получить кандидата по UID"""
    candidates = get_candidates()
    for i in candidates:
        if i["id"] == uid:
            return i
    return None


def get_candidates_by_skill(skill: str) -> list[dict]:
    """Получить кандидатов по скилу"""
    candidates = get_candidates()
    result = []
    for i in candidates:
        if skill.lower() in i["skills"].lower().split(", "):
            result.append(i)
    return result


def make_page_candidates(candidates: list) -> str:
    """Создать страницу кандидатов для вью"""
    data = "<pre>"
    for i in candidates:
        data += f"{i['name']}\n {i['position']}\n{i['skills']}\n"
    data += "</pre>"
    return data
