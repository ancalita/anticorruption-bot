from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

chatbot = ChatBot("Anticorruption",
                  read_only=True,
                  logic_adapters=['chatterbot.logic.BestMatch'])
trainer = ListTrainer(chatbot)

for knowledge in os.listdir('base'):
    BotMemory = open('base/' + knowledge, 'r').readlines()
    trainer.train(BotMemory)

corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train("chatterbot.corpus.english")

app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()
    responded = False
    bot_response = chatbot.get_response(incoming_msg)

    if bot_response:
        msg.body(str(bot_response))
        responded = True

    if not responded:
        msg.body('I did not understand your question. '
                 'I only know about anticorruption laws, initiatives and orgs in Romania, sorry!')
    return str(response)


if __name__ == '__main__':
    app.run()
