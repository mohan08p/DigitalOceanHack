from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


class BotTrainer(object):
	conver= [
			"Hello",
			"Hi there!",
			"How are you?",
			"I am good.",
			"How are you doing?",
			"I'm doing great.",
			"Where do you live?",
			"I live in Mumbai",
			"Where are you from?",
			"I live in Navi Mumbai",
			"Where in navi mumbai?",
			"Cbd bealpur",
			"Are you robot or human?",
			"I am human ofcourse.",
			"That is good to hear",
			"Me too",
			"Thank you.",
			"You're welcome.",
			"give me a job",
			"That's great.Please, enter the position for which you want the job"    
   		]
   	chatbot = ChatBot("Ron Obvious")
	def __init__(self):
		chatbot = self.chatbot
  		chatbot.set_trainer(ChatterBotCorpusTrainer)
  		chatbot.train("chatterbot.corpus.english")  		
		chatbot.set_trainer(ListTrainer)
		chatbot.train(self.conver)
              
	def respond(self, text):
		ans=self.chatbot.get_response(text)
		ans=str(ans)
                print ans
		return ans
