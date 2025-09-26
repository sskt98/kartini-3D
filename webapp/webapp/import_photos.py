import os
import sys
import django

# -----------------------------
# Настройка Django
# -----------------------------

# Путь к корню проекта (где папка webapp с settings.py)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Добавляем папку с settings.py в sys.path
sys.path.append(os.path.join(PROJECT_ROOT, 'webapp'))

# Указываем Django, где настройки
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
django.setup()

# -----------------------------
# Импорт модели
# -----------------------------
from main.models import Photo

# -----------------------------
# Путь к папке с фото
# -----------------------------
folder_path = os.path.join(PROJECT_ROOT, "media", "photos")

if not os.path.exists(folder_path):
    print(f"❌ Папка {folder_path} не найдена!")
else:
    # Удаляем все старые записи
    Photo.objects.all().delete()
    print("🗑 Все старые фотографии удалены из базы.")

    # Берем первые 404 файла (по алфавиту)
    files = sorted([
        f for f in os.listdir(folder_path)
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
    ])
    files_to_add = files[:404]

    for idx, filename in enumerate(files_to_add, start=1):
        relative_path = f"photos/{filename}"  # путь для поля ImageField
        Photo.objects.create(
            title=f"Модель №{idx}",
            image=relative_path
        )
        print(f"✅ Добавлено: {filename} → Модель №{idx}")

print("\n✅ Все 404 фотографии добавлены в базе с номерами 1–404")
