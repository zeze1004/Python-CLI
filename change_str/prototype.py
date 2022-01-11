from __future__ import print_function, unicode_literals
from os import replace

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint


style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


questions = [
    {
        'type': 'checkbox',
        'message': 'Select option',
        'name': 'redis-resource',
        'choices': [
            Separator('= env ='),
            {
                'name': 'alpha'
            },
            {
                'name': 'prod'
            },
            Separator('= region ='),
            {
                'name': 'Seoul'
                # 'checked': True
            },
            {
                'name': 'Tokyo'
            },
            {
                'name': 'Japan'
            },
            {
                'name': 'UK'
            },
            Separator('= cluster mode ='),
            {
                'name': 'redis cluster'
            },
            {
                'name': 'redis single'
            }
        ],
        'validate': lambda answer: 'You must choose at least one option.' 
            if len(answer) == 0 else True
    }
]

answers = prompt(questions, style=style)
pprint(answers)

resouce = {
    'env': [
        'alpha',
        'prod'
    ],
    'region': [
        'Seoul',
        'Tokyo',
        'Japan',
        'UK'
    ],
    'mode': [
        'cluster',
        'single'
    ]
}
new_answers = []
def change_str(answers):
    // resouce의 key 값이 replace될 단어
    // new_answers에 answers의 값 넣음?
        

fin = open("redis.tf", "rt") ### redis랑 new_redis랑 바꾸기
#output file to write the result to
fout = open("new_redis.tf", "wt")
#for each line in the input file
for line in fin:
    #read replace the string and write to output file
    fout.write(line.replace('region', ))
#close input and output files
fin.close()
fout.close()