from sbituploader import * 

pi_host = '192.168.1.111'
pi_port = 22
pi_username = 'username'
pi_password = 'password'
pi_path = 'Documents/autorun/'
filename = 'helloworld.py'

sbitupload(pi_host, pi_port, pi_username, pi_password, pi_path, filename)
# filename is usually instructions.py. runscript.py is always automatically uploaded. 