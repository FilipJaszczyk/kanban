# Project setup

```bash
poetry install
poetry shell
```
## Swagger schema 

Regenerate schema
```bash
poetry shell
make schema
python manage.py runserver
```
New schema will be at /api/schema/swagger
