import click
from health_data_dumper.utils import time_util as tu


@click.group()
def cli():
    click.echo('a group with sub-commands')


@cli.command()
@click.option('--name', prompt='Your name please', default='World',
              help='option to customize greet message with name as user input')
@click.option('--repeat', default=1, help='repeats greeting x number of times')
def greet(name, repeat):
    """
    This script greets you and prints today's date
    """
    for i in range(repeat):
        click.echo(f'Hello {name}! .::Today is {tu.get_todays_date()}::.')


@cli.command()
def today():
    """
    This script prints today's date
    """
    click.pause()
    click.echo(tu.get_todays_date())


@cli.command()
@click.argument('year')
def dump_year(year):
    click.echo(year)


@cli.command()
def dump_month():
    pass


if __name__ == '__main__':
    print('main')
