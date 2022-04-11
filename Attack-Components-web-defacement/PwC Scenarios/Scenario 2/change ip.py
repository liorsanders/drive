import wmi


def findAndChangeIp():
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    # find not vm network adaptor
    i = 0
    while(True):
        nic = nic_configs[i]
        print(nic.Caption)
        if "VM" not in nic.Caption:
            break
        i += 1
    for adatper in nic_configs:
        if "VM" not in nic.Caption:
            nic = adatper
            break


    # getting the current values and changing only the ip
    ip = nic.IPAddress
    print("current ip:", ip)
    ip = ('192.168.192.218',) # todo cahnge last digits to one more
    mask = nic.IPSubnet
    gateway = nic.DefaultIPGateway
    print(mask, gateway, ip, sep='\n')
    print(nic.EnableStatic(IPAddress=ip, SubnetMask=mask))
    print(nic.SetGateways(DefaultIPGateway=gateway))

findAndChangeIp()
