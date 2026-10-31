from email.message import EmailMessage
from pathlib import Path

# Создаём письмо локально. Никуда его не отправляем.
message = EmailMessage()
message["From"] = "training@example.test"
message["To"] = "student@example.test"
message["Subject"] = "Учебный пример — форма карты"
message.set_content(
    "Это учебная демонстрация. Используйте только вымышленные данные.\n"
    "Сначала запустите server.py, затем откройте http://127.0.0.1:8765/"
)
message.add_alternative("""
<html lang="ru"><body>
  <h2>Учебная форма карты</h2>
  <p>Только вымышленные данные. Никаких реальных платежей.</p>
  <a href="http://127.0.0.1:8765/">Открыть локальную форму</a>
</body></html>
""", subtype="html")

path = Path(__file__).resolve().parent / "email.eml"
path.write_bytes(message.as_bytes())
print(f"Письмо сохранено в {path.name}. Отправки нет.")
