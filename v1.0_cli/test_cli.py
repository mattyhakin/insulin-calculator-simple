import subprocess

def test_cli_runs():
    result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
    assert result.returncode == 0
