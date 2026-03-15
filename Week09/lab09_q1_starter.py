# ============================================================
#  WEEK 09 LAB — Q1: SYSTEM INFORMATION REPORTER
#  COMP2152 — Alikhan Zhilkibayev
# ============================================================

import os
import sys
import platform


# --- Helper (provided) — error handling example from Week 06 ---
def display(title, data):
    print(f"\n--- {title} ---")
    for k, v in data.items():
        print(f"  {k:<12} : {v}")


def safe_run(label, func, *args):
    try:
        result = func(*args)
        if result is None:
            print(f"  [!] {label} returned None — missing return?")
            return {}
        return result
    except Exception as e:
        print(f"  [ERROR] {label}: {e}")
        return {}


# TODO: Complete get_system_info()
#   Return a dict with keys: "os", "node", "release", "machine"
#   Use: platform.system(), platform.node(),
#        platform.release(), platform.machine()
def get_system_info():
    pass


# TODO: Complete get_python_info()
#   Return a dict with keys: "version", "executable", "platform"
#   Use: sys.version, sys.executable, sys.platform
def get_python_info():
    pass


# TODO: Complete get_directory_info(path)
#   Return a dict with keys: "path", "exists", "file_count", "is_directory"
#   Use: os.path.abspath(), os.path.exists(),
#        os.listdir() (count items), os.path.isdir()
def get_directory_info(path):
    pass


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  SYSTEM INFORMATION REPORTER")
    print("=" * 60)

    info = safe_run("System Info", get_system_info)
    if info: display("System Info", info)

    info = safe_run("Python Info", get_python_info)
    if info: display("Python Info", info)

    info = safe_run("Directory Info", get_directory_info, ".")
    if info: display("Directory Info for '.'", info)

    print("\n" + "=" * 60)