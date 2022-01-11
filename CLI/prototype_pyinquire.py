from __future__ import print_function, unicode_literals

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