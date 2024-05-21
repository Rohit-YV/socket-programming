from socket import *
import time

if __name__ == "__main__":
    target = input('Enter host for scanning: ')
    try:
        t_ip = gethostbyname(target)
        print('Starting scanning on host:', t_ip)
    except gaierror:
        print('Hostname could not be resolved. Exiting.')
        exit()

    starttime = time.time()

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(1)
        conn = s.connect_ex((t_ip, i))
        if conn == 0:
            print('Port %d: open' % (i))
        s.close()

    print("Time taken:", time.time() - starttime)
