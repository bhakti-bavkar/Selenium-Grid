import wmi
for nic in wmi.WMI().Win32_NetworkAdapterConfiguration (IPEnabled=1):
    print( nic.Caption, nic.IPAddress)
