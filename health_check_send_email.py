#!/usr/bin/env python3

import os
import shutil
import psutil
import sys
import socket
import report_email

def check_cpu_constrained():
    """Returns True if the cpu is having too much usage, False otherwise."""  
    return psutil.cpu_percent(1) > 80

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise."""
    disk_usage = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * disk_usage.free / disk_usage.total
    # Calculate how many free gigabytes
    gigabytes_free = disk_usage.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def check_memory():
    """ Returns True if the computer is low on memory."""
    return psutil.virtual_memory()[3]/1000000000 > 0.5

def localhost_check():
    """ Returns True if 'localhost' resolves to "127.0.0.1", False otherwise. """
    host = socket.gethostbyname('localhost')
    if host == "127.0.0.1":
        return False
    else:
        return True

def main():
    """ Check for errors then send email if one is detected """
    checks=[(check_cpu_constrained(), "ERROR - CPU load too high."), (check_disk_full("/", 5, 55), "Error - Available disk space is less than 20%"), (check_memory(), "Error - Available memory is less than 500MB"), (localhost_check(), "Error - localhost cannot be resolved to 127.0.0.1")]
    for check, msg in checks:
        if check:
            """ If error, send appropriate email """
            subject = msg
            sender = "automation@example.com"
            receiver = "{}@example.com".format(os.environ.get('USER'))
            body = "\n\n" + "Please check your system and resolve the issue as soon as possible."
            message = report_email.generate_email_no_attachment(sender, receiver, subject, body)
            # report_email.send(message)
            print(msg)
        else: 
            """ If no error, display quick OK message """
            if msg == "ERROR - CPU load too high.":
                print("CPU: OK")
            if msg == "Error - Available disk space is less than 20%":
                print("Disk space: OK")
            if msg == "Error - Available memory is less than 500MB":
                print("RAM: OK")
            if msg == "Error - localhost cannot be resolved to 127.0.0.1":
                print("localhost: OK")

if __name__ == "__main__":
  main()