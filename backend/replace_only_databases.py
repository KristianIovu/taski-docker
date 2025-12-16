import re

with open('backend/settings.py', 'r') as f:
    content = f.read()

# Добавляем import os если его нет
if 'import os' not in content:
    content = content.replace('from pathlib import Path',
                              'from pathlib import Path\nimport os')

# Заменяем только DATABASES блок
new_db_config = '''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'django'),
        'USER': os.getenv('POSTGRES_USER', 'django'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', ''),
        'PORT': os.getenv('DB_PORT', 5432)
    }
}'''

# Ищем и заменяем DATABASES блок
pattern = r"DATABASES\s*=\s*\{[^}]+\}"
new_content = re.sub(pattern, new_db_config, content, flags=re.DOTALL)

with open('backend/settings.py', 'w') as f:
    f.write(new_content)

print("DATABASES блок заменён без комментариев")
