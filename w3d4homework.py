import requests
import time

# Function to find the pokemon in the chosen type, and to allow the pokemon trainer to pick a pokemon
def find_pick_poke(poke_names):
    print(f"These are all of the pokemon in the {type_choice} typing")
    pokemon_in_type = []
    player_team = []
    for i in poke_names['pokemon']:
        if '-' not in i['pokemon']['name']:
            time.sleep(.05)
            print(i['pokemon']['name'])
            pokemon_in_type.append(i['pokemon']['name'])
    pick_from_type = True
    while pick_from_type:
        picking_pokes = input("Please choose any of these pokemon you like: ").title()
        player_team.append(picking_pokes)
        keep_picking = input("Would you like to keep picking from this typing? Y/N: ").upper()
        if keep_picking == "N":
            pick_from_type = False
        else:
            continue
    print(f"Here's your team so far {player_team}")
    return player_team

# Pokedex logic
pokemon_ing = True
while pokemon_ing:
    lets_pick = input("Would you like to pick some pokemon? If you would like to stop and move out in the wide world, press 'n' when you return to this prompt: ").upper()
    if lets_pick == 'N':
        pokemon_ing = False
        picking = False
        break
    else:
        picking = True
        while picking:
            type_choice = input("Choose your type: ").lower()
            type_poke = f"https://pokeapi.co/api/v2/type/{type_choice}/"
            chosen_poke_type = requests.get(type_poke).json()
            find_pick_poke(chosen_poke_type)
            time.sleep(1)
            print("Okay, let's move on to another type")
            picking = False

    





