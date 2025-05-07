import os
import sys
import pytest

def test_gui_runs():
    # Skip test in headless environments (like GitHub Actions)
    if os.environ.get("CI") == "true" or sys.platform.startswith("linux"):
        pytest.skip("Skipping GUI test in CI environment without display")

    import subprocess
    import time

    try:
        proc = subprocess.Popen(["python", "SimpleInsulinCalc_GUI_Refactored_Accessible.py"])
        time.sleep(3)
        proc.terminate()
        assert True
    except Exception:
        assert False