# Libs
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Nomeia o Bot
bot =  ChatBot('Dojo_Whats')

# Treina
treino =  ChatterBotCorpusTrainer(bot)
treino.train('chatterbot.corpus.portuguese.conversations')

# Responde
resposta = bot.get_response('Olá')
while True:
    resposta = bot.get_response(input(str()))
    print(resposta)
