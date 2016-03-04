from soccersimulator import SoccerTeam
from Strategie import *
from soccersimulator import  Player 
from decisiontree import DTreeStrategy, gen_features
import cPickle
#team1 = SoccerTeam("JSK",[Player("Fonceur",milieu) , Player("Fonceur",defense_Strategy) , Player("1",goal_strat) , Player("1",goal_strat)])
#team4 = SoccerTeam("JSK",[Player("Fonceur",defense_Strategy),Player("9",attaque_Strategy)])
#team4 = SoccerTeam("JSK",[Player("Fonceur",P1_fonceur)])

team1 = SoccerTeam("JSK",[Player("9",P1_fonceur)])

team2 = SoccerTeam("JSK",[Player("9",P1_fonceur) , Player("1",defense_Strategy)])

team4 = SoccerTeam("JSK",[Player("10",attaquant_gauche),Player("9",def_gauche),Player("4",att_def_droit),Player("1",goal_strat)])


##### TEAM IA 

#### Arbres de decisions

tree = cPickle.load(file("./fichier.pkl"))
dic = {"def_gauche":def_gauche,"def_droit":deffa_droit_basic,"att_gauche":att_gauche_basic , "att_droit":att_droit_basic , "foncer":P1_fonceur}
treeStrat = DTreeStrategy(tree,dic,gen_features)

teamIA= SoccerTeam("IATEAM",[Player("IATREE",treeStrat)  , Player("9",def_gauche) , Player("1",goal_strat) , Player("10",attaquant_gauche) ])

