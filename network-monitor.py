import subprocess
from decouple import config

IP_DEVICE = config('IP_DEVICE')

process = subprocess.Popen(["ping", '-t', IP_DEVICE], stdout=subprocess.PIPE)

while True:
    line = process.stdout.readline()
    if not line:
        break

    try:
        connected_ip = line.decode('utf-8').split()[2].replace(':', '')
        if connected_ip == IP_DEVICE:
            print('Device connected!')
            break
        else:
            print('Pinging device...')
    except (IndexError, UnicodeDecodeError):
        pass
