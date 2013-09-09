import ConfigParser
import twisted.internet



[SystemInformation]
Clientname: 
User: 
Password: 
Server: 
TestLog:
ProdLog:
TimeZne:


[Monitor]
MonitorMode:     #Options: Single, Subnet, Custom
TestIntervole:
ErrorIntervole:
RetryIntervole:
#NetmonitorDev: (192.168.1.2, wifirouter)
#Edit your '/etc/hosts' file to create names for each device or insert IP addresses
    
    
[Logging]
NetErrorLogging:False
NetErrorLogType: File   '''Options: File, MongoDB, Redis '''
NetErrorLogDir: /etc/netman/neterror.log
#NetErrorMongoDB: (Hostname, Username, Password)
#NetErrorRedisDB: (Hostname, Username, Password)




[Network]
Tunnel:False
IPAddr:
IPSubnet:
IPGw:







