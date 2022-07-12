top_games = ["Dark souls", "Elder scrolls", "Mine craft", "Metal Gear","NieR Automata"]
multiplayer_player = ["R6","CSGO","APEX","COD","OW"]
top_games[1] = "Skyrim"
print(top_games[1])
print(top_games[1:4])
print(top_games[1:5])
top_games.sort()
top_games.insert(0,"Bioshock")
print(top_games)
top_games.append("DMC5")
print(top_games)
top_games.pop(6)
print(top_games)
print(top_games.index("Dark souls"))
top_games.extend(multiplayer_player)
print(top_games)