import random

def lookaway (num_trials):
    num_games = num_trials
    luigi_wins = 0
    while num_trials > 0:
        rounds = 5
        peach_life = 1
        wario_life = 1
        mario_life = 1
        while rounds > 0:
            peach_look = random.random()
            if peach_look < 0.20:
                peach_life = 0
            wario_look = random.random()
            if wario_look < 0.20:
                wario_life = 0
            mario_look = random.random()
            if mario_look < 0.20:
                mario_life = 0
            rounds-=1
        if peach_life+mario_life+wario_life == 0:
            luigi_wins+=1
        num_trials-=1
        
    print "Luigi won ", luigi_wins, " out of ", num_games, " games."
    
