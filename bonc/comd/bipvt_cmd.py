import socket
import comd.var

def soc_reconnect():
    print("socket connection lost... reconnecting")
    soc_connection_try = 0
    connected = False
    while not connected:
        soc_connection_try = soc_connection_try + 1
        if soc_connection_try > 30:
            soc_connection_try = 0
            print("still fail_to_connect")
        try:
            comd.read_cmd.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            comd.read_cmd.soc.connect((comd.var.server_ip, comd.var.server_port))

            connected = True
            print("re-connection successful")

            comd.var.soc_fail_count = 0
            comd.var.soc_connect_fail = False

        except socket.error:
            time.sleep(2)
            print("re-connection fail, so re-connect start")
