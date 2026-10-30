
@echo off
cd /d "%~dp0"

echo TEST 1: Missing startup script
echo exit | python stage2.py --script missing.txt

echo TEST 2: Missing script with VFS argument
echo exit | python stage2.py --vfs ./vfs_data --script missing.txt

echo TEST 3: Unknown command
(echo badcommand & echo exit) | python stage2.py

pause
