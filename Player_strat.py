from  soccersimulator import settings
from soccersimulator import  SoccerAction 
from Tools import *

# ATTAQUE BASIC T1
def attaquant1(Mystate):
    return Mystate.shoot_to_cage_t1() + Mystate.suivre_bal()                
       
       
# ATTAQUE EN POINTE 
       
def attaque_pointe(Mystate):
    if(Mystate.position_bal().x >=  (settings.GAME_WIDTH*2.5)/4 ) or Mystate.position_bal().x == settings.GAME_WIDTH / 2  :
        return Mystate.shoot_to_cage_t1() + Mystate.suivre_bal()
        
    elif (Mystate.position_bal().x > settings.GAME_WIDTH / 2 ) :
        a = random.uniform(0,30)
        if a > 2.5:
            return Mystate.suivre_bal_en_y()
        else:
            return Mystate.shoot_to_cage_t1() + Mystate.suivre_bal()

    elif (Mystate.position_bal().x < settings.GAME_WIDTH / 2 ) :
        return Mystate.go_to_attack()
        
# MILIEU DE TERRAIN
def milieu_centre(Mystate):
    if(Mystate.position_bal().x >  (settings.GAME_WIDTH*3)/4 ) :
        return Mystate.suivre_bal_en_y()
        
    elif (Mystate.position_bal().x >= settings.GAME_WIDTH / 2 ) :
        return Mystate.shoot_to_cage_t1() + Mystate.suivre_bal()
        
    elif Mystate.position_bal().x >= settings.GAME_WIDTH / 4 :
        return Mystate.shoot_to_cage_t1() + Mystate.suivre_bal()
        
    elif Mystate.position_bal().x < settings.GAME_WIDTH / 4 :
        return Mystate.suivre_bal_en_y()
        
# DEFENSE BASIC T1
def defenseur1(Mystate):
    
    if( Mystate.position_bal().x < settings.GAME_WIDTH / 3 ) :
        return Mystate.shoot_bal_def() + Mystate.suivre_bal()  
            
    elif(Mystate.position_bal().x >= settings.GAME_WIDTH / 2) :
       return Mystate.go_to_defence()
  
    else : 
        return Mystate.suivre_bal_en_y()
        
# GOAL
def goal(Mystate):
    
     if( Mystate.position_bal().x < settings.GAME_WIDTH / 6 ) :
        return Mystate.shoot_bal_def() + Mystate.suivre_bal()
        
     else :
        return Mystate.go_to_goal()
    
    
# DEFENSE BASIC T2
def defenseur2(Mystate):
    if( Mystate.position_bal().x > settings.GAME_WIDTH *3/4 ) :
        return Mystate.shoot_bal_def() + Mystate.suivre_bal() 
                    
    elif( Mystate.position_player().x < settings.GAME_WIDTH *3/ 4 ):
        v = Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        return Mystate.retour_position(v)
    else : 
        return Mystate.suivre_bal_en_y()
        
        
# MIL ATT
def milieu_att(Mystate):

     if( Mystate.position_bal().x >=  (settings.GAME_WIDTH*2.5)/4  ):
        return attaque_pointe(Mystate)
        
     else :
        return milieu_centre(Mystate)
        
def test1(Mystate):   
    
    #if(Mystate.distance_of_cage() < 50 ):
    if Mystate.distance_players_t2(Mystate.state) == True: 
        return Mystate.shoot_to_cage_t1()
    else:
        return Mystate.go_to_cage_with_ball()     
 
         
   
        
        
        
        
        
        
        
        
        
        
        
