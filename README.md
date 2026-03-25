#Project
A mini 2-player gaming hub

#Initializing	
bash main.sh

#File Structure
-README
-hub/
   -main.sh
   -game.py
   -leaderboard.sh
   -game.py/
      -tictactoe.py
      -othello.py
      -connect4.py
   -users.tsv
   -history.csv

#Files Description

main.sh     - 1) authenticates a user login or creates a new user
              2) calls game.py if authentication is succesful
users.tsv   - contains usernames and *hash passwords
game.py     -
history.csv - contains details of game played ,date,winner,loser 
