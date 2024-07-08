from pathlib import Path

from piccolo.engine.sqlite import SQLiteEngine
from piccolo.table import Table
from piccolo.columns import Varchar, Integer

db_path = Path.cwd() / "db" / "db.sqlite"
engine = SQLiteEngine(path=str(db_path))


class User(Table, db=engine):
    # id = Integer(primary_key=True, autoincrement=True)
    username = Varchar(unique=True)
    hashed_password = Varchar()
