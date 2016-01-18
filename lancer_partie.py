import soccersimulator
from  soccersimulator import settings
from soccersimulator import AbstractStrategy, SoccerAction 
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player , SoccerTournament
class RandomStrategy (AbstractStrategy):
	def __init__ (self) :
	   AbstractStrategy.__init__(self, "Random" )
	def compute_strategy (self, state, id_team, id_player):
	   return SoccerAction(Vector2D.create_random(),
			       Vector2D.create_random())

class MaStrategy(AbstractStrategy):
      def __init__(self):
         AbstractStrategy.__init__(self, "MaStrategie")
         
      def compute_strategy(self, state, id_team, id_player):
         bal = state.ball.position
         p = state.player_state(id_team, id_player)
         
         if  (p.position.distance(bal) < 1 + 0.65):
             if( id_team == 1):
                 return SoccerAction(bal-p.position ,Vector2D(settings.GAME_WIDTH , (settings.GAME_HEIGHT)/2) - p.position )
             else :
                 return SoccerAction(bal-p.position, Vector2D(x=-11,y=0))
         return SoccerAction(bal - p.position,Vector2D(x=0,y=0))
        

team1 = SoccerTeam("JSK",[Player("fonceur",MaStrategy()) ])
team2 = SoccerTeam("USMA",[Player("t2j1",MaStrategy())])
team3 = SoccerTeam("team3",[Player("t3j1",RandomStrategy())])

tournoi = SoccerTournament(1)
tournoi.add_team(team1)
tournoi.add_team(team2)
tournoi.add_team(team3)
soccersimulator.show(tournoi)

