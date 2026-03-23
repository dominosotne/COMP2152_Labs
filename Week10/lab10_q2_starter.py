# ============================================================
#  WEEK 10 LAB — Q2: LOGIN ATTEMPT TRACKER
# ============================================================

import os
import sqlite3
import datetime
import sys

DB_NAME = "login_attempts.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS login_attempts (
            username TEXT NOT NULL,
            success INTEGER NOT NULL,
            attempted_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def display_failed_attempts(title, rows):
    print(f"\n--- {title} ---")
    for username, success, attempted_at in rows:
        status = "success" if success else "FAILED"
        print(f"  {username:<8} | {status:<7} | {attempted_at}")


def display_failure_counts(rows):
    print(f"\n--- Failure Counts ---")
    for username, count in rows:
        extra = ""
        if username == "root" and count >= 4:
            extra = "  \u26a0 root has 4 failed attempts \u2014 possible brute-force!"
        print(f"  {username:<11} {count} failed attempts{extra}")


# TODO: record_attempt(username, success)
def record_attempt(username, success):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO login_attempts (username, success, attempted_at) VALUES (?, ?, ?)",
        (username, 1 if success else 0, now),
    )
    conn.commit()
    conn.close()


# TODO: get_failed_attempts(username)
def get_failed_attempts(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM login_attempts WHERE username = ? AND success = 0",
        (username,),
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


# TODO: count_failures_per_user()
def count_failures_per_user():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT username, COUNT(*) FROM login_attempts
        WHERE success = 0
        GROUP BY username
        ORDER BY username ASC
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


# TODO: delete_old_attempts(username)
def delete_old_attempts(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM login_attempts WHERE username = ?", (username,))
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    init_db()

    print("=" * 60)
    print("  LOGIN ATTEMPT TRACKER")
    print("=" * 60)

    print("\n--- Recording Login Attempts ---")
    attempts = [
        ("admin", True),
        ("admin", False),
        ("admin", False),
        ("admin", False),
        ("guest", True),
        ("guest", False),
        ("root", False),
        ("root", False),
        ("root", False),
        ("root", False),
    ]
    for user, ok in attempts:
        record_attempt(user, ok)
        status = "success" if ok else "FAILED"
        print(f"  Recorded: {user} ({status})")

    display_failed_attempts("Failed Attempts for 'admin'", get_failed_attempts("admin"))

    rows = count_failures_per_user()
    display_failure_counts(rows)

    print("\n--- Reset 'root' account (delete all attempts) ---")
    n = delete_old_attempts("root")
    print(f"  Deleted {n} records for root")

    print("\n--- Failure Counts (after reset) ---")
    for username, count in count_failures_per_user():
        print(f"  {username:<11} {count} failed attempts")

    print("\n" + "=" * 60)
