import subprocess

def test_gui_runs():
    result = subprocess.run(["python", "gui.py"], capture_output=True, text=True)
    assert result.returncode == 0
