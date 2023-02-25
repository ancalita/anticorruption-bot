from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

chatbot = ChatBot("Anticorruption",
                  read_only=True,
                  logic_adapters=['chatterbot.logic.BestMatch'],
                  database_uri=os.environ.get('DATABASE_URL'))

trainer = ListTrainer(chatbot)

for knowledge in os.listdir('base'):
    BotMemory = open('base/' + knowledge, 'r').readlines()
    trainer.train(BotMemory)

app = Flask(__name__)


@app.route("/", methods=["POST"])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()
    bot_response = chatbot.get_response(incoming_msg)
    msg.body(str(bot_response))

    return str(response)


if __name__ == '__main__':
    app.run()
