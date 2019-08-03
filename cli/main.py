import click
import crawl.cat

@click.group()
def main():
    pass

@click.command()
def welcome():
    click.echo('Hello ! Welcome Smart-Crawller')

@click.command()
@click.option('--selenium', '-s')
@click.argument('site_name')
def cat(site_name, selenium):

    if selenium is None:
        click.echo(crawl.cat.cat_simple(site_name))
    else:
        click.echo(crawl.cat.cat_simple())



main.add_command(welcome)
main.add_command(cat)