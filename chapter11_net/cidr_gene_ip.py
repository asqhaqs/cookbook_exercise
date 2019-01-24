import ipaddress

net = ipaddress.ip_network('123.45.67.64/27')
print(net)

for a in net:
    print(a)

print(net.num_addresses)
print(net[0])

a = ipaddress.ip_address("123.45.67.69")
print(a in net)