import click
import requests

from rich.pretty import pprint
from rich.console import Console
from rich.table import Table

console = Console()

@click.group()
def cli():
    """Dndsear: main group"""
    pass


@cli.group(name='list')
def list_():
    """List: this is the home group for listing data."""
    pass


@cli.group()
def find():
    """Find: this is the home group for searching and finding specific data."""
    pass


@cli.command(help='This is the base url for the api, this is not created by me.')
def url():
    console.print('https://www.dnd5eapi.co/', style='blue')


@find.command(help="Gives info on a spell, put quotation marks around spell.")
@click.argument('spell')
def spell(spell):

    spell = spell.lower()
    spell = spell.replace(' ', '-')

    data = requests.get(f"https://www.dnd5eapi.co/api/spells/{spell}")
    data = data.json()

    table = Table(title=f"{spell.capitalize()}'s Search Quarries", show_lines=True)

    table.add_column("Index", justify="left", style="blue")
    table.add_column("Key", justify="center", style="red")

    for i, info in enumerate(data): 
        table.add_row(str(i), info)
        query_data = data


    console.print(table)

    where = input("Where would you like to continue on to: ")
    query_data = query_data[where]

    while True:

        if where == 'url':
            pprint(query_data)
            url = query_data

            query_data = requests.get(f'https://www.dnd5eapi.co{url}')
            query_data = query_data.json()

            where = ""

        else:
            if type(query_data) in [str, int]:
                console.print(query_data, style='blue')
                break

            elif type(query_data) == dict:

                new_table = Table(title=f"{spell.capitalize()}'s Search Quarries", show_lines=True)

                new_table.add_column("Index", justify="left", style="blue")
                new_table.add_column("Key", justify="center", style="red")

                for i, info in enumerate(query_data): 
                    new_table.add_row(str(i), info)


                console.print(new_table)

                where = input("Where would you like to continue on to: ")
                query_data = query_data[where]
            
            elif type(query_data) == list:
                pprint(query_data)

                where = int(input("Where would you like to focus in on. Number: "))
                query_data = query_data[where - 1]


@find.command(help="Gives info on a monster, put quotation marks around monster.")
@click.argument('monster')
def monster(monster):

    monster = monster.lower()
    monster = monster.replace(' ', '-')

    data = requests.get(f"https://www.dnd5eapi.co/api/monsters/{monster}")
    data = data.json()

    table = Table(title=f"{monster.capitalize()}'s Search Quarries", show_lines=True)

    table.add_column("Index", justify="left", style="blue")
    table.add_column("Key", justify="center", style="red")

    for i, info in enumerate(data): 
        table.add_row(str(i), info)
        query_data = data


    console.print(table)

    where = input("Where would you like to continue on to: ")
    query_data = query_data[where]

    while True:

        if where == 'url':
            pprint(query_data)
            url = query_data

            query_data = requests.get(f'https://www.dnd5eapi.co{url}')
            query_data = query_data.json()

            where = ""

        else:
            if type(query_data) in [str, int]:
                console.print(query_data, style='blue')
                break

            elif type(query_data) == dict:

                new_table = Table(title=f"{monster.capitalize()}'s Search Quarries", show_lines=True)

                new_table.add_column("Index", justify="left", style="blue")
                new_table.add_column("Key", justify="center", style="red")

                for i, info in enumerate(query_data): 
                    new_table.add_row(str(i), info)


                console.print(new_table)

                where = input("Where would you like to continue on to: ")
                query_data = query_data[where]
            
            elif type(query_data) == list:
                pprint(query_data)

                where = int(input("Where would you like to focus in on. Number: "))
                query_data = query_data[where - 1]


@find.command(help = 'This is the url command to search through more spesific parts. Dont include "https://www.dnd5eapi.co/api/"')
@click.argument('quarry')
def quarrysearch(quarry):

    data = requests.get(f"https://www.dnd5eapi.co/api/{quarry}")
    data = data.json()

    table = Table(title=f"Search Quarries", show_lines=True)

    table.add_column("Index", justify="left", style="blue")
    table.add_column("Key", justify="center", style="red")

    for i, info in enumerate(data): 
        table.add_row(str(i), info)
        quarry_data = data


    console.print(table)

    where = input("Where would you like to continue on to: ")
    quarry_data = quarry_data[where]

    while True:

        if where == 'url':
            pprint(quarry_data)
            url = quarry_data

            quarry_data = requests.get(f'https://www.dnd5eapi.co{url}')
            quarry_data = quarry_data.json()

            where = ""
            
        else:
            if type(quarry_data) in [str, int]:
                print(quarry_data)
                break

            elif type(quarry_data) == list:

                pprint(quarry_data)

                where = int(input("Where would you like to go, integers: "))
                quarry_data = quarry_data[where - 1]

            elif type(quarry_data) == dict:
                
                new_table = Table(title=f'Search Quarries', show_lines=True)

                new_table.add_column("Index", justify="left", style="blue")
                new_table.add_column("Key", justify="center", style="red")

                for i, info in enumerate(quarry_data): 
                    new_table.add_row(str(i), info)


                console.print(new_table)

                where = input("Where would you like to continue on to: ")
                quarry_data = quarry_data[where]


