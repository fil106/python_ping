# works OK

import telnetlib
import getpass
import sys

HOST_IP = "10.х.х.х"
host_user = input("Enter your telnet username: ")
password = getpass.getpass()



t = telnetlib.Telnet(HOST_IP)

t.read_until(b"Username:", timeout=0)
t.write(host_user.encode("ascii") + b"\n")
if password:
	t.read_until(b"Password:", timeout=0)
	t.write(password.encode("ascii") + b"\n")
print(t.read_all)
t.write(b"show switch\n")
t.write(b"logout\n")

print(t.read_all().decode("ascii"))
