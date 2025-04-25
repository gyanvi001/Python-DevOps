"""
This script will:
- Check the size of the log file.
- If it exceeds a specified limit (e.g., 5 MB), it will rename the current log file and create a new one.
- Keep a specified number of backup logs (e.g., 5).
"""

import os
import shutil

# Configuration
MAX_LOG_SIZE = 5  # in MB
MAX_BACKUPS = 5
LogFile = "app.log"


def rotate_logs():
    if not os.path.exists(LogFile):  # Fixed condition
        print("Log file not found")
        return

    log_size_mb = os.path.getsize(LogFile) / (1024 * 1024)  # Use parentheses to ensure correct math
    if log_size_mb < MAX_LOG_SIZE:
        print("No need to rotate the log file. Log File size within limit")
        return

    print(f"Rotating Log File {LogFile}")  # Added f-string formatting

    # Remove the oldest log if it exists
    oldest_log = f"{LogFile}.{MAX_BACKUPS}"
    if os.path.exists(oldest_log):
        os.remove(oldest_log)

    # Rotate older logs
    for i in range(MAX_BACKUPS - 1, 0, -1):
        src = f"{LogFile}.{i}"
        dest = f"{LogFile}.{i + 1}"
        if os.path.exists(src):
            os.rename(src, dest)

    # Rename the current log to log.1
    shutil.move(LogFile, f"{LogFile}.1")

    # Create a new empty logfile
    open(LogFile, 'w').close()
    print("Rotation_Complete")


if __name__ == "__main__":  # Moved to the correct indentation level
    rotate_logs()
