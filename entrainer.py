""" Permet de jouer et d'entrainer une strategie
    * changer les strategies ajoutees
    * utilisation : python entrainer prefix_fichier_exemple
    par defaut ajoute au fichier d'exemples sil existe deja
    (extension : .exp pour le fichier exemple)
"""

from soccersimulator import SoccerMatch, show, SoccerTeam,Player,KeyboardStrategy
from Strategie import *
import sys

if __name__=="__main__":
    prefix = "goal"
    if len(sys.argv)>1:
        prefix = sys.argv[1]
    #team 4
    team1 = SoccerTeam("JSK",[Player("10",attaquant_gauche),Player("9",def_gauche),Player("4",att_def_droit),Player("1",keygoal)])
    team2 = SoccerTeam("JSK",[Player("10",attaquant_gauche),Player("9",def_gauche),Player("4",att_def_droit),Player("1",goal_strat)])
    
    #Team 2
   # team1 = SoccerTeam("JSK",[Player("10",keyatt),Player("9",defense_Strategy)])
    #team2 = SoccerTeam("JSK",[Player("9",foncer) , Player("1",defense_Strategy)])
    
    #Team1
    #team1 = SoccerTeam("JSK",[Player("9",milieu_deffa) , Player("1",milieu_deffa)])
    #team2 = SoccerTeam("JSK",[Player("9",foncer) , Player("1",goal_strat) ])
    
  
    
    
    match = SoccerMatch(team1,team2,4000)
    show(match)
    keyatt.write(prefix+".exp",True)
    keygoal.write(prefix+".exp",True)

#"""keyatt
#keygoal