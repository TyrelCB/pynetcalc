import ipaddress
import subprocess

try:
    import typer
except:
    subprocess.run('pip install "typer[all]"'.split())
    print('Dependancies Installed Please Re-Run')


app = typer.Typer()

@app.command()
def netinfo(
    ipv4:str= typer.Argument(..., help="IP address in CIDR Notation 172.16.0.0/12 or with Subnet Mask 10.0.0.0/255.0.0.0"), 
    octets:bool=True
    ):
    if ipv4 == None:
        prompt = '''
        Acceptable Formats:
            CIDR Notation 10.0.0.1/8
            With Netmask  10.0.0.1/255.0.0.0
        Enter an IPv4 address: '''
        ipv4 = input(prompt)
        if ipv4 == '': 
            ipv4 = '10.10.10.10/22'
            print(f"You Didn't Enter and IP! Using Default {ipv4}")
    ip = ipaddress.ip_interface(ipv4)
    print()
    print(f'IP is Private    : {ip.is_private} (RFC1918)')
    print(f'IP is Global     : {ip.is_global}')
    print(f'IP is Loopback   : {ip.is_loopback} (RFC3330)')
    print(f'IP is Multicast  : {ip.is_multicast} (RFC3171)')
    print(f'IP is Link Local : {ip.is_link_local} (APIPA RFC3927)')
    print()
    print(f'Decimal Value: {int(ip)}')
    print(f'HEX     Value: {hex(int(ip))}')
    if octets:
        binary = f'{int(ip):032b}'
        binary = f'{binary[:8]}.{binary[8:16]}.{binary[16:24]}.{binary[24:32]}'
        print(f'Binary  Value: {binary}')
        netmask = f'{int(ip.netmask):032b}'
        netmask = f'{netmask[:8]}.{netmask[8:16]}.{netmask[16:24]}.{netmask[24:32]}'
        print(f'Netmask      : {netmask}')
        anded = f'{int(ip)&int(ip.netmask):032b}'
        anded = f'{anded[:8]}.{anded[8:16]}.{anded[16:24]}.{anded[24:32]}'
        print(f'Bitwise AND  : {anded}')
        hostmask = f'{int(ip.hostmask):032b}'
        hostmask = f'{hostmask[:8]}.{hostmask[8:16]}.{hostmask[16:24]}.{hostmask[24:32]}'
        print(f'Hostmask     : {hostmask}')        
    else:
        print(f'Binary  Value: {int(ip):032b}')
        print(f'Netmask      : {int(ip.netmask):032b}')
        # print(f'Hostmask     : {int(ip.hostmask):032b}')
        print(f'Bitwise XOR  : {int(ip)^int(ip.netmask):032b}')
        print(f'Bitwise AND  : {int(ip)&int(ip.netmask):032b}')
    print()
    print(f'Network Address  : {ip.network[0]}')
    print(f'First Usable     : {ip.network[1]}')
    print(f'Last  Usable     : {ip.network[-2]}')
    print(f'Broadcast Address: {ip.network[-1]}')
    print(f'Subnet Mask      : {ip.netmask}')
    print(f'Host Mask        : {ip.hostmask}')
    print(f'Usable Addresses : {ip.network.num_addresses-2:,}')
    print()
    return ip

@app.command()
def subnet(
    ip_net:str= typer.Argument(...,help="IP Network Address in CIDR Notaion 172.16.0.0/24 or with Subnet Mask 172.16.0.0/255.255.255.0"), 
    new_prefix:str=typer.Option(...,help="New CIDR Prefix Length /27, Must be greater than the Original Prefix length")
    ):
    net = ipaddress.ip_interface(ip_net)
    diff = int(new_prefix[-2:]) - int(ip_net[-2:])
    net = list(net.network.subnets(prefixlen_diff=diff))
    print(f'Networks = {len(net)}')
    print(f'Hosts Per Network = {len(list(net[0].hosts())):,}')
    print(f'Subnet Mask {net[0].netmask}')
    for subnet in net:
        print(f'{net.index(subnet):>5} - {subnet}')
        # print(f'First Usable: {}')


if __name__ == "__main__":
    app()