
@echo off
cd /d "%~dp0"

echo TEST 1: No arguments
echo exit | python stage2.py

echo TEST 2: VFS argument
echo exit | python stage2.py --vfs ./vfs_data

echo TEST 3: Startup script
python stage2.py --script start.txt

echo TEST 4: Both arguments
python stage2.py --vfs ./vfs_data --script start.txt

pause
