#import soccersimulator
import math
import random
from  soccersimulator import settings
from soccersimulator import SoccerAction 
from soccersimulator import Vector2D

class PlayerStateDecorator : 
    def __init__(self , state , id_team , id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player 
        
    def position_bal(self) : 
        return self.state.ball.position
        
    def position_player(self):
        return self.state.player_state(self.id_team, self.id_player).position  
        
    def no_shoot(self):
        return Vector2D(x=0,y=0)
    
    def stop(self):
        return SoccerAction()
        
    def distance_of_bal(self):
        return self.state.player_state(self.id_team, self.id_player).position.distance(self.state.ball.position)
        
    def can_shoot(self):
        if(self.distance_of_bal() < settings.PLAYER_RADIUS + settings.BALL_RADIUS):
            return True
        else :
            return False
 
    def shoot_to_cage_t1(self):
        if self.can_shoot() == True:
            return SoccerAction( self.position_bal()-self.position_player() , Vector2D(settings.GAME_WIDTH , (settings.GAME_HEIGHT)/2) - self.position_player())
        else :
            return SoccerAction(self.position_bal()-self.position_player(),self.no_shoot())
            
    def shoot_to_cage_t2(self)  : 
        if self.can_shoot() == True:
            return SoccerAction( self.position_bal()-self.position_player() , Vector2D(0, (settings.GAME_HEIGHT)/2) - self.position_player())
        else :
            return SoccerAction(self.position_bal()-self.position_player(),self.no_shoot())
            
    def shoot_rand(self) :
        a = random.uniform(2,4) 
        u = (self.position_player().x*self.position_player().x) + (settings.GAME_HEIGHT/2 - self.position_player().y)*(settings.GAME_HEIGHT/2 - self.position_player().y) 
        d = math.sqrt(u)
        v = Vector2D(angle = a , norm = d ) 
        if self.can_shoot() == True:
            return SoccerAction(self.position_bal()-self.position_player(), v)
        else :
            return SoccerAction(self.position_bal()-self.position_player(),self.no_shoot())
            
    def retour_position(self, v):
         return SoccerAction(v - self.position_player(),Vector2D())
        
    def suivre_bal(self) : 
        return SoccerAction(self.position_bal()-self.position_player() , self.no_shoot())
        
    def suivre_bal_en_y(self) :
        return SoccerAction(Vector2D(0,(self.position_bal().y - self.position_player().y)),Vector2D())
    
   # def suivre_bal_en_y_t2(self) :
    #    return SoccerAction(Vector2D(0,(self.position_bal().y - self.position().y)),Vector2D())
        
    def shoot_bal( self):
        if(self.can_shoot() == True):
            return self.shoot_to_cage_t1() 
        else :
            return self.stop()
    
    def shoot_bal_def(self) : 
        if(self.can_shoot() == True):
            return self.shoot_rand() 
        else :
            return self.stop()
            
            
            
z = """      ############### suivre la balle #################################"
def suivre_bal( state , id_team, id_player):
    
    bal = state.ball.position # position bal 
    p = state.player_state(id_team, id_player)    # position joueur             
    return SoccerAction(bal - p.position,Vector2D(x=0,y=0)) # no shoot
      
    ###################################################################
    
    ###################### tirer la balle #############################
"""
u = """def shoot_bal(mystate):
    if (mystate.id_team==1):
        if mystate.peux_shooter():
            return mystate.shoot_vers_but()"""
            

zz = """def shoot_bal( state , id_team, id_player):
     "
     bal = state.ball.position
     p = state.player_state(id_team, id_player)
     if( id_team == 1):
         if(( p.position.distance(bal) < settings.PLAYER_RADIUS + settings.BALL_RADIUS)) : #distance of bal + can_shoot
             return SoccerAction(bal-p.position ,Vector2D(settings.GAME_WIDTH , (settings.GAME_HEIGHT)/2) - p.position ) #shoot vers cage
         else :
             return SoccerAction() #stop
     else :
         return SoccerAction(bal-p.position, Vector2D(0, (settings.GAME_HEIGHT)/2) - p.position)
    ####################################################################       
############################ tire d'un defenseur ###############################
       
def shoot_bal_def(state, id_team, id_player):
    
    bal = state.ball
    p = state.player_state(id_team, id_player)
    
    if( id_team == 1):
        a = random.uniform(0,1)-0.5 
        u = (p.position.x*p.position.x) + (settings.GAME_HEIGHT/2 - p.position.y)*(settings.GAME_HEIGHT/2 - p.position.y) 
        d = math.sqrt(u)
        v = Vector2D(angle = a , norm = d )
        return SoccerAction(bal.position-p.position, v)
    else :
        a = random.uniform(2,4) 
        u = (p.position.x*p.position.x) + (settings.GAME_HEIGHT/2 - p.position.y)*(settings.GAME_HEIGHT/2 - p.position.y) 
        d = math.sqrt(u)
        v = Vector2D(angle = a , norm = d )
        return SoccerAction(bal.position-p.position, v)
        
    ######################################################################################
        
############################## retour a une position donnee ##########################
def retour_position( state , id_team , id_player ,v):
        return SoccerAction(v-state.player_state(id_team, id_player).position,Vector2D())

########################################################################################## """