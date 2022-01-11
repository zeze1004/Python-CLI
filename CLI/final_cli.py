from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
# from prompt_toolkit.validation import Validator, ValidationError


# class NumberValidator(Validator):

#     def validate(self, document):
#         try:
#             int(document.text)
#         except ValueError:
#             raise ValidationError(message="Please enter a number", cursor_position=len(document.text))

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

###
# 아무것도 선택 안했을 때 로직 추가
###

pprint(answers)

# answer_env = answers.get('redis-resource-env', None)
# answer_region = answers.get('redis-resource-region')
# answer_mode = answers.get('redis-resource-mode')
# print("env",  answer_env)
# print("region", answer_region)
# print("cluster", answer_mode)

# if len(answer_cluster) > 1:
#     print("multiple task")
# else:
#     print("single task:", answer_cluster)