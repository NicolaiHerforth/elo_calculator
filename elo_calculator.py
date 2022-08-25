# Python 3 program for Elo Rating
import math
import random 
import time
from typing import Literal

# Function to calculate the Probability
def Probability(team_1_rating: int, team_2_rating:int) -> float:
    """Calculates the probability of team_2 winning
    
    Args:
        team_1_rating (int): Integer representation of rating for team 1
        team_2_rating (int): Integer representation of rating for team 2
    Returns:
        float value representation of the probability of team_2 winning
    """
 
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (team_1_rating - team_2_rating) / 400))
 
 
# Function to calculate Elo rating
# K is a constant.
# d determines whether
# Player A wins or Player B.
def EloRating(rating_team_a: int, rating_team_b:int, winner: Literal[1,0], K: int = 30, ):
    """
    Calculates elo rating rating_team_a and rating_team_b. 

    Args:
        rating_team_a (int): Rating of team a
        rating_team_b (int): Rating of team b
        K (int): A constant modifying rating change. If K is of a lower value, then the rating is changed by a small fraction but if K is of a higher value, then the changes in the rating are significant.
        winner (Literal[1,0]): Binary representation of winner, with 1 being team a and 0 being team b.
    """
    # Calculate the probabilities of each team winning
    probability_team_b = Probability(rating_team_a, rating_team_b)
    probability_team_a = Probability(rating_team_b, rating_team_a)
 
    # Case 1 When team_a wins
    if (winner == 1) :
        rating_team_a = rating_team_a + K * (1 - probability_team_a)
        rating_team_b = rating_team_b + K * (0 - probability_team_b)
     
 
    # Case 2 When team_b wins
    else :

        rating_team_a = rating_team_a + K * (0 - probability_team_a)
        rating_team_b = rating_team_b + K * (1 - probability_team_b)
     
   

    return rating_team_a, rating_team_b

if __name__ == '__main__':
    Rating_a = 1700
    Rating_b = 1600
    for i in range(100):
        if i % 10 == 0:
            print(f"Updated Ratings at game {i}:")
            print("Rating_a =", round(Rating_a, 6)," Rating_b =", round(Rating_b, 6))
            print("Prob team A", Probability(Rating_b, Rating_a), "Prob team B", Probability(Rating_a, Rating_b))
            print()
        # Roll winner based on probabilty of winning
        d = random.choices(population=[1,0], weights=[Probability(Rating_b, Rating_a), Probability(Rating_a, Rating_b)])[0]
        Rating_a, Rating_b = EloRating(Rating_a, Rating_b, d)