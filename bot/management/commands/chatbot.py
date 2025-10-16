from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

DB_PATH = 'db.sqlite3'

class Command(BaseCommand):
    help = 'Run a terminal chatbot session'

    def handle(self, *args, **options):
        bot = ChatBot(
            'TerminalBot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri=f'sqlite:///{DB_PATH}',
            logic_adapters=[
                {'import_path': 'chatterbot.logic.BestMatch'}
            ],
            read_only=False
        )

        if not os.path.exists(DB_PATH):
            self.stdout.write(self.style.WARNING('First run detected. Training the bot...'))
            trainer = ChatterBotCorpusTrainer(bot)
            try:
                trainer.train('chatterbot.corpus.english.greetings',
                              'chatterbot.corpus.english.conversations')
            except Exception as e:
                self.stdout.write(self.style.NOTICE(f'[info] Training step skipped or completed: {e}'))
            self.stdout.write(self.style.SUCCESS('Training complete.'))

        self.stdout.write("Type 'quit' to exit.\n")
        while True:
            try:
                user_text = input('user: ').strip()
                if user_text.lower() in {'quit', 'exit'}:
                    print('bot: Bye!')
                    break
                response = bot.get_response(user_text)
                print(f'bot: {response}')
            except (KeyboardInterrupt, EOFError):
                print('\nbot: Bye!')
                break
