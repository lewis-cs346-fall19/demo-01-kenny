Author: Kenny McLaren
CSC 346, Fall 2019

Start by running net_server.py with the command:

	python net_server.py

Open a new terminal, connect to lectura, and run net_client.py with:
	
	python net_client.py

The client will prompt you to enter a single word.  When the word is entered, the client will send
the word to the server, receive the response, and print out what it received.  Both the server and
client will print about what they are doing during the process. The client will then prompt you for
another single word.  Enter another word to receive another response, or enter control+C to end.
