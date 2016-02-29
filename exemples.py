#from strategies import FonceurStrategy, DefenseStrategy, RandomStrategy
from decisiontree import DTreeStrategy
from soccersimulator import SoccerMatch, show, SoccerTeam,Player,KeyboardStrategy
from decisiontree import gen_features
import cPickle
from Strategie import *


#### Arbres de decisions

tree = cPickle.load(file("./fichier.pkl"))
dic = {"def_gauche":def_gauche,"def_droit":deffa_droit_basic,"att_gauche":att_gauche_basic , "att_droit":att_droit_basic}
treeStrat = DTreeStrategy(tree,dic,gen_features)

