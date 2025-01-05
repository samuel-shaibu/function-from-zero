import click
from mylib.bot import scrape


@click.command()
@click.option(
    "--name", prompt="Wikipedia page to scrape", help="Web page we want to scrape"
)
# @click.option('length',
# help='length of the output from wikipedia')


def cli(name):
    result = scrape(name)
    click.echo(click.style(f"Result: {result}:", fg="blue", bg="white"))


if __name__ == "__main__":
    cli()
