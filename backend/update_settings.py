with open('backend/settings.py', 'r') as f:
    content = f.read()

# Обновляем STATIC_ROOT
import re
content = re.sub(r"STATIC_ROOT = .*", "STATIC_ROOT = BASE_DIR / 'collected_static'", content)

# Обновляем ALLOWED_HOSTS
content = re.sub(r"ALLOWED_HOSTS = \[\]", "ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'backend', 'gateway']", content)

with open('backend/settings.py', 'w') as f:
    f.write(new_content)
print("Settings updated")
