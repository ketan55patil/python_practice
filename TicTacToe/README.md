[![codecov](https://codecov.io/gh/ketan55patil/python_practice/branch/master/graph/badge.svg)](https://codecov.io/gh/ketan55patil/python_practice/branch/master)

# Create a Tic Tac Toe game.

## Requirements:
1. 2 players should be able to play the game (both sitting at the same computer)
1. The board should be printed out every time a player makes a move
1. You should be able to accept input of the player position and then place a symbol on the board
1. Game is played between 2 players until 
   1. one of them wins
   1. game ends up in a draw
   1. one of them decides to exit by pressing '0'.

## Sample output:
```
$ pipenv run python3 ticTacToe_V2.py
  1  |  2  |  3  
  4  |  5  |  6  
  7  |  8  |  9  
Enter where do you want to place x: 1
  x  |  2  |  3  
  4  |  5  |  6  
  7  |  8  |  9  
Enter where do you want to place o: 5
  x  |  2  |  3  
  4  |  o  |  6  
  7  |  8  |  9  
Enter where do you want to place x: 9
  x  |  2  |  3  
  4  |  o  |  6  
  7  |  8  |  x  
Enter where do you want to place o: 7
  x  |  2  |  3  
  4  |  o  |  6  
  o  |  8  |  x  
Enter where do you want to place x: 3
  x  |  2  |  x  
  4  |  o  |  6  
  o  |  8  |  x  
Enter where do you want to place o: 6
  x  |  2  |  x  
  4  |  o  |  o  
  o  |  8  |  x  
Enter where do you want to place x: 2
Player x won!!!
  x  |  x  |  x  
  4  |  o  |  o  
  o  |  8  |  x  
```
