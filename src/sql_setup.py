''' Script for setting up a quick sqlite db '''

import sqlite3
import pathlib

from sqlite3 import Cursor, Connection
from typing import Tuple

def setup_db() -> Tuple[Connection,Cursor]:
    """ Quickly creates sqlite db.

    """
    if not pathlib.Path("data").exists():
        pathlib.Path("data").mkdir()
    conn = sqlite3.connect("data/image.db")
    c = conn.cursor()
    return conn, c