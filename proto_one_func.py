import click

@click.command()
@click.option("--input", prompt="Your input")

def communication(input):
    while input != "end":
        communication2(input)
    exit()

def communication2(input):
    click.echo("%s" %input)
    communication()


if __name__ == '__main__':
    print("프로그램 종료를 원하시면 end를 입력해주세요")
    communication()
    