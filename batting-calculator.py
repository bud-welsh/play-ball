print('Welcome to the Batting Calculator')

player_name = input('What is the name or the player? ')
hits = int(input('How many hits did ' + player_name + ' have during his career? '))
at_bats = int(input('How many at bats did ' + player_name + ' have during his career? '))
batting_average = hits / at_bats

print(player_name + ' had a batting average of:')
print(batting_average)
