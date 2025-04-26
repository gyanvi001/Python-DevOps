import subprocess

def is_service_running(servicename):
    status = subprocess.run([ 'systemctl' , 'isactive' , servicename], stdout = subprocess.PIPE)
    return status.stdout.decode().strip() == "active"

service = "ngnix"
if is_service_running(service):
    print(f"{service} is running ")
else:
    print(f"{service} is not running")






