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
    prefix = "fichier"
    if len(sys.argv)>1:
        prefix = sys.argv[1]
        
    team1 = SoccerTeam("JSK",[Player("10",attaquant_gauche),Player("9",def_gauche),Player("4",keytest),Player("1",goal_strat)])
    team2 = SoccerTeam("JSK",[Player("10",attaquant_gauche),Player("9",def_gauche),Player("4",att_def_droit),Player("1",goal_strat)])
    
    match = SoccerMatch(team1,team2,2000)
    show(match)
    keytest.write(prefix+".exp",True)
