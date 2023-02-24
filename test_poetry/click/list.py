import click

@click.group()
def pipelines():
    pass

@pipelines.command()
def list():
    click.echo(print(['HELLO', 'WORLD']))

@pipelines.command()
def run():
    click.echo("It's run")
