pokemons_list = [int(pokemon) for pokemon in input().split()]
combined_value = 0
while len(pokemons_list) != 0:
    command = int(input())
    if command < 0:
        removed = pokemons_list[0]
        pokemons_list[0] = pokemons_list[-1]
    elif command >= len(pokemons_list):
        removed = pokemons_list[-1]
        pokemons_list[-1] = pokemons_list[0]
    else:
        removed = pokemons_list.pop(command)
    for pokemon in range(len(pokemons_list)):
        if pokemons_list[pokemon] <= removed:
            pokemons_list[pokemon] += removed
        elif pokemons_list[pokemon] > removed:
            pokemons_list[pokemon] -= removed
    combined_value += removed
print(combined_value)

