print('Welcome to the Batting Calculator')

player_name = input('What is the name or the player? ')
hits = int(input('How many hits did ' + player_name + ' have during his career? '))
doubles = int(input('How many of those hits were doubles? '))
triples = int(input('How many of those hits were triples? '))
home_runs = int(input('How many of those hits were home runs? '))
at_bats = int(input('How many at bats did ' + player_name + ' have during his career? '))
batting_average = hits / at_bats
total_bases = (hits + doubles + (triples * 2) + (home_runs * 3))

print(player_name + ' had a batting average of: ' + str(batting_average))
print(player_name + ' had ' + str(total_bases) + ' total bases')