@list_.command(help='This lists the possible list commands.')
def lists():
    listcommands = ['spells', 'classes', 'skills', 'magicitems', 'languages', 'features', 'quarries', 'monsters']

    table = Table(title="DnD Spells", show_lines=True)

    table.add_column("Command Number", justify="left", style="blue")
    table.add_column("Command Name", justify="center", style="red")

    for i, comm in enumerate(listcommands):
        table.add_row(str(i), comm)

    console.print(table)


@list_.command(help="This lists the spells.")
def spells():
    data = requests.get(f"https://www.dnd5eapi.co/api/spells/", timeout=90)
    data = data.json()['results']

    table = Table(title="DnD Spells", show_lines=True)

    table.add_column("Index Number", justify="left", style="blue")
    table.add_column("Spell Name", justify="center", style="red")
    table.add_column("Spell Index", justify='center', style='purple')

    for i, mons in enumerate(data): 
        table.add_row(str(i), mons["name"], mons['index'])


    console.print(table)


@list_.command(help="This lists the classes.")
def classes():
    data = requests.get(f"https://www.dnd5eapi.co/api/classes/", timeout=90)
    data = data.json()['results']

    table = Table(title="DnD Classes", show_lines=True)

    table.add_column("Index Number", justify="left", style="blue")
    table.add_column("Class Name", justify="center", style="red")
    table.add_column("Class Index", justify='center', style='purple')

    for i, mons in enumerate(data): 
        table.add_row(str(i), mons["name"], mons['index'])


    console.print(table)


@list_.command(help="This lists the skills.")
def skills():
    data = requests.get(f"https://www.dnd5eapi.co/api/skills/", timeout=90)
    data = data.json()['results']

    table = Table(title="DnD Skills", show_lines=True)

    table.add_column("Index Number", justify="left", style="blue")
    table.add_column("Skill Name", justify="center", style="red")
    table.add_column("Skill Index", justify='center', style='purple')

    for i, mons in enumerate(data): 
        table.add_row(str(i), mons["name"], mons['index'])


    console.print(table)


@list_.command(help="This lists the magic.")
def magicitems():
    data = requests.get(f"https://www.dnd5eapi.co/api/magic-items/", timeout=90)
    data = data.json()['results']

    table = Table(title="DnD Magic Items", show_lines=True)

    table.add_column("Index Number", justify="left", style="blue")
    table.add_column("Item Name", justify="center", style="red")
    table.add_column("Item Index", justify='center', style='purple')

    for i, mons in enumerate(data): 
        table.add_row(str(i), mons["name"], mons['index'])


    console.print(table)


@list_.command(help="This lists the languages.")
def languages():
    data = requests.get(f"https://www.dnd5eapi.co/api/languages/", timeout=90)
    data = data.json()['results']

    table = Table(title="DnD Language", show_lines=True)

    table.add_column("Index Number", justify="left", style="blue")
    table.add_column("Language Name", justify="center", style="red")
    table.add_column("Language Index", justify='center', style='purple')

    for i, mons in enumerate(data): 
        table.add_row(str(i), mons["name"], mons['index'])


    console.print(table)


@list_.command(help="This lists the features from classes & levels.")
def features():
    data = requests.get(f"https://www.dnd5eapi.co/api/features/", timeout=90)
    data = data.json()['results']

    table = Table(title="DnD Classes", show_lines=True)

    table.add_column("Index Number", justify="left", style="blue")
    table.add_column("Feature Name", justify="center", style="red")
    table.add_column("Feature Index", justify='center', style='purple')

    for i, mons in enumerate(data): 
        table.add_row(str(i), mons["name"], mons['index'])


    console.print(table)


@list_.command(help = 'This shows the possible quarries for the advanced search.')
def quarries():
    things = requests.get("https://www.dnd5eapi.co/api/", timeout=90)
    results_dict = things.json()

    table = Table(title="DnD Api Quarries", show_lines=True)

    table.add_column("Index Number", justify="left", style="blue")
    table.add_column("Quarry Name", justify="center", style="red")

    for i, quar in enumerate(results_dict):
        table.add_row(str(i), quar)


    console.print(table)


@list_.command(help = 'This lists the data of a monster of choice.')
def monsters():
    data = requests.get(f"https://www.dnd5eapi.co/api/monsters/", timeout=90)
    data = data.json()['results']

    table = Table(title="DnD Monsters", show_lines=True)

    table.add_column("Index Number", justify="left", style="blue")
    table.add_column("Monster Name", justify="center", style="red")
    table.add_column("Monster Index", justify='center', style='purple')

    for i, mons in enumerate(data): 
        table.add_row(str(i), mons["name"], mons['index'])


    console.print(table)
