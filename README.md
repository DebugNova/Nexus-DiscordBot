# Nexus Discord Bot

A Discord bot that uses OpenAI's GPT-3.5-turbo to provide empathetic and context-aware responses.

## Features

- Context-aware conversations
- Persistent memory across sessions
- Wake/sleep functionality
- Emotionally intelligent responses

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with the following variables:
   ```
   OPENAI_API_KEY=your_openai_api_key
   DISCORD_TOKEN=your_discord_bot_token
   ```
4. Run the bot:
   ```bash
   python nexus.py
   ```

## Commands

- `nexus wake up` - Activates the bot in the current channel
- `nexus sleep` - Deactivates the bot in the current channel

## Security

- Never commit your `.env` file
- Keep your API keys secure
- The bot only responds in channels where it has been explicitly activated

## License

MIT License
