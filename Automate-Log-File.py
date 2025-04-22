""" This script will:
- Check the size of the log file.
- If it exceeds a specified limit (e.g., 5 MB), it will rename the current log file and create a new one.
- Keep a specified number of backup logs (e.g., 5). """

import os
import gzip
import shutil
from datetime import datetime

#Configuration
MAX_LOG_SIZE = 5
MAX_BACKUPS = 5
LogFile = "app.log"


def rotate_logs():
    if not os.path.exists:
        print("Log file not found")
        return
    
    log_size_mb = os.path.getsize(LogFile) / 1024*1024
    if log_size_mb < MAX_LOG_SIZE:
        print("No need to rotate the log file. Log File size within limit")

    










