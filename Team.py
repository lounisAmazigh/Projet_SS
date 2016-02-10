from soccersimulator import SoccerTeam
from Strategie import *
from soccersimulator import  Player 

team1 = SoccerTeam("JSK",[Player("Fonceur",attaque_basic)])
team1 = SoccerTeam("JSK",[Player("Fonceur",attaque_basic),Player("G1",goal_strat)])
team4 = SoccerTeam("JSK",[Player("Ray",milieu),Player("Ria",defense_Strategy),Player("Dia",attaque_Strategy),Player("Dou",goal_strat)])
#team1 = SoccerTeam("JSK",[Player("BEL",milieu),Player("BEL",defense_Strategy),Player("BEL",attaque_Strategy),Player("BEL",goal_strat)])
#team2 = SoccerTeam("JSsK",[Player("BEL",attaque_basic),Player("BEL",attaque_basic),Player("BEL",attaque_Strategy),Player("BEL",goal_strat)])
