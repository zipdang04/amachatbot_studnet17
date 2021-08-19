from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:nguyenthanhdat13031977@localhost/chatbot'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lpawitweaifdms:3e30c818a7cedc2fc0c85c703826c4177725c93b2241d8499a9bf248ffb1217c@ec2-52-3-130-181.compute-1.amazonaws.com:5432/debhac8sm0k1qr'    

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


bot = ChatBot('Training Example')


'''
This is an example showing how to create an export file from
an existing chat bot that can then be used to train other bots.
'''

chatbot = ChatBot('Export Example Bot')

# First, lets train our bot with some data
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')

# Now we can export the data to a file
trainer.export_for_training('./my_export.json')
trainer.export_for_training('./train_vietnam.json')
@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()