import wmi

wlan_int_id=None
for nic in wmi.WMI().Win32_NetworkAdapter():
    if nic.NetConnectionID == "Wireless Network Connection":
        wlan_int_id=nic.Index
        break

if wlan_int_id is not None:
    for nic in wmi.WMI ().Win32_NetworkAdapterConfiguration (IPEnabled=1):
        if nic.Index==wlan_int_id:
            print( nic.IPAddress[0])
else:
    print( "WLAN interface NOT Found")
