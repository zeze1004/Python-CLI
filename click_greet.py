import click

def say_hello(name):
    click.echo("Hello, %s" %name)

def say_goodbye(name):
    click.echo("Good bye, %s" %name)

@click.command()
@click.option('--bye', is_flag=True, help="say good bye.")
@click.option('--hello', is_flag=True, help="say hello.")
@click.option("--name", prompt="Your name", help="The person to greet.")

def main(name, hello, bye):
    if bye:
        say_goodbye(name)
    else:
        say_hello(name)

if __name__ == "__main__":
    main()