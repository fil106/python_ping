from pysnmp.hlapi import *

for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in bulkCmd(SnmpEngine(),
        CommunityData('public'),
        UdpTransportTarget(('192.168.88.1', 161)),
        ContextData(),
        0, 25,  # fetch up to 25 OIDs one-shot
        ObjectType(ObjectIdentity('1.3.6.1.2.1.17.7.1.2.2.1.2'))):
    if errorIndication or errorStatus:
        print(errorIndication or errorStatus)
        break
    else: #Выводит все возможные OID на устройстве
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
