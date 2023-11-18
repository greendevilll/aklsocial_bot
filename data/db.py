import sqlite3
from data.config import db_fn
import random

async def is_user_exists(uid: int):
    with sqlite3.connect(db_fn) as db:
        res = db.execute("SELECT * FROM users WHERE id=?",(uid,)).fetchone()
        if res == None:
            return False
        return bool(len(res))

async def reg_user(uid: int):
    print(db_fn)
    if await is_user_exists(uid):
        return
    with sqlite3.connect(db_fn) as db:
        db.execute("INSERT INTO users (id) VALUES (?)",(uid,))

async def new_text(text: str, is_anon: int):
    with sqlite3.connect(db_fn) as db:
        db.execute("INSERT INTO data (text, is_anon) VALUES (?,?)",(text, is_anon,))

        r = db.execute("SELECT id FROM data ORDER BY ID DESC LIMIT 1").fetchone()
        return r
    
async def select_random(range_: int):
    with sqlite3.connect(db_fn) as db:
        public_ids = [int(i[0]) for i in db.execute("SELECT id FROM data WHERE is_anon = 0").fetchall()]
        if len(public_ids) <= 0:
            return None
        range_ = min(range_,len(public_ids))
        random_ids = [random.choice(public_ids) for _ in range(0,range_)]
        out = []
        for id_ in random_ids:
            r = db.execute("SELECT text FROM data WHERE id = ?",(id_,)).fetchone()
            out.append(r[0])
    return out
        