#!/usr/bin/python
import click

@click.group()
def cli():
    pass

@cli.command()
def create():
    click.echo('Initialized the redis')

@cli.command()
def delete():
    click.echo('Deleted the redis')

def communication(input_str):
    while input_str != "end":
        if input_str == "create":
            create()
        elif input_str == "delete":
            delete()
        else:
            print("다시 입력하시오")
            input_str = input("명령어를 입력하시오: ")
    exit()

if __name__ == '__main__':
    print("프로그램 종료를 원하시면 end를 입력해주세요")
    print("redis 생성: create / 삭제 delete")
    input_str = input("명령어를 입력하세요: ")
    communication(input_str)

    