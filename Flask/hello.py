from flask import Flask, render_template
from prompt_toolkit.key_binding.bindings.named_commands import register
app = Flask(__name__)

###

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
pprint(type(answers))

### 

@app.route('/<name>')
def hello_world(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
