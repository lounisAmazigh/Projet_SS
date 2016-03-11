from  soccersimulator import settings
from soccersimulator import  SoccerAction 
from Tools import *
import math
import random

# ATTAQUE BASIC T1
def foncer(Mystate):
    
    if Mystate.pos_ball_attaque() :
        if Mystate.ball_is_goal_t2():
            return Mystate.shoot_to_cage_t1(4) 
        else :             
            return Mystate.foncer_vers_les_but(2)
            
    elif Mystate.distance_players_t2(20) :
        return Mystate.foncer_a_gauche(1)
        
    else :
        return Mystate.foncer_tout_droit(1.5)    
      #  return Mystate.foncer_a_gauche(2)

def attaquant1(Mystate):
    if Mystate.pos_ball_AG() :
       return attaquant_droit_basic(Mystate)
        
    elif Mystate.pos_ball_AD():
        return attaquant_gauche_basic(Mystate)   
        
    elif Mystate.pos_ball_DG():
        return deff_droit_basic(Mystate)
        
    elif Mystate.pos_ball_DD():
        return deff_gauche_basic(Mystate) 
    
    else : 
        return foncer(Mystate)
        
def attaquant_droit_basic(Mystate):
    if Mystate.pos_ball_AG():
       if Mystate.distance_players_t2(20):
           return Mystate.shoot_to_cage_t1(5)
       else : 
           return Mystate.foncer_vers_les_but(2)
    else :
        return Mystate.go_to_left()
        
def attaquant_gauche_basic(Mystate):
    if Mystate.pos_ball_AD():
       if Mystate.distance_players_t2(15):
           return Mystate.pass_to_attaquant()
       else : 
           return Mystate.foncer_vers_les_but(2)
    else :
        return Mystate.go_to_right()
        
def deff_droit_basic(Mystate):
    if Mystate.pos_ball_DG():
       if Mystate.distance_players_t2(25):
           return Mystate.pass_to_attaquant()
       else : 
           return foncer(Mystate)
    else :
        return Mystate.go_to_def_left()
        
def deff_gauche_basic(Mystate):
    if Mystate.pos_ball_DD():
       if Mystate.distance_players_t2(25):
           return Mystate.pass_to_attaquant()
       else : 
           return foncer(Mystate)
    else :
        return Mystate.go_to_def_right()
        
        
       
# ATTAQUE BASIC T2 
def player_go(Mystate):
    
     if  Mystate.position_bal().x ==  (settings.GAME_WIDTH)/2  :
         return attaquant1(Mystate)
    
     elif(Mystate.pos_ball_attaque() == True) :
        return Mystate.go_to_the_middle()
        
     elif (Mystate.pos_ball_milieu() == True) :
        v = Vector2D(settings.GAME_WIDTH*3/4,settings.GAME_HEIGHT/2.)
        if Mystate.position_bal().x >  (settings.GAME_WIDTH*1.2)/2 :
            return Mystate.suivre_bal() + Mystate.shoot_to_cage_t1(5) 
        else :
            return Mystate.suivre_bal() + Mystate.shoot_to(v)
            
     else :
         return Mystate.shoot_bal_def() + Mystate.suivre_bal()
     
       
# ATTAQUATNS
       #attaque pointe
def attaque_pointe(Mystate):
    
    if Mystate.pos_ball_attaque() == True :
        if Mystate.distance_players_t2(20):
            return Mystate.shoot_to_cage_t1(5) 
        else: 
            return Mystate.foncer_vers_les_but(2)
        
    elif Mystate.pos_ball_defense():
        return Mystate.suivre_bal_en_y()
    else :
        return Mystate.go_to_attack()
        
     #attaque gauche 
def attaque_gauche(Mystate):
    if Mystate.pos_ball_AG() :    
        if Mystate.distance_players_t2(20):
            return Mystate.shoot_to_cage_t1(5)
        else : 
            return Mystate.foncer_vers_les_but(2)
    elif Mystate.pos_ball_AD() :
        return Mystate.suivre_bal_en_x()
    
    else :
        if Mystate.distance_of_bal() < 15 :
            return attaquant1(Mystate)
        else : 
            return Mystate.go_to_left()
        
def marcelo(Mystate):
    if Mystate.position_bal().x == settings.GAME_WIDTH/2 :
        return attaquant1(Mystate)
    elif Mystate.pos_ball_AD() :
        if Mystate.ball_is_goal_t2():
            return Mystate.shoot_to_cage_t1(5)
        elif Mystate.distance_players_t2(15):
            return Mystate.pass_to_attaquant()
        else :
            return Mystate.foncer_vers_les_but(2)
            
    elif Mystate.pos_ball_AG() :
        if Mystate.distance_of_bal() < 10 :
            return attaquant1(Mystate)
        else  :
            return Mystate.suivre_bal_en_x()
        
    elif Mystate.pos_ball_DD() :
        if Mystate.distance_players_t2(25):
            return Mystate.pass_to_attaquant()
        else :
            return Mystate.foncer_tout_droit(2)
            
    else :
        if Mystate.distance_of_bal() < 20 :
            return attaquant1(Mystate)
        else : 
            return Mystate.suivre_bal_en_x()
        
def deff_gauche(Mystate):
    if Mystate.pos_ball_DG() :
        #if Mystate.distance_players_t2():
        return Mystate.pass_to_attaquant()
        #else :
        #return Mystate.foncer_tout_droit()
            
    elif Mystate.pos_ball_AD() or Mystate.pos_ball_AG():
        return Mystate.go_to_defence()
        
    elif Mystate.pos_ball_DD() :
        if Mystate.distance_of_bal() < 20 :
            return attaquant1(Mystate)
        else : 
            return Mystate.suivre_bal_en_x()
    
    else :
        return Mystate.suivre_bal_en_x()
            

# MILIEU DE TERRAIN
def milieu_centre(Mystate):
     
     if Mystate.pos_ball_attaque() or Mystate.pos_ball_milieu() or Mystate.distance_of_bal() < 11 :
         return foncer(Mystate)
         
     else :
         return Mystate.suivre_bal_en_y()
         
   
        
# DEFENSE BASIC T1
def defenseur1(Mystate):

    if Mystate.pos_ball_DG():
        return deff_gauche(Mystate)
        
    elif Mystate.pos_ball_DD():
        return deff_gauche_basic(Mystate)
        
        
    else :
        if Mystate.position_bal().y == settings.GAME_HEIGHT/2. :
            return Mystate.avant_poste()
        
        elif Mystate.distance_of_bal() < 11 :
            return foncer(Mystate)
            
        elif Mystate.position_player().x > settings.GAME_WIDTH*3/4 :
            return Mystate.go_to_the_middle()
        else : 
            return Mystate.suivre_bal_en_y()
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
            return Mystate.shoot_to_cage_t1(5)
        else:
            return Mystate.go_to_cage_with_ball()    
            
    else : 
            return Mystate.go_to_the_middle()
    
 
        
        
        
        
        
        
        
        
