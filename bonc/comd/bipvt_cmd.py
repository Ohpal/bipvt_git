import socket
import comd.var

bipvt_socket_client = False


def connect_bipvt_socket():
    global bipvt_socket_client

    try:
        hosting = comd.var.bipvt_ip
        porting = int(comd.var.bipvt_port)

        bipvt_socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bipvt_socket_client.connect((hosting, porting))
        comd.var.bipvt_connect_status = True
        return True
    except Exception as ex:
        print('connect_bipvt_socket() Exception -> ', ex)
        comd.var.bipvt_connect_status = False
        return False


def bipvt_socket_data():
    try:
        connect_bipvt_socket()
        bipvt_datas = bipvt_socket_client.recv(500).decode().split()

        bipvt_data = bipvt_datas[1:-1]

        if len(bipvt_data) == 62:
            bipvt_data[0] = bipvt_casting(bipvt_data[0], 0.1)
            bipvt_data[1] = bipvt_casting(bipvt_data[1], 0.1)
            bipvt_data[2] = bipvt_casting(bipvt_data[2])
            bipvt_data[3] = bipvt_casting(bipvt_data[3], 0.1)
            bipvt_data[4] = bipvt_casting(bipvt_data[4], 0.1)
            bipvt_data[5] = bipvt_casting(bipvt_data[5])
            bipvt_data[6] = bipvt_casting(bipvt_data[6], 0.1)
            bipvt_data[7] = bipvt_casting(bipvt_data[7], 0.1)
            bipvt_data[8] = bipvt_casting(bipvt_data[8], 0.1)
            bipvt_data[9] = bipvt_casting(bipvt_data[9], 0.1)
            bipvt_data[10] = bipvt_casting(bipvt_data[10], 0.1)
            bipvt_data[11] = bipvt_casting(bipvt_data[11], 0.1)
            bipvt_data[12] = bipvt_casting(bipvt_data[12], 0.1)
            bipvt_data[13] = bipvt_casting(bipvt_data[13], 0.1)
            bipvt_data[14] = bipvt_casting(bipvt_data[14], 0.1)
            bipvt_data[15] = bipvt_casting(bipvt_data[15], 0.1)
            bipvt_data[16] = bipvt_casting(bipvt_data[16], 0.1)
            bipvt_data[17] = bipvt_casting(bipvt_data[17], 0.1)
            bipvt_data[18] = bipvt_casting(bipvt_data[18], 0.1)
            bipvt_data[19] = True if bipvt_casting(bipvt_data[19]) == 10 else False
            bipvt_data[20] = bipvt_casting(bipvt_data[20])
            bipvt_data[21] = bipvt_casting(bipvt_data[21])
            bipvt_data[22] = bipvt_casting(bipvt_data[22])
            bipvt_data[23] = bipvt_casting(bipvt_data[23])
            bipvt_data[24] = bipvt_casting(bipvt_data[24])
            bipvt_data[25] = bipvt_casting(bipvt_data[25])
            bipvt_data[26] = bipvt_casting(bipvt_data[26], 0.1)
            bipvt_data[27] = bipvt_casting(bipvt_data[27], 0.1)
            bipvt_data[28] = bipvt_casting(bipvt_data[28], 0.1)
            bipvt_data[29] = bipvt_casting(bipvt_data[29], 0.1)
            bipvt_data[30] = bipvt_casting(bipvt_data[30], 0.1)
            bipvt_data[31] = bipvt_casting(bipvt_data[31], 0.1)
            bipvt_data[32] = True if bipvt_casting(bipvt_data[32]) == 10 else False
            bipvt_data[33] = bipvt_casting(bipvt_data[33], 0.1)
            bipvt_data[34] = True if bipvt_casting(bipvt_data[34]) == 10 else False
            bipvt_data[35] = bipvt_casting(bipvt_data[35], 0.1)
            bipvt_data[36] = bipvt_casting(bipvt_data[36])
            bipvt_data[37] = bipvt_casting(bipvt_data[37])
            bipvt_data[38] = bipvt_casting(bipvt_data[38])
            bipvt_data[39] = bipvt_casting(bipvt_data[39])
            bipvt_data[40] = bipvt_casting(bipvt_data[40])
            bipvt_data[41] = bipvt_casting(bipvt_data[41])
            bipvt_data[42] = bipvt_casting(bipvt_data[42])
            bipvt_data[43] = bipvt_casting(bipvt_data[43])
            bipvt_data[44] = bipvt_casting(bipvt_data[44])
            bipvt_data[45] = bipvt_casting(bipvt_data[45])
            bipvt_data[46] = bipvt_casting(bipvt_data[46])
            bipvt_data[47] = bipvt_casting(bipvt_data[47])
            bipvt_data[48] = bipvt_casting(bipvt_data[48])
            bipvt_data[49] = bipvt_casting(bipvt_data[49])
            bipvt_data[50] = bipvt_casting(bipvt_data[50])
            bipvt_data[51] = bipvt_casting(bipvt_data[51])
            bipvt_data[52] = bipvt_casting(bipvt_data[52])
            bipvt_data[53] = bipvt_casting(bipvt_data[53])
            bipvt_data[54] = bipvt_casting(bipvt_data[54])
            bipvt_data[55] = bipvt_casting(bipvt_data[55])
            bipvt_data[56] = bipvt_casting(bipvt_data[56])
            bipvt_data[57] = bipvt_casting(bipvt_data[57])
            bipvt_data[58] = bipvt_casting(bipvt_data[58])
            bipvt_data[59] = bipvt_casting(bipvt_data[59])
            bipvt_data[60] = bipvt_casting(bipvt_data[60])
            bipvt_data[61] = bipvt_casting(bipvt_data[61])

            if bipvt_data[2] > 100 or bipvt_data[5] > 360 or bipvt_data[18] < 0 or bipvt_data[18] > 1000:
                raise Exception('Trash Data >> ', bipvt_datas)
            else:
                comd.var.bipvt_temp_data = bipvt_data
                return bipvt_data

            comd.var.bipvt_socket_client.close()
        else:
            pass

    except Exception as ex:
        print('bipvt_socket_data() Exception -> ', ex)


def bipvt_casting(data, unit=1):
    if '-' in data:
        data = bipvt_casting(data.split('-')[1], -unit)
        return data
    else:
        data = int(data) * unit
        return round(data, 1)
