from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from chatterbot.response_selection import get_random_response

my_bot = ChatBot(name='pepper',read_only = True,
                 response_selection_method=get_random_response,
                 logic_adapters=[
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'empty',
            'output_text': ''
        },
        {   
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'i honestly have no idea how to respond to that',
            'maximum_similarity_threshold': 0.9
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        }

    ]
    )

trainer = ChatterBotCorpusTrainer(my_bot)
trainer.train("./conversations.yml")
while True:
    try:
        user_input = input("user > ")

        bot_response = my_bot.get_response(user_input)

        print(bot_response)
    except:
        break
