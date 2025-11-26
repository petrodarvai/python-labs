from sqlalchemy import text

def test_dummy(db_session):
    # обертаємо SQL рядок у text()
    result = db_session.execute(text("SELECT 1")).fetchone()
    assert result[0] == 1
