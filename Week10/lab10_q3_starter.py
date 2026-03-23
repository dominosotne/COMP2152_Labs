# ============================================================
#  WEEK 10 LAB — Q3: SECURITY AUDIT LOG + UNIT TESTS
# ============================================================

import os
import sqlite3
import sys
import unittest

DB_NAME = "audit_log.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            severity TEXT NOT NULL,
            message TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def seed_audit_log():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM audit_log")
    events = [
        ("2026-03-10 09:00:00", "LOW", "User login"),
        ("2026-03-11 10:30:00", "MEDIUM", "Config changed"),
        ("2026-03-12 11:15:00", "HIGH", "Multiple failed logins"),
        ("2026-03-13 08:45:00", "LOW", "Backup completed"),
        ("2026-03-14 14:00:00", "HIGH", "Unauthorized port scan"),
        ("2026-03-15 16:20:00", "MEDIUM", "Policy update"),
        ("2026-03-16 09:30:00", "HIGH", "Privilege escalation attempt"),
        ("2026-03-17 12:00:00", "LOW", "Routine scan OK"),
    ]
    cursor.executemany(
        "INSERT INTO audit_log (timestamp, severity, message) VALUES (?, ?, ?)",
        events,
    )
    conn.commit()
    conn.close()


def display_audit_section(title, rows):
    print(f"\n--- {title} ---")
    if not rows:
        print("  (no rows)")
        return
    for row in rows:
        print(f"  {row}")


# TODO: get_events_by_severity(severity)
def get_events_by_severity(severity):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM audit_log WHERE severity = ?", (severity,))
    rows = cursor.fetchall()
    conn.close()
    return rows


# TODO: get_recent_events(limit)
def get_recent_events(limit):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM audit_log ORDER BY timestamp DESC LIMIT ?",
        (limit,),
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


# TODO: count_by_severity()
def count_by_severity():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT severity, COUNT(*) FROM audit_log GROUP BY severity ORDER BY COUNT(*) DESC"
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


# TODO: safe_query(query)
def safe_query(query):
    conn = sqlite3.connect(DB_NAME)
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
        return []
    finally:
        conn.close()


class TestAuditLog(unittest.TestCase):
    def setUp(self):
        if os.path.exists(DB_NAME):
            os.remove(DB_NAME)
        init_db()
        seed_audit_log()

    # TODO: test_high_severity
    def test_high_severity(self):
        rows = get_events_by_severity("HIGH")
        self.assertEqual(len(rows), 3)

    # TODO: test_recent_events
    def test_recent_events(self):
        rows = get_recent_events(5)
        self.assertEqual(len(rows), 5)

    # TODO: test_count
    def test_count(self):
        results = count_by_severity()
        self.assertIn(("HIGH", 3), results)

    # TODO: test_safe_bad_query
    def test_safe_bad_query(self):
        result = safe_query("SELECT * FROM fake_table")
        self.assertEqual(result, [])


if __name__ == "__main__":
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    init_db()
    seed_audit_log()

    print("=" * 60)
    print("  SECURITY AUDIT LOG")
    print("=" * 60)

    display_audit_section("HIGH severity", get_events_by_severity("HIGH"))
    display_audit_section("5 most recent", get_recent_events(5))
    display_audit_section("Counts by severity", count_by_severity())

    print("\n--- Running Unit Tests ---")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestAuditLog)
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
    runner.run(suite)
