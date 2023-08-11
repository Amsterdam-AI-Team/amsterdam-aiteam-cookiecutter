import os

# Create folder structure

CREATE_FOLDERS = [
    "data",
    "docs",
    "notebooks",
    "res/images",
    "scripts",
    "src",
    "tests",
    ]

for path in CREATE_FOLDERS:
    path = path.strip()
    os.makedirs(path, exist_ok=True)

# Remove unnecessary files based on cookiecutter params

REMOVE_PATHS = [
    "{% if cookiecutter.env_management != 'pip' %} requirements.txt {% endif %}",
    "{% if cookiecutter.env_management != 'conda' %} environment.yml {% endif %}",
    ]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
