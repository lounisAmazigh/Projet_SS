#import soccersimulator
import math
import random
from  soccersimulator import settings
from soccersimulator import SoccerAction 
from soccersimulator import Vector2D

        
        ################ MIROIR    #####################

def miroir_p(p):       # miroir position
    return Vector2D( settings.GAME_WIDTH - p.x,p.y)

        # miroir vecteur
def miroir_v(v):
    return Vector2D(-1*v.x , v.y)  
    
def miroir_sa(action):
    return SoccerAction(miroir_v(action.acceleration),miroir_v(action.shoot))
    
def miroir_st(state):
    res = state.copy()
    res.ball.position = miroir_p(state.ball.position)
    res.ball.vitesse = miroir_v(state.ball.vitesse)
    for (id_team, id_player) in state.players :
        (res.player_state(id_team,id_player)).position = miroir_p(state.player_state(id_team,id_player).position)
        (res.player_state(id_team,id_player)).vitesse = miroir_v(state.player_state(id_team,id_player).vitesse)
    return res    
                    
class PlayerStateDecorator : 
    def __init__(self , state , id_team , id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player 
       

            
        ################ POSITION  #####################
   
    def position_bal(self) : 
        return self.state.ball.position
        
    def position_player(self):
        return self.state.player_state(self.id_team, self.id_player).position  
        
    def distance_of_bal(self):
        return self.state.player_state(self.id_team, self.id_player).position.distance(self.state.ball.position)               
       
       ############## Dattaque_pointeEPLACEMENT ########################
       
    def stop(self):
        return SoccerAction()
       
    def retour_position(self, v):
         return SoccerAction(v - self.position_player(),Vector2D())
        
    def suivre_bal(self) : 
        return SoccerAction(self.position_bal()-self.position_player() , self.no_shoot())
        
    def suivre_bal_en_y(self) :
        return SoccerAction(Vector2D(0,(self.position_bal().y - self.position_player().y)),Vector2D())
    
    
    def go_to_the_middle(self):
        v = Vector2D(settings.GAME_WIDTH/2,settings.GAME_HEIGHT/2.)
        return self.retour_position(v)
            
    def go_to_attack(self):
        v = Vector2D(settings.GAME_WIDTH*3/4,settings.GAME_HEIGHT/2.)
        return self.retour_position(v)
        
            
    
    def go_to_defence(self):
        v= Vector2D(settings.GAME_WIDTH*1/4,settings.GAME_HEIGHT/2.)
        return self.retour_position(v)
   

    def go_to_goal(self):
        v= Vector2D(0,settings.GAME_HEIGHT/2.)
        if(self.id_team == 1):
            return self.retour_position(v)
        else :
            return self.retour_position(v)

    ############## SHOOT ###########################
        
    def no_shoot(self):
        return Vector2D(x=0,y=0)
        
    def can_shoot(self):
        if(self.distance_of_bal() < settings.PLAYER_RADIUS + settings.BALL_RADIUS):
            return True
        else :
            return False
            
    def shoot_to(self, v):
        if(self.id_team == 1):
            return SoccerAction( self.position_bal()-self.position_player() , v - self.position_player())
        else: 
            v = miroir_v(v)
            return SoccerAction( self.position_bal()-self.position_player() , v - self.position_player())
 
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
        
    def shoot_bal( self):
        if(self.can_shoot() == True):
            return self.shoot_to_cage_t1()
        else :
            return self.stop()
            
    def small_shoot(self):
        if(self.can_shoot() == True):
            return SoccerAction( self.position_bal()-self.position_player() , Vector2D(settings.GAME_WIDTH , (settings.GAME_HEIGHT)/6) - self.position_player())
        else:
            return self.stop()
    
    def shoot_bal_def(self) : 
        if(self.can_shoot() == True):
            return self.shoot_rand() 
        else :
            return self.stop()
            
    ############# PASS #####################
            
    def pass_to(self , v):
        v.norme = 5
        

        return self.shoot_to(v)
        
        
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
