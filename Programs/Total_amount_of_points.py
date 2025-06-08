# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

#     if x > y: 3 points (win)
#     if x < y: 0 points (loss)
#     if x = y: 1 point (tie)

# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

# Notes:

#     our team always plays 10 matches in the championship
#     0 <= x <= 4
#     0 <= y <= 4



def points(games):
    total = 0 

    for game in games:
        my_team_score, opponent_team_score = int(game[0]),int(game[2])  

        if my_team_score > opponent_team_score:
            total += 3  # Win
        elif my_team_score == opponent_team_score:
            total += 1  # Draw
        else:
            total += 0  # Loss (optional, since it adds nothing)

    return total


print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))