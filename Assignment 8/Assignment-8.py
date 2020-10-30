names = ("audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask")
pokelist = names.split(" ")
pokedict = {}
for i in pokelist:
    if i[0] not in pokedict:
        pokedict[i[0]] = [i]
    else:
        pokedict[i[0]].append(i)

def pokemonlist(x):
    global longest

    longest = []
    if len(x) > len(longest):
        longest = x

    if x[-1][-1] in pokedict:
        for name in pokedict[x[-1][-1]]:
            if name not in x:
                x.append(name)
                pokemonlist(x) 

for x in pokelist:
    pokemonlist([x])

print(longest)
