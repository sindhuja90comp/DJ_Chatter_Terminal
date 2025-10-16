"""Terminal client using ChatterBot.
Run: python terminal_client.py
"""
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Use local SQLite database in project root
DB_PATH = 'db.sqlite3'

def get_bot():
    # Create the chatbot (will create the DB on first run)
    bot = ChatBot(
        'TerminalBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri=f'sqlite:///{DB_PATH}',
        logic_adapters=[
            {'import_path': 'chatterbot.logic.BestMatch'}
        ],
        read_only=False
    )
    return bot

def ensure_trained(bot):
    # Train from a small built-in English corpus on first run
    # This is idempotent; subsequent runs will reuse the DB.
    trainer = ChatterBotCorpusTrainer(bot)
    try:
        trainer.train('chatterbot.corpus.english.greetings',
                      'chatterbot.corpus.english.conversations')
    except Exception as e:
        # If already trained or corpus missing, continue gracefully
        print('[info] Training step skipped or completed:', e)

def main():
    bot = get_bot()
    if not os.path.exists(DB_PATH):
        print('[setup] First run detected. Training the bot...')
        ensure_trained(bot)
        print('[setup] Training complete. Start chatting!')
    print("Type 'quit' to exit.\n")
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

if __name__ == '__main__':
    main()
