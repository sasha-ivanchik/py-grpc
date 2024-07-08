from pathlib import Path

from piccolo.engine.sqlite import SQLiteEngine
from piccolo.table import Table
from piccolo.columns import Varchar, Integer, Boolean

db_path = Path.cwd() / "db" / "db.sqlite"
engine = SQLiteEngine(path=str(db_path))


class Item(Table, db=engine):
    is_simple = Boolean(default=True)
    name = Varchar()
    sample_int = Integer(default=0)
    user_id = Integer()
