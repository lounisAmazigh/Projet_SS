from  soccersimulator import settings
from soccersimulator import  SoccerAction 
from Tools import *

# ATTAQUE BASIC T1
def attaquant1(Mystate):
    return Mystate.shoot_to_cage_t1() + Mystate.suivre_bal()                
       
# ATTAQUE BASIC T2 
def player_go(Mystate):
    
     if  Mystate.position_bal().x ==  (settings.GAME_WIDTH)/2  :
         return attaquant1(Mystate)
    
     elif(Mystate.pos_ball_attaque() == True) :
        return Mystate.go_to_the_middle()
        
     elif (Mystate.pos_ball_milieu() == True) :
        v = Vector2D(settings.GAME_WIDTH*3/4,settings.GAME_HEIGHT/2.)
        if Mystate.position_bal().x >  (settings.GAME_WIDTH*1.2)/2 :
            return Mystate.suivre_bal() + Mystate.shoot_to_cage_t1() 
        else :
            return Mystate.suivre_bal() + Mystate.shoot_to(v)
            
     else :
         return Mystate.shoot_bal_def() + Mystate.suivre_bal()
     
       
# ATTAQUE EN POINTE 
       
def attaque_pointe(Mystate):
    
    if Mystate.pos_ball_attaque() == True :
        if Mystate.distance_players_t2():
            return Mystate.shoot_to_cage_t1() 
        else: 
            return Mystate.go_to_cage_with_ball()
        
    elif Mystate.pos_ball_defense():
        return Mystate.suivre_bal_en_y()
    else :
        return Mystate.go_to_attack()
        
# MILIEU DE TERRAIN
def milieu_centre(Mystate):
    
    if (Mystate.pos_ball_milieu() == True) :
        v = Vector2D(settings.GAME_WIDTH*3/4,settings.GAME_HEIGHT/2.)
        
        if Mystate.position_bal().x > (settings.GAME_WIDTH*1.07)/2  :
            return Mystate.suivre_bal() + Mystate.shoot_to_cage_t1() 
            
        elif Mystate.distance_players_t2() :
            return Mystate.suivre_bal() + Mystate.shoot_to(v)
            
        else :
            return Mystate.go_to_cage_with_ball()  
            
            
    elif Mystate.pos_ball_defense() == True :
        return Mystate.go_to_left()
        
    else:
        return Mystate.suivre_bal_en_y()
        
# DEFENSE BASIC T1
def defenseur1(Mystate):
    
    if( Mystate.pos_ball_defense() == True):
        v = Vector2D(settings.GAME_WIDTH*1/2,settings.GAME_HEIGHT*3/4.)
            
        if Mystate.distance_players_t2() : 
            return Mystate.shoot_to(v) + Mystate.suivre_bal()  
            
        else : 
            return Mystate.go_to_cage_with_ball()
            
    elif Mystate.pos_ball_milieu() :
            return Mystate.suivre_bal_en_y() 
            
    elif Mystate.pos_ball_goal()  :
        return Mystate.shoot_bal_def() + Mystate.suivre_bal()
  
    else : 
            return  Mystate.go_to_defence()
        
# GOAL
def goal(Mystate):  
  
     if Mystate.pos_ball_goal() == True :
        return Mystate.shoot_bal_def() + Mystate.suivre_bal()    
     else : 
           return Mystate.go_to_goal()      
    

# MIL ATT
def milieu_def(Mystate):

     if(Mystate.pos_ball_attaque() == True) :
        return milieu_centre(Mystate)
        
     else : 
         return defenseur1(Mystate)
        
def test1(Mystate):   
    
    if(Mystate.pos_ball_attaque() == True or Mystate.pos_ball_milieu()) :
        if Mystate.distance_players_t2() or Mystate.ball_is_goal_t2() : # True
            return Mystate.shoot_to_cage_t1()
        else:
            return Mystate.go_to_cage_with_ball()    
            
    else : 
            return Mystate.go_to_the_middle()
    
 
         

        
        
        
        
        
        
        
        
        
        
