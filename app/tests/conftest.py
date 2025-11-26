import pytest
import yaml
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ===============================
# Шлях до конфігурації
# ===============================
config_path = Path(__file__).resolve().parent.parent / "config" / "app.yml"

# Зчитування конфігу
with open(config_path, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

db_config = config["database"]

# ===============================
# Підключення до бази даних
# ===============================
DATABASE_URL = (
    f"{db_config['dialect']}+{db_config['driver']}://"
    f"{db_config['username']}:{db_config['password']}@"
    f"{db_config['host']}:{db_config['port']}/"
    f"{db_config['database']}"
)

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ===============================
# Pytest фікстура для сесії БД
# ===============================
@pytest.fixture(scope="function")
def db_session():
    """
    Фікстура для тестів, яка створює сесію БД і закриває її після тесту.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
