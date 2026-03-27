import subprocess

filename = "data.txt"

try:
    with open(filename, "r", encoding="utf-8") as f:
        file_content = f.read()

    result = subprocess.run(
        ["wc", "-l"],
        input=file_content,    
        capture_output=True,     
        text=True               
    )

    print(f"Кількість рядків у файлі '{filename}':", result.stdout.strip())

except FileNotFoundError:
    print(f"Помилка: Файл '{filename}' не знайдено. Створіть його перед запуском.")
except Exception as e:
    print(f"Сталася непередбачувана помилка: {e}")