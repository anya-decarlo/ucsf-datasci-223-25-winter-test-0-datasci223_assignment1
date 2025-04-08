import os
import sys
import hashlib
import subprocess
import pytest
import shutil

# Test constants
TEST_EMAIL = "test@example.com"
EXPECTED_SHA256_HASH = hashlib.sha256(TEST_EMAIL.encode()).hexdigest()

def test_committed_hash_email():
    """Test that the committed hash.email file exists and has the correct format"""
    if not os.path.exists("hash.email"):
        pytest.skip("No hash.email file committed to the repository")
    with open("hash.email", "r") as f:
        hash_output = ''.join(f.read().split())
    assert len(hash_output) == 64, "Committed hash length is not 64 characters (after removing whitespace)"
    assert all(c in "0123456789abcdef" for c in hash_output.lower()), "Committed hash contains non-hexadecimal characters"

def setup_function():
    """Move hash.email file to a backup location if it exists"""
    if os.path.exists("hash.email"):
        shutil.move("hash.email", "hash.email.bak")

def test_script_exists():
    """Test that email_hasher.py exists"""
    assert os.path.exists("email_hasher.py"), "email_hasher.py file not found"

def test_command_line_args():
    """Test that the script accepts command line arguments"""
    result = subprocess.run(
        [sys.executable, "email_hasher.py", TEST_EMAIL],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Script failed with error: {result.stderr}"
    assert os.path.exists("hash.email"), "hash.email file was not created"

def test_sha256_algorithm():
    """Test that the script uses SHA-256 algorithm"""
    subprocess.run(
        [sys.executable, "email_hasher.py", TEST_EMAIL],
        capture_output=True,
        text=True
    )
    with open("hash.email", "r") as f:
        hash_output = f.read().strip()
    assert hash_output == EXPECTED_SHA256_HASH, "Hash does not match expected SHA-256 hash"

def test_hex_format():
    """Test that the hash is in hexadecimal format"""
    subprocess.run(
        [sys.executable, "email_hasher.py", TEST_EMAIL],
        capture_output=True,
        text=True
    )
    with open("hash.email", "r") as f:
        hash_output = ''.join(f.read().split())
    assert len(hash_output) == 64, "Hash length is not 64 characters (after removing whitespace)"
    assert all(c in "0123456789abcdef" for c in hash_output.lower()), "Hash contains non-hexadecimal characters"

def test_file_creation():
    """Test that the script creates a file named 'hash.email'"""
    subprocess.run(
        [sys.executable, "email_hasher.py", TEST_EMAIL],
        capture_output=True,
        text=True
    )
    assert os.path.exists("hash.email"), "hash.email file was not created"
    with open("hash.email", "r") as f:
        content = f.read().strip()
    assert content, "hash.email file is empty"

def teardown_function():
    """Restore hash.email file if it was backed up"""
    if os.path.exists("hash.email.bak"):
        shutil.move("hash.email.bak", "hash.email")

def test_readme_exists():
    """Test that README.md exists"""
    assert os.path.exists("README.md"), "README.md file is missing"

def test_readme_contains_link():
    """Test that README.md contains a link (http)"""
    if not os.path.exists("README.md"):
        pytest.skip("README.md file is missing")
    with open("README.md", "r") as f:
        content = f.read()
    assert "http" in content, "README.md might be missing a link to music recommendation"