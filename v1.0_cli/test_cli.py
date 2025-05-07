import subprocess

def test_cli_input_logic():
    # Simulate passing inputs via subprocess (if CLI supports arguments or stdin interaction)
    process = subprocess.Popen(['python', 'main.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        output, _ = process.communicate(input="breakfast\n50\nno\n", timeout=5)
        assert "Units" in output or "units" in output
    except subprocess.TimeoutExpired:
        process.kill()
        assert False, "CLI test timed out"
