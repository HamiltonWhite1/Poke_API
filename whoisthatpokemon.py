# Running into strange errors when importing. Going to try to resolve issue tomorrow


# import requests
# import time
# from w3d4homework import find_pick_poke

# print("Hello. My name is professor Oak. Welcome to the world of Pokemon ")

# trainer_team = []
# pokemon_ing = True
# while pokemon_ing:
#     lets_pick = ("Which type would you like to pick from? If you would like to stop and move out in the wide world, press 'n' when you return to this prompt: ").upper()
#     if lets_pick == 'N':
#         pokemon_ing = False
#         picking = False
#         break
#     else:
#         picking = True
#         while picking:
#             type_choice = input("Choose your type: ").lower()
#             type_poke = f"https://pokeapi.co/api/v2/type/{type_choice}/"
#             chosen_poke_type = requests.get(type_poke).json()
#             find_pick_poke(chosen_poke_type)
#             time.sleep(1)
#             print("Okay, let's move on to another type")
#             picking = False
