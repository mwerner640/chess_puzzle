## Chess Puzzle

This code spawns a random chess board and tells you where the warden hid the key for the following classic math puzzle: 

The warden has allowed you and a fellow prisoner a chance to escape prison if you can solve a puzzle. He has placed 64 coins
at random on a chess board. Under one of these coins, he has placed a small key. You are required to flip 
one coin on the board and you must do so in such a way that your fellow prisoner can identify which of the coins the key is under.

This program calculates a way to defeat the warden following my method. We map each square on the board to coordinates in a six-dimensional modulo two space (for further  We then sum the coordinates of all squares whose coin is flipped heads to obtain a sum coordinate. We then find the coordinate of which coin to flip, by adding a one to \<0, 0, 0, 0, 0, 0\> in each dimension where the sum coordinate does not match the key coordinate. We then flip that coordinate behind the scenes and resum to verify.

#### To run
`FLASK_APP=server.py flask run`

You must have python and flask installed. The server will open on localhost:5000/

#### How I arrived at this method

As this problem is extremely complex I start with a two state version:

|        0       |       1      | 
| :------------- | :----------: | 
|        T       |       H      |

We are in a modulo-2 world where boxes have weight 0 or 1. If we let tails indicate 0 and heads indicate 1, this state indicates the key should be under box 1. If the key is under box 1, we can flip box 0  without affecting the sum. If it is under box 1 we can change the state to what we need flipping box 1. You can try this with all 8 coin/key positions to convince yourself this method works. Now to expand. My first impulse was to expand to modulo-3, but this has various issues. After trying unsuccessfully to find a new method other than the modulo worlds, I realised I didn't actually need the 3 case. I skipped it to expand further to a box:

|     |       0      |       1      |
| :-- | :----------: | -----------: |
|  0  |       H      |       H      |
|  1  |       H      |       T      |

When we expand out into two dimensions of the modulo-2 world, our last solution still holds. In the above scenario, if the key is under \<0, 1\>, we need to flip \<1, 0\> to change the sum from \<1, 1\> to \<0, 1\>. 

Now, you can visualize three dimensions of the modulo-2 world. Assure yourself this works.


With our chessboard we are working with six dimensions of the modulo-2 world.

#### Thoughts for further implementations

The current website does not flip the indicated coin over in the visual. The front-end code ought to be refactored to do so, perhaps out of HTML.
