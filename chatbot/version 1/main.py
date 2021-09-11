from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 
from chatterbot.trainers import ChatterBotCorpusTrainer
my_bot = ChatBot(
    name  = "JaysonBot", 
read_only = True,  logic_adpters = ["chatterbot.logic.mathematicaEvaluation", "chatterbot.logic.BestMatch"] )

small_talk = [
    'hi there!',
    'hi', 
    'howdo you do ?',
    'i\'m cool.', 
    'fine, you?', 
    'always cool.',
    'i\'m ok',
    'glad to hear that.', 
    'i feel awsome', 
    'excellent, glad to hear that.',
    'not so good',
    'sorry to hear that.',
    'not so good', 
    'so sorry to hear that.',
    'what\'s your name?',
    'i\'m jaysonBot. ask me a math question, please.'

]
math_talk_1 = [
    'pythagorean theorem'
    'a squared plus b squared equals c squared.'
]
math_talk_2 = [
    'law of cosines', 
    'c**2 = a**2 +b**2 - 2* a*b *cos(gamma)'
]
list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

print(my_bot.get_response("hi"))
print(my_bot.get_response("i fell awsome today"))
print(my_bot.get_response("what's  your name"))
print(my_bot.get_response("show me your pythagorean theorem"))

while True:

    try: 
        bot_input = input("You: ")
        bot_response = my_bot.get_response(bot_input)
        print( f"{my_bot.name}: {bot_response}")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break;