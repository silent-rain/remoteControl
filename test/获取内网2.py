import os


def get_local_ip():
    result = []
    ipv4 = None
    ipv6 = None
    for x in os.popen('ipconfig'):
        result.append(x)
    # print(result)
    for x in range(len(result)):
        # print(result[x + 2][-2])
        if 'IPv4' in result[x] and result[x + 2][-2] != ' ':
            ipv4 = result[x][result[x].find(':') + 2:-1]
        elif 'IPv6' in result[x] and result[x + 3][-2] != ' ':
            ipv6 = result[x][result[x].find(':') + 2:-1]
    return ipv4, ipv6


print(get_local_ip())
