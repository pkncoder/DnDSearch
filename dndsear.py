import click
import requests


from rich.pretty import pprint
from rich.console import Console
from rich.table import Table

console = Console()

@click.group()
def cli():
    pass


@cli.group(name='list')
def list_():
    """This is the home group for listing data."""
    pass


@cli.group()
def find():
    """This is the home group for searching and finding specific data."""
    pass


@cli.command(help = 'This is the base url for the api, this is not created by me.')
def url():
    click.echo('https://www.dnd5eapi.co')


@list_.command(help = 'This shows all of the possible quarries for the advanced search.')
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
def monster():
    data = requests.get(f"https://www.dnd5eapi.co/api/monsters/", timeout=90)
    data = data.json()['results']

    table = Table(title="DnD Monsters", show_lines=True)

    table.add_column("Index Number", justify="left", style="blue")
    table.add_column("Monster Name", justify="center", style="red")
    table.add_column("Monster Index", justify='center', style='purple')

    for i, mons in enumerate(data): 
        table.add_row(str(i), mons["name"], mons['index'])


    console.print(table)


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

        if type(query_data) in [str, int]:
            click.echo(query_data)
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
            query_data = query_data[where]


@find.command(help = 'This is the url command to search through more spesific parts. Dont include "https://dnd5eapi.co/api/"')
@click.argument('quarry')
def quarrysearch(quarry):

    data = requests.get(f"https://www.dnd5eapi.co/api/{quarry}/", timeout=90)
    data = data.json()['results']

    pprint(data)

    where = int(input("What number do you wish to go to: "))

    pprint(data[where - 1]['url'])

    url = data[where - 1]['url']

    

    quarry_data = requests.get(f"https://www.dnd5eapi.co{url}")
    quarry_data = quarry_data.json()


    while True:

        if type(quarry_data) in [str, int]:
            print(quarry_data)
            break
    

        elif type(quarry_data) == list:
            pprint(quarry_data)
            where = int(input("Where would you like to go, integers: "))

            url = quarry_data[where - 1]['url']

            quarry_data = requests.get(f"https://www.dnd5eapi.co{url}")
            quarry_data = quarry_data.json()

            quarry_data = quarry_data 
            

        elif type(quarry_data) == dict:
            
            new_table = Table(title=f'Search Quarries', show_lines=True)

            new_table.add_column("Index", justify="left", style="blue")
            new_table.add_column("Key", justify="center", style="red")

            for i, info in enumerate(quarry_data): 
                new_table.add_row(str(i), info)


            console.print(new_table)

            where = input("Where would you like to continue on to: ")
            
            quarry_data = quarry_data[where]
