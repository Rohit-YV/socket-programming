import nmap

begin = 75
end = 80
target = '127.0.0.1'
scanner = nmap.PortScanner()

for i in range(begin, end + 1):
    try:
        res = scanner.scan(target, str(i))
        state = res['scan'][target]['tcp'][i]['state']
        print(f"Port {i} is {state}.")
    except KeyError:
        print(f"Port {i} is not available in the scan results.")
    except Exception as e:
        print(f"An error occurred while scanning port {i}: {e}")
