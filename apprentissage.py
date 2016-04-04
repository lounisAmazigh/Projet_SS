
from soccersimulator import settings, SoccerAction,Vector2D,DecisionTreeClassifier, KeyboardStrategy, BaseStrategy
from soccersimulator import export_graphviz
import cPickle
import sys
from Tools import *
from collections import defaultdict
from Player_strat import *


#######################VALEURS GLOBAL##############
alpha = 0.1
gamma = 0.9
epsilon = 0.1

#################################################

class PlayerIA :
    def __init__(self , state , id_team , id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player 
        self.suivre =0
        self.tirer =0
        self.avancer = 0
        
        
    def descritisation(self):
        Mystate = PlayerStateDecorator(self.state,self.id_team,self.id_player)

        lista = []   
        ## Distance du joueur adverse    
        if Mystate.distance_players_t2(40): 
            pos_jou_ad = 0
        elif Mystate.distance_players_t2(30):
            pos_jou_ad = 1
        elif Mystate.distance_players_t2(20):
            pos_jou_ad = 2
        elif Mystate.distance_players_t2(10):
            pos_jou_ad = 3
        else :
            pos_jou_ad = 0
        
        lista.add(pos_jou_ad)
    ## Distance de la balle pour tirer 
        if(Mystate.distance_of_bal() < settings.PLAYER_RADIUS + settings.BALL_RADIUS) :
            pos_bal = 3
        else :
            pos_bal = 0
            
        lista.add(pos_bal)
    ## Distance des goal adverse : 
        if Mystate.distance_of_cage() < 20 :
            cage = 3
        
        elif Mystate.distance_of_cage() < 30 :
            cage = 2
        
        elif Mystate.distance_of_cage() < 50 :
            cage = 1      
        
        else :
            cage = 0
        
        lista.add(cage)
    ## Distance de mes cages 
        if Mystate.distance_of_mycage() < 10 :
            m_cage = 3
            
        elif Mystate.distance_of_mycage() < 20 :
            m_cage = 2
        
        elif Mystate.distance_of_mycage() < 30 :
            m_cage = 1     

        else :
            m_cage = 0
 
        lista.add(m_cage)

        return tuple(lista)

    def Q(self):
    
        s = discretisation(self.state,self.id_team,self.id_player)

        Q[s]=defaultdict(float)
        #choisire une action au hasard 
      #  a = choisire action 
        Q[s][a] 
        return Q 
  
    # INFO SUR L'ETAT :
  
    def info_etat()
    def recompense(self,etat,action):
        
        
    

    def Monte_carlo(Q= None, scenario = [(state,action)...,(state,action)]):
    
        R = recompense(senario[-1][0])      
        if Q is None:
            Q = dict()
     
        for (s,a) in senario[-2::-1]:
            if s not in Q:
                Q[s] = defaultdict(float)
                Q[s][a] = 0
       
        for (s,a) in senario[-2::-1]:
            Q[s][a] = Q[s][a] + alpha*(R-Q[s][a])
            R = gamma * R +recompense(s)
        
        return Q
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    