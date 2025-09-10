import os
from django.core.files import File
from main.models import Photo
from django.conf import settings

folder_path = os.path.join(settings.MEDIA_ROOT, "photos")
if not os.path.exists(folder_path):
    print(f"❌ Папка {folder_path} не найдена!")
else:
    files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))])
    files_to_add = files[:404]

    for idx, filename in enumerate(files_to_add, start=1):
        relative_path = f"photos/{filename}"
        Photo.objects.create(
            title=f"Модель №{idx}",
            image=relative_path
        )
        print(f"✅ Добавлено: {filename} → Модель №{idx}")

print("\n✅ Все 404 фотографии добавлены в базе с номерами 1–404")
