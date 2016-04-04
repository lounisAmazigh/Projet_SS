from soccersimulator import SoccerTeam
from Strategie import *
from soccersimulator import  Player 
from decisiontree import DTreeStrategy, gen_features
import cPickle
import os


team1 = SoccerTeam("JSK",[Player("10",test)])

team2 = SoccerTeam("JSK",[Player("10",goal_strat)])

#team2 = SoccerTeam("JSK",[Player("9",milieu) , Player("4",defense_Strategy)])

team4 = SoccerTeam("JSK",[Player("9",attaquant_gauche),Player("4",def_gauche),Player("7",att_def_droit),Player("1",goal_strat)])


##### TEAM IA 
fn = os.path.join(os.path.dirname(os.path.realpath(__file__)),"attaquant.pkl")
fn2 = os.path.join(os.path.dirname(os.path.realpath(__file__)),"goal.pkl")
fn3 = os.path.join(os.path.dirname(os.path.realpath(__file__)),"defence.pkl")
#### Arbres de decisions

tree = cPickle.load(file(fn))
dic = {"def_gauche":def_gauche,"def_droit":deffa_droit_basic,"att_gauche":att_gauche_basic , "att_droit":att_droit_basic , "foncer":P1_fonceur}
treeStrat = DTreeStrategy(tree,dic,gen_features)

### Arbre de decisions pour le goal 
tree1 = cPickle.load(file(fn2))
dic_goal = {"def":defense_Strategy,"1":goal_strat,"tire_alea":tire_alea}
treeGoal = DTreeStrategy(tree1,dic_goal,gen_features)

## Arbre de decision pour la deffence
tree2 = cPickle.load(file(fn3))
treeDef = DTreeStrategy(tree2,dic,gen_features)

teamIA= SoccerTeam("IATEAM",[Player("IA_A",treeStrat)  , Player("IA_D",treeDef)   ])
teamIA1= SoccerTeam("jsk",[Player("IA_A",foncer) ])
teamIA2= SoccerTeam("jsk",[Player("IA_A",treeStrat) ,Player("7",defense_Strategy) ])
teamIA4= SoccerTeam("jsk",[Player("IA_A",treeStrat) ,Player("7",att_def_droit)  , Player("9",def_gauche) , Player("IA_G",treeGoal)  ])