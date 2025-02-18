import socket
server_name = '127.0.0.1'
server_port = 12000

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((server_name, server_port))

# Options client can give to server
print ('1.) Conversion to Upper-Case characters | ')
print ('2.) Conversion to Lower-Case characters | ')
print ('3.) Length of the String | ')
print ('4.) Count vowels | ')
print ('5.) Count words | ')

# Inputs for sentence and options
sentence = input('First, type in a string that you want to modify/want more information on: ')
client.send(sentence.encode())
optionsList = input('Next, type in the options that you want (Format: #,#,#,#,#): ')
client.send(optionsList.encode())

# Response is received back from the server
response = client.recv(2048).decode()

# Prints each response on its own line for the client to read easily
for i, line in enumerate(response.strip().split("\n"), start=1):
    print(f"{i}.) {line}")

client.close()
