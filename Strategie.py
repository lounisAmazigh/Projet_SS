#import soccersimulator
#import random
#from soccersimulator import SoccerTeam, SoccerMatch
from  soccersimulator import settings
from soccersimulator import BaseStrategy, SoccerAction 
from Tools import *
from Player_strat import *


class attaque_Strategy(BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self, "Attaque")
        
    def compute_strategy(self , state , id_team , id_player ):  
       
        Mystate = PlayerStateDecorator(state,id_team , id_player)
        return attaquant1(Mystate)
        
       
class defense_Strategy(BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self, "Defense")
        
    def compute_strategy(self , state , id_team , id_player ):
        Mystate = PlayerStateDecorator(state , id_team , id_player)
     
        if(id_team == 1):
             return defenseur1(Mystate)
        else:
            return defenseur2(Mystate)
         
           
class Test(BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self, "test")
        
    def compute_strategy(self , state , id_team , id_player ):
        Mystate = PlayerStateDecorator(state , id_team , id_player)
        
        if Mystate.can_shoot() == True : 
            return  Mystate.shoot_to_cage_t2()
        else:
            return  Mystate.suivre_bal() 
     
        return Mystate.shoot_to_cage_t1() + Mystate.suivre_bal()
 
class attaquant_de_pointe(BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self, "joueur 9")
        
    def compute_strategy(self , state , id_team , id_player ):
        Mystate = PlayerStateDecorator(state , id_team , id_player)   
        
        return attaque_pointe(Mystate)

class milieu(BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self, "joueur 10")
        
    def compute_strategy(self , state , id_team , id_player ):
        Mystate = PlayerStateDecorator(state , id_team , id_player) 

        return milieu_centre(Mystate)
        
class goal_strat(BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self, "joueur 1")
        
    def compute_strategy(self , state , id_team , id_player ):
        Mystate = PlayerStateDecorator(state , id_team , id_player) 
        
        if(Mystate.id_team == 1):
            return goal(Mystate)
        else:
            return goal2(Mystate)































                    
"""class MaStrategy(BaseStrategy):
      def __init__(self):
         BaseStrategy.__init__(self, "Basic")
         
      def compute_strategy(self, state, id_team, id_player):

          bal = state.ball.position
          p = state.player_state(id_team, id_player) 
         
          if  (p.position.distance(bal) < settings.PLAYER_RADIUS + settings.BALL_RADIUS):
              return shoot_bal(state , id_team ,id_player)
          else : 
              return suivre_bal(state , id_team, id_player)"""
              
              
              
              
              
              
              
              
              
              