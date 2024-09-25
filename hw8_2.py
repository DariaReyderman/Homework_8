nba_players: list[int] = []
height: float = 0.0
SENTINEL: int = -999
good_height: int = 0
counter: int = 0

while True:
    height: float = float(input("Enter a height of the player: "))
    if height == SENTINEL:
        break
    if not 1.60 <= height <= 3.0:
        continue
    nba_players.append(height)

    if height > 2.0:
        good_height += 1
if len(nba_players) > 0:
    print(f"Total number of players is {len(nba_players)}")
    print(f"The maximum height is {max(nba_players)}")
    print(f"The minimum height is {min(nba_players)}")
    avg_height: float = sum(nba_players) / len(nba_players)
    print(f"The average height of the players is {avg_height:.2f}")
    print(f"Number of players who is higher than 2 meters: {good_height}")

# Unfortunately I didn't understand how I can find the number of players who is higher than average :(((((
# I will very appreciate if you can explain, pleeeeaseeee :)
