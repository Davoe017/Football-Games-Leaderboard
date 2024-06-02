#Linear and Multiplicative Congruential Method
'''ini_seed = int(input("Input the initial seed: "))
a = int(input("Input multiplier: "))
modu = int(input("Input modulus: ")) 
incre = int(input("Input Increment: ")) 
#n = int(input("How many random numbers do you want to generate: "))
for j in range(1,5):
    ini_seed = ((a*ini_seed) + incre) % modu
    while ini_seed != j:
        #ini_seed = int(input("Input the initial seed: ")) linear congruential
        ini_seed = ((a*ini_seed) + incre) % modu #multiplicative congruential
        print(f'{ini_seed}')'''

import random

def linear_congruential(seed, a, c, m, n):
    random_numbers = []
    x = seed
    for g in range(n):
        x = (a * x + c) % m
        random_numbers.append(x)
    return random_numbers

def generate_matchups_teams(num_teams):
    matchups = []
    teams = list(range(num_teams))
    random.shuffle(teams)
    for i in range(0, num_teams - 1, 2):
        matchups.append((teams[i], teams[i + 1]))
    return matchups

def generate_scores(num_teams, matchups, num_weeks):
    scores = {team: 0 for team in range(num_teams)}
    for week in range(1, num_weeks + 1):
        print(f"Week {week}:")
        for matchup in matchups:
            team1, team2 = matchup
            score1 = random.randint(0, min(8, 4 + random.randint(-1, 1))) # Random score for team 1
            score2 = random.randint(0, min(8, 4 + random.randint(-1, 1))) # Random score for team 2
            print(f"Matchup: Team {team1+1} vs Team {team2+1} - Score: {score1}-{score2}")
            if score1 > score2:
                scores[team1] += 3
            elif score1 < score2:
                scores[team2] += 3
            else:
                scores[team1] += 1
                scores[team2] += 1
        print()
    return scores

if __name__ == "__main__":
    num_teams = 8  # Change this to the number of teams you have (A-H teams)
    num_weeks = 5
    seed = 42  # Initial seed for random number generation
    a = 1664525
    c = 1013904223
    m = 2**32
    n = num_weeks * (num_teams // 2)

    random.seed(seed)
    matchups = generate_matchups_teams(num_teams)
    random_numbers = linear_congruential(seed, a, c, m, n)
    scores = generate_scores(num_teams, matchups, num_weeks)
    print("Final Scores:")
    for team, score in scores.items():
        print(f"Team {team+1}: {score} points")