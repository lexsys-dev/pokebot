import pokepy
from . import Ability, Learnset, Type

def get_all_info(api, query):
	ans = ''

	try:
		pikasp = api.get_pokemon_species(query)
	except:
		response = "Nome inválido."
		return response

	for n in pikasp.names:
		if n.language.name == 'en':
			pname = n.name
	PRE_URL = 'https://bulbapedia.bulbagarden.net/wiki/'
	MID = pname + '_%28Pokémon%29'
	B_URL = PRE_URL+MID

	ans = 'Nome do Pokémon: ['+pname+']('+B_URL+')' + '\n\n'

	ans = ans + Ability.get_ability(api,query)

	ans = ans + Type.fetch_type(api,query) + '\n'

	ans = ans + 'Lista de golpes: ' + Learnset.get_learnset(api,query)

	return ans
