import click
from crawl.commands.cat import Cat
from crawl.commands.xpath import Xpath

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
        click.echo(Cat.with_simple(site_name))
    else:
        click.echo(Cat.with_selenium(site_name))





@click.command()
@click.argument('url')
@click.argument('xpath_')
def xpath(url, xpath_):
    click.echo(Xpath.get(url=url, xpath=xpath_))

    # example1.
    # smart-crawller xpath https://stackoverflow.com/questions/38727520/adding-default-parameter-value-with-type-hint-in-python //*[@id=\"answer-38727786\"]/div/div[2]/div[1]/p[1]

main.add_command(welcome)
main.add_command(cat)
main.add_command(xpath)