import socket
server_port = 12000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', server_port))
server.listen(1)
print ("The server is ready to receive")
while 1:
	print ("Waiting ...")
	connection_socket, addr = server.accept()
	print ("Connection Accepted!")

	# Receives a sentence and options from client
	sentence = connection_socket.recv(2048).decode()
	print ("Message Received: " + sentence)
	optionsList = connection_socket.recv(2048).decode()
	print ("Options received: " + optionsList)

	# Store our responses in a list
	responses = []

	# Corresponding numbers from our choices indicate which if block statement is executed
	if "1" in optionsList:
		modifiedSentence = sentence.upper()
		responses.append(modifiedSentence)

	if "2" in optionsList:
		lowerSentence = sentence.lower()
		responses.append(lowerSentence)
	
	if "3" in optionsList:
		lengthOfSentence = len(sentence)
		responses.append(str(lengthOfSentence))
	
	if "4" in optionsList:
		vowelCount = 0
		tempSentence = sentence.lower()
		for character in tempSentence:
			if character in "aeiou":
				vowelCount += 1
		responses.append(str(vowelCount))
	
	if "5" in optionsList:
		wordCount = len(sentence.split())
		responses.append(str(wordCount))

	# Final message joins each response from the list and combines them into one string which gets sent back to the client
	finalMessage = "\n".join(responses) + "\n"
	connection_socket.send(finalMessage.encode())

	connection_socket.close()
