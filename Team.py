from soccersimulator import SoccerTeam
from Strategie import *
from soccersimulator import  Player 

#team1 = SoccerTeam("JSK",[Player("Fonceur",milieu) , Player("Fonceur",defense_Strategy) , Player("1",goal_strat) , Player("1",goal_strat)])
#team4 = SoccerTeam("JSK",[Player("Fonceur",defense_Strategy),Player("9",attaque_Strategy)])
team1 = SoccerTeam("JSK",[Player("Fonceur",P1_fonceur) )
team4 = SoccerTeam("JSK",[Player("10",defense_Strategy),Player("9",attaque_Strategy),Player("4",milieu),Player("1",goal_strat)])
team2 = SoccerTeam("JSK",[Player("Fonceur",T2_All) , Player("4",defense_Strategy)])
