# ============================================================
#  WEEK 10 LAB — Q1: PASSWORD VAULT
# ============================================================

import os
import sqlite3

DB_NAME = "vault.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS vault (
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def display_credential_rows(title, rows):
    print(f"\n--- {title} ---")
    if not rows:
        print("  (no results)")
        return
    for website, username, password in rows:
        print(f"  {website:<14} | {username:<12} | {password}")


# TODO: add_credential(website, username, password)
def add_credential(website, username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO vault (website, username, password) VALUES (?, ?, ?)",
        (website, username, password),
    )
    conn.commit()
    conn.close()


# TODO: get_all_credentials()
def get_all_credentials():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vault ORDER BY website ASC")
    rows = cursor.fetchall()
    conn.close()
    return rows


# TODO: find_credential(website)
def find_credential(website):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vault WHERE website = ?", (website,))
    rows = cursor.fetchall()
    conn.close()
    return rows


if __name__ == "__main__":
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    init_db()

    print("=" * 60)
    print("  PASSWORD VAULT")
    print("=" * 60)

    print("\n--- Adding Credentials ---")
    add_credential("github.com", "admin", "s3cur3P@ss")
    print("  Saved: github.com")
    add_credential("google.com", "maziar@gmail", "MyP@ssw0rd")
    print("  Saved: google.com")
    add_credential("netflix.com", "maziar", "N3tfl1x!")
    print("  Saved: netflix.com")
    add_credential("github.com", "work_user", "W0rkP@ss!")
    print("  Saved: github.com (work)")

    display_credential_rows("All Credentials", get_all_credentials())
    display_credential_rows("Search for 'github.com'", find_credential("github.com"))
    display_credential_rows("Search for 'spotify.com'", find_credential("spotify.com"))

    print("\n" + "=" * 60)
