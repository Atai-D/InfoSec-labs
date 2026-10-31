import json
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)
app.config.update(MAX_CONTENT_LENGTH=2048, TRUSTED_HOSTS=["127.0.0.1", "localhost"])
FOLDER = Path(__file__).resolve().parent
DEMO = {
    "name": "DEMO STUDENT",
    "number": "0000 0000 0000 0000",
    "expiry": "00/00",
    "cvv": "000",
}


@app.get("/")
def index():
    return send_from_directory(FOLDER, "index.html")


@app.post("/submit")
def submit():
    data = request.get_json(silent=True)
    # Сохраняем только этот вымышленный пример, а не реальные реквизиты.
    if data != DEMO:
        return jsonify(message="Используйте только тестовые значения из примера."), 400
    try:
        with (FOLDER / "card_data.txt").open("a", encoding="utf-8") as file:
            file.write(json.dumps(DEMO, ensure_ascii=False) + "\n")
    except OSError:
        return jsonify(message="Не удалось записать card_data.txt."), 500
    return jsonify(message="Тестовые данные сохранены в card_data.txt.")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8765, debug=False)
