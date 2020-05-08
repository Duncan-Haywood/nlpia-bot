""" Pattern and template based chatbot dialog engines """
import re
import json


# from .template_generators import generate_sentence  # noqa


class Bot:
    def __init__(self, file_name="journal_questions.txt"):
        with open(file_name, 'r') as fin:
            self.questions = json.load(fin)
        
    
    def reply(self, statement):
        """ Chatbot "main" function to respond to a user command or statement

        >>> reply('Hi')[0][1]
        Hello!
        >>> len(reply('Hey Mycroft!'))
        4
        """
        responses = []
        for q in self.questions:
            responses.append((1,q))
        return responses
