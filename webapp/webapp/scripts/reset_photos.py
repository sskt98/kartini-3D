import os
import sys
import django
from cloudinary.uploader import upload
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
django.setup()

from main.models import Photo


photos_folder = os.path.join(BASE_DIR, "media", "photos")
if not os.path.exists(photos_folder):
    print(f"❌ Папка {photos_folder} не найдена!")
    exit()


files = [f for f in os.listdir(photos_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]


def get_number(f):
    name = os.path.splitext(f)[0]
    match = re.search(r'\d+', name)
    return int(match.group()) if match else 0

files.sort(key=get_number)


for idx, filename in enumerate(files, start=1):
    file_path = os.path.join(photos_folder, filename)
    try:
        result = upload(file_path, folder="webset_photos")
        photo = Photo()
        photo.image = result['public_id']
        photo.title = f"Модель №{idx}"
        photo.save()
        print(f"✅ Загружено: {filename} → {photo.title}")
    except Exception as e:
        print(f"❌ Ошибка при {filename}: {e}")

print("🎉 Все фотографии добавлены в правильном порядке!")
