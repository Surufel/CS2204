#config values.

#random number range, default range is from 0 ~ 9
RANDOM_RANGE = [0, 9]
#2|10|16 (binary, deciminal or hexadecimal)
NUMBER_SYSTEM = 16
#True|False
SHOW_CODE_DIGIT = True
#players' name.
PLAYER_NAME = ['Player 1', 'Player 2']
#['machine'|'human', 'machine'|'human']
PLAYER_TYPE = ['Machine', 'Machine']
#PLAYER_TYPE = ['machine', 'machine']
#PLAYER_TYPE = ['machine', 'human']
# I think player1 was human and is now machine. Commented out on line 13 is default.
# Update: The bug was the wrong position of Player 1 and Player 2. So ... line 16 means to say that player1 is machine and well, player0 too.
