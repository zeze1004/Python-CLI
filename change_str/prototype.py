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


resource = {
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

def get_choies(subject):
    result = []
    for choices in resource.get(subject):
        result.append({'name': choices})
    return result

questions = [
    {
        'type': 'checkbox',
        'message': 'Select option',
        'name': 'redis-resource-env',
        'choices': get_choies('env'),
        'validate': lambda answer: 'You must choose at least one option.'
        if len(answer) == 0 else True
    },
    {
        'type': 'checkbox',
        'message': 'Select option',
        'name': 'redis-resource-region',
        'choices': get_choies('region'),
        'validate': lambda answer: 'You must choose at least one option.' 
        if len(answer) == 0 else True
    },
    {
        'type': 'checkbox',
        'message': 'Select option',
        'name': 'redis-resource-mode',
        'choices': get_choies('mode'),
        'validate': lambda answer: 'You must choose at least one option.' 
        if len(answer) == 0 else True
    }
]

answers = prompt(questions, style=style)

pprint(answers)

# with 추가하기
fin = open("redis_sample.tf", "rt") 
fout = open("redis.tf", "wt")

for line in fin:
    fout.write(line.replace('region_input', str(answers.get('redis-resource-region'))))
fin.close()
fout.close()
