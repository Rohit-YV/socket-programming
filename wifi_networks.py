import subprocess       
nw = subprocess.check_output(['netsh','wlan','show','network'])
decoded_nw=nw.decode('ascii')
print(decoded_nw)