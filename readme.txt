C50 Final 

I ended up creating two separate programs after I realized that I had bit off more than I could chew for my project. My initial goal was to create a network connected game of Tic Tac Toe to try and teach myself about socket programming and threading. I completed the rough framework of the tic tac toe game and began working on trying to make a client/server version of the game. I quickly realized I was in over my head given the time constraints as such the Tic Tac Toe game is somewhat simplistic.

I still wanted to learn a little bit about sockets so I remembered there used to be a service called Quote of the Day, like FTP, that you could connect to and get a random quote. I don't think they exist anymore since it's rather outdated and probably a security concern. I did some research and found the speficiation here:

https://tools.ietf.org/rfc/rfc865.txt

So my second program is a Random Quote client/server that is in the same vain as the Quote of the Day Protocol outlined in the RFC above.


Tic Tac Toe:

A simple text based game of tic tac toe against the computer contained in two files, tic_tac.py and a header file helper.py that contains the ascii header and board as well as some functions. The game prompts the user to choose X or O and proceeds to choose who goes first randomly 

Use:
./tic_tac or python tic_tac.py

To Implement:

1. Improve the computer's AI, current logic check's to see if center square is empty and goes there, if not another random value is returned, checks if occupied, if free goes there.
	A. First check would be to see if the next move can win the game, if so the computer should go there first.
	B. Second check should be to see if computer move can block opposing player from winning
	C. If computer can't win on next turn or block player (2 spaces), choose from available spaces with a priority to center, then corner spots, lastly middle spaces on perimeter.

2. Allow two players to play against each other vs just against the computer

--------------------------------------------------------------------------------------------------------------------------------------

Quote of the Day

A simple implementation of the QoTD service. Server opens a file named "quotes.txt" and reads each line into a list. Server will take a command line input of a port number or prompt the user if none is provided suggesting 17 (per the RFC). Server will display host name and ip address and atttempt open a socket and bind & listen to it. On client connection the server with create a new thread to handle each connection, so even though the client disconnects after 2 seconds, theoretically it could handle multiple connnections. 

The server randomly selects a quote using the randint() function based on the number of quotes in the list, encodes it as UTF-8 and sends it.

The client progam takes 2 optional command parameters for target port number and server address. Without any arguments client assumes that the server address is local and port is default for QotD (17). Client attempts to open socket and connect to the server address and port number, as well as creates a buffer of 1024bytes to receive the quote. The quote is decoded and printed to the screen then the connection is closed.

To Implement:

1. Allow client program to request another quote from the server without disconnecting/reconnecting.