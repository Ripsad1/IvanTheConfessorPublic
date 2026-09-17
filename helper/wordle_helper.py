import sqlite3

wordle_data = sqlite3.connect("wordle.db")
cursor = wordle_data.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS wordle_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    wordle INTEGER NOT NULL,
    guesses INTEGER NOT NULL,
    won INTEGER NOT NULL CHECK (won IN (0, 1))
)
""")

wordle_data.commit()