import soccersimulator
import math
import random
from  soccersimulator import settings
from soccersimulator import BaseStrategy, SoccerAction 
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player , SoccerTournament
class RandomStrategy (BaseStrategy):
	def __init__ (self) :
	   BaseStrategy.__init__(self, "Random" )
	def compute_strategy (self, state, id_team, id_player):
	   return SoccerAction(Vector2D.create_random(),
			       Vector2D.create_random())
          
       ############### suivre la balle #################################"
def suivre_bal( state , id_team, id_player):
    
    bal = state.ball.position
    p = state.player_state(id_team, id_player)                
    return SoccerAction(bal - p.position,Vector2D(x=0,y=0))
      
    ###################################################################
    
    ###################### tirer la balle #############################
def shoot_bal( state , id_team, id_player):
     
     bal = state.ball.position
     p = state.player_state(id_team, id_player)
     if( id_team == 1):
         return SoccerAction(bal-p.position ,Vector2D(settings.GAME_WIDTH , (settings.GAME_HEIGHT)/2) - p.position )
     else :
         return SoccerAction(bal-p.position, Vector2D(0, (settings.GAME_HEIGHT)/2) - p.position)
    ####################################################################
         
############################ tire d'un defenseur ###############################
         
def shoot_bal_def(state, id_team, id_player):
    
    bal = state.ball
    p = state.player_state(id_team, id_player)
    
    if( id_team == 1):
        
        return SoccerAction(bal.position-p.position ,Vector2D(settings.GAME_WIDTH , (settings.GAME_HEIGHT)/2 , angle =10) - p.position )
    else :
        a = random.random()*math.pi 
        v = Vector2D(angle = a , norm = 20)
        return SoccerAction(bal.position-p.position, v)
        
    ######################################################################################
        
############################## retour a une position donnee ##########################
def retour_position( state , id_team , id_player ,v):
        return SoccerAction(v-state.player_state(id_team, id_player).position,Vector2D())

##########################################################################################

         
class MaStrategy(BaseStrategy):
      def __init__(self):
         BaseStrategy.__init__(self, "Basic")
         
      def compute_strategy(self, state, id_team, id_player):

          bal = state.ball.position
          p = state.player_state(id_team, id_player) 
         
          if  (p.position.distance(bal) < settings.PLAYER_RADIUS + settings.BALL_RADIUS):
              return shoot_bal(state , id_team ,id_player)
          else : 
              return suivre_bal(state , id_team, id_player)
              
class defense_Strategy(BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self, "Defense")
        
    def compute_strategy(self , state , id_team , id_player ):
        bal = state.ball.position
        p= state.player_state(id_team , id_player)
        
        if(id_team == 1):
            if( bal.x < settings.GAME_WIDTH / 2 ) :
                if(( p.position.distance(bal) < settings.PLAYER_RADIUS + settings.BALL_RADIUS)) :
                    return shoot_bal(state , id_team , id_player)
                else: 
                    return suivre_bal(state,id_team,id_player)
            else:
                if(p.position.x > settings.GAME_WIDTH / 4) :
                   return retour_position( state , id_team , id_player , Vector2D(0,settings.GAME_HEIGHT/2.))
                else : 
                    return SoccerAction(Vector2D(0,(bal.y -p.position.y),Vector2D()))
 
        else:
              if( bal.x > settings.GAME_WIDTH / 2 ) :
                if(( p.position.distance(bal) < settings.PLAYER_RADIUS + settings.BALL_RADIUS)) :
                    #return shoot_bal(state , id_team , id_player)
                    return shoot_bal_def(state, id_team, id_player)
                else: 
                    return suivre_bal(state,id_team,id_player)
              else:
                  if(p.position.x < settings.GAME_WIDTH *3/ 4) :
                      return retour_position( state , id_team , id_player , Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.))
                  else : 
                    return SoccerAction(Vector2D(0,(bal.y -p.position.y),Vector2D()))
                    
                    
class attaque_Strategy(BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self, "Attaque")
    def compute_strategy(self , state , id_team , id_player ):
        bal = state.ball.position
        p= state.player_state(id_team , id_player)
        if(id_team == 1):
            if( bal.x >= settings.GAME_WIDTH / 2 ) :
                if(( p.position.distance(bal) < settings.PLAYER_RADIUS + settings.BALL_RADIUS)) :
                    return shoot_bal(state , id_team , id_player)
                else: 
                    return suivre_bal(state,id_team,id_player)
            else:
                if(p.position.x < settings.GAME_WIDTH / 2) :
                   return retour_position( state , id_team , id_player , Vector2D(0,settings.GAME_HEIGHT/2.))
                else : 
                    return SoccerAction(Vector2D(0,(bal.y -p.position.y),Vector2D()))
                    
        else :
            return SoccerAction()
       
        

team1 = SoccerTeam("JSK",[Player("def",defense_Strategy()),Player("att",MaStrategy())])
team2 = SoccerTeam("USMA",[Player("t2j1",MaStrategy()),Player("az",defense_Strategy())])

match = SoccerMatch(team1,team2,1000)
soccersimulator.show(match)

