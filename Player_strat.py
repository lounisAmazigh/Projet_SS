from  soccersimulator import settings
from soccersimulator import  SoccerAction 
from Tools import *


def attaquant1(Mystate):
    
    if( Mystate.position_bal().x >= settings.GAME_WIDTH / 2 ) :
        return Mystate.shoot_to_cage_t1() + Mystate.suivre_bal()  
    else:
        if(Mystate.position_bal().x < settings.GAME_WIDTH / 4) :
            return Mystate.stop()
        else : 
            return Mystate.shoot_to_cage_t1() + Mystate.suivre_bal()                
       
       
def defenseur1(Mystate):
    
    if( Mystate.position_bal().x < settings.GAME_WIDTH / 2 ) :
        return Mystate.shoot_to_cage_t1() + Mystate.suivre_bal()  
            
    elif(Mystate.position_player().x > settings.GAME_WIDTH / 4) :
        v= Vector2D(0,settings.GAME_HEIGHT/2.)
        return Mystate.retour_position(v)
    else : 
        return Mystate.suivre_bal_en_y()
        
def defenseur2(Mystate):
    if( Mystate.position_bal().x > settings.GAME_WIDTH / 2 ) :
        return Mystate.shoot_bal_def() + Mystate.suivre_bal() 
                    
    elif( Mystate.position_player().x < settings.GAME_WIDTH *3/ 4 ):
        v = Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        return Mystate.retour_position(v)
    else : 
        return Mystate.suivre_bal_en_y()