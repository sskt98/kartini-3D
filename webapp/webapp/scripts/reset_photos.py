import os
import sys
import django
from django.core.files import File

# --- Настройка Django ---
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
django.setup()

from main.models import Photo
from django.conf import settings

# --- Папка с фотографиями ---
folder = os.path.join(settings.MEDIA_ROOT, 'photos')
if not os.path.exists(folder):
    print(f"❌ Папка {folder} не найдена!")
    exit()

# --- Очистка базы ---
Photo.objects.all().delete()
print("✅ Все старые фотографии удалены из базы")

# --- Переименование файлов по числовому порядку ---
files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg','.jpeg','.png','.gif'))]

def get_number(f):
    """Возвращает числовую часть имени файла"""
    name = os.path.splitext(f)[0]
    try:
        return int(name)
    except ValueError:
        return 0

files.sort(key=get_number)

for idx, filename in enumerate(files, start=1):
    ext = os.path.splitext(filename)[1]
    new_name = f"{idx}{ext}"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

print(f"✅ Файлы переименованы по числовому порядку 1…{len(files)}")

# --- Добавление файлов в базу ---
files = sorted(os.listdir(folder), key=get_number)

for idx, filename in enumerate(files, start=1):
    path = os.path.join(folder, filename)
    with open(path, 'rb') as f:
        photo = Photo()
        photo.image.save(filename, File(f), save=False)
        photo.title = f'Модель №{idx}'
        photo.save()
        print(f"Добавлено: {filename} → Модель №{idx}")

print("\n🎉 Все фотографии добавлены по правильному порядку!")