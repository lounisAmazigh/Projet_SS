#import soccersimulator
#import random
#from soccersimulator import SoccerTeam, SoccerMatch
from  soccersimulator import settings
from soccersimulator import BaseStrategy, SoccerAction, KeyboardStrategy
from Tools import *
from Player_strat import *


class Strat(BaseStrategy):
    def __init__(self,comportement,name):
        BaseStrategy.__init__(self,name)
        self.comportement = comportement
    def compute_strategy(self, state, id_team, id_player):
        s_miroir = state
        if id_team==1 :
            Mystate = PlayerStateDecorator(s_miroir,id_team , id_player)
            return self.comportement(Mystate)
        else :
            s_miroir = miroir_st(state)
            Mystate = PlayerStateDecorator(s_miroir,id_team , id_player)
            return miroir_sa(self.comportement(Mystate))
    
keyatt = KeyboardStrategy()
keygoal = KeyboardStrategy()
keydef = KeyboardStrategy()

    


goal_strat = Strat(goal , "1")
attaque_Strategy = Strat(attaque_pointe,"attaquant")
defense_Strategy = Strat(defenseur1,"def")
milieu = Strat(milieu_centre , "mil")      
milieu_deffa = Strat(milieu_def , "milOf")
test = Strat(test1, "test")
P1_fonceur = Strat(attaquant1 , "foncer")
T2_All = Strat(player_go , "tout")
attaquant_gauche = Strat(attaque_gauche , "7")
att_def_droit = Strat(marcelo , "att_def_droit")
def_gauche = Strat(deff_gauche , "3")
foncer = Strat(foncer , "9")
tire_alea = Strat(tire_aleatoire,"tire_alea")


#BASIC 
att_droit_basic = Strat(attaquant_droit_basic , "att_droit")
att_gauche_basic = Strat(attaquant_gauche_basic , "att_gauche")
deffa_droit_basic = Strat(deff_droit_basic , "def_droit")
deffa_gauche_basic = Strat(deff_gauche_basic , "def_gauche")

# ATT DEF GAUCHE
keyatt.add("d" ,   P1_fonceur ) 
keyatt.add("s" , att_gauche_basic  )
keyatt.add("z" , att_droit_basic  )           
keyatt.add("q" , deffa_gauche_basic ) 
keyatt.add("a" ,  deffa_droit_basic ) 

# Goal Strategie 
keygoal.add("g" , goal_strat)
keygoal.add("f" , defense_Strategy)
keygoal.add("h" , tire_alea)
  
#DEF STRATEGIE
  
keydef.add("d" ,   P1_fonceur ) 
keydef.add("s" , att_gauche_basic  )
keydef.add("z" , att_droit_basic  )    
keydef.add("q" , deffa_gauche_basic ) 
keydef.add("a" ,  deffa_droit_basic )   
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
#Keytest.add("d" , P1_fonceur )  
  
