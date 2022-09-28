import random
 
from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
    
random.seed(1)

def plot1():
  class MyAgent(MLAgent):
      def human(self, board):
          if is_winner(board, self.symbol):
              reward = 1
          elif is_winner(board, opponent[self.symbol]):
              reward = -1
          else:
              reward = 0
          return reward
def plot2():
  class MyAgent(MLAgent):
      def dumb(self, board):
          if is_winner(board, self.symbol):
              reward = 1
          elif is_winner(board, opponent[self.symbol]):
              reward = -1
          else:
              reward = 0
          return reward
def plot3():
  class MyAgent(MLAgent):
      def train(self, board):
          if is_winner(board, self.symbol):
              reward = 1
          elif is_winner(board, opponent[self.symbol]):
              reward = -1
          else:
              reward = 0
          return reward
def plot4():
  class MyAgent(MLAgent):
      def smart(self, board):
          if is_winner(board, self.symbol):
              reward = 1
          elif is_winner(board, opponent[self.symbol]):
              reward = -1
          else:
              reward = 0
          return reward
        
def plot5():
    class MyAgent(MLAgent):
      def evaluate(self, board):
          if is_winner(board, self.symbol):
              reward = 1
          elif is_winner(board, opponent[self.symbol]):
              reward = -1
          else:
              reward = 0
          return reward
      
    
random.seed(1)

plot_5 = plot5()

my_agent = MyAgent()
random_agent = RandomAgent()
 
train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)