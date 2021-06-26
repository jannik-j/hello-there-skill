from mycroft import MycroftSkill, intent_file_handler


class HelloThere(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hello.there.intent')
    def handle_there_hello(self, message):
        self.speak_dialog('hello.there')


def create_skill():
    return HelloThere()

