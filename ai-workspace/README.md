RECOMMENDED FOLDER STRUCTURE 
app/
├── main.py
├── api/
├── models/
├── schemas/
├── services/
├── repositories/
├── db/
├── core/
└── utils/

HOW TO CREATE MIGRATION 
alembic revision --autogenerate -m "create users table"
HOW TO APPLY MIGRATION 
alembic upgrade head