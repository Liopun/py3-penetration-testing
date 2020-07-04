import nmap

scanner = nmap.PortScanner()

print("--------SIMPLE NMAP AUTOMATION TOOL--------")
print("<------------------------------------------>")

ip_addr = input("Enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP scan
                3)Comprehensive Scan\n""")
print("You have selected option: ", resp)

if (resp == '1'):
  print("Nmap version: ", scanner.nmap_version())
  scanner.scan(ip_addr, '1-1024', '-v -sS')
  print(scanner.scaninfo())
  print("IP status: ", scanner[ip_addr].state())
  print("IP protocol: ", scanner[ip_addr].all_protocols())
  print("Open ports: ", scanner[ip_addr]['tcp'].keys())




