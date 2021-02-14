from netmiko import ConnectHandler

if __name__=="__main__":
    a={
        'device_type':'cisco_ios',
        'ip':'192.168.50.100',
        'username':'cisco',
        'password':'cisco123!',}
    sshCli=ConnectHandler(**a)
    output= sshCli.send_command("sho ip int brie")
    print(output)
    string="CIAO MONDO!"
    string.replace('?','!')
    print(string)
    config_commands=['interface loopback1','ip address 1.1.1.1 255.255.255.255']
    ciccio=sshCli.send_config_set(config_commands)
    print('\n',ciccio)
