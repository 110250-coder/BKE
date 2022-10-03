import random
 
from bke import start, MLAgent, is_winner, opponent, RandomAgent, train_and_plot, EvaluationAgent

class MyRandomAgent(EvaluationAgent):
  def evaluate(self, board, y_symbol, opponent_symbol):
    return random.randint(1, 500)
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
    



def Validation():
  my_agent = MyAgent(alpha=0.8, epsilon=0.2)
  
  my_agent = MyAgent()
  random_agent = RandomAgent()
   
  train_and_plot(
      agent=my_agent,
      validation_agent=random_agent,
      iterations=50,
      trainings=100,
      validations=1000)