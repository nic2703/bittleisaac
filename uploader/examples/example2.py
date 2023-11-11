from ..upload_run import * 

pi_host = '192.168.1.111'
pi_port = 22
pi_username = 'username'
pi_password = 'password'
pi_path = 'Documents/autorun/'
filename = ['dance.py', 'ardSerial.py', 'SerialCommunication.py']

upload_run(pi_path, filename)
# filename is usually instructions.py. runscript.py is always automatically uploaded. 