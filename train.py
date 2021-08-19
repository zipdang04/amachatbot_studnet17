from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)

trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)