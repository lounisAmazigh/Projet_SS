from soccersimulator import SoccerTeam
from Strategie import *
from soccersimulator import  Player 

team1 = SoccerTeam("JSK",[Player("def",defense_Strategy()),Player("att",attaque_Strategy())])
team2 = SoccerTeam("USMA",[Player("t2j1",Test()),Player("az",defense_Strategy())])