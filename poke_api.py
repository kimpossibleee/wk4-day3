import requests
from wk4_day3 import Node, LinkedList

class Pokemon:
    def __init__(self, pokemon):
        self.name = pokemon
        self.is_fully_evolved = False
        self.ev_chain_data = None
        self.call_evolution_chain_api()
        self.evolve_chain = LinkedList()


    def call_evolution_chain_api(self):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{self.name}')
        if response.status_code == 200:
            data = response.json()
            self.name = data['name']
            if 'evolution_chain' in data:
                response = requests.get(data['evolution_chain']['url'])
                self.ev_chain_data = response.json()
            else:
                print('This pokemon has no evolution chain.')
        else:
            print(f'Error, Status Code {response.status_code}')

    def add_evolution_chain(self):
        child = self.ev_chain_data['chain']['species']['name']
        self.evolve_chain.add_node(Node(child))
        next_evolution = self.ev_chain_data['chain']['evolves_to']
        while next_evolution:
            self.evolve_chain.add_node(Node(next_evolution[0]['species']['name']))
            next_evolution = next_evolution[0]['evolves_to']

mudkip = Pokemon('mudkip')
mudkip.add_evolution_chain()
print(mudkip.evolve_chain)
