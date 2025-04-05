# Professor Music Bot

A powerful Telegram Music Bot written in Python using Pyrogram and Py-Tgcalls. This bot allows you to play music and videos in Telegram group voice chats.

## Features

- Play music from YouTube, SoundCloud, Spotify, Apple Music, Resso, and Telegram audio files
- Play video streams in group video chats
- Supports channel streaming
- Powerful queue management with shuffle, loop, and playlist features
- Multi-language support
- Attractive thumbnails and UI
- Supports live streaming from YouTube
- Customizable settings for audio and video quality

## Requirements

- Python 3.8 or higher
- A Telegram API key (API ID and API Hash)
- A Telegram Bot token from [@BotFather](https://t.me/BotFather)
- MongoDB database for storing user preferences and playlists

## Setup & Deployment

### Local Deployment

1. Clone the repository:
   ```bash
   git clone https://github.com/username/professor-music-bot.git
   cd professor-music-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy `sample.env` to `.env` and fill in the required variables:
   ```bash
   cp sample.env .env
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

### Heroku Deployment

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/username/professor-music-bot)

### Docker Deployment

1. Build the image:
   ```bash
   docker build -t professor-music-bot .
   ```

2. Run the container:
   ```bash
   docker run -d --name professor-music-bot professor-music-bot
   ```

## Configuration

Edit the `.env` file or set the following environment variables:

- `API_ID` - Telegram API ID from my.telegram.org
- `API_HASH` - Telegram API Hash from my.telegram.org
- `BOT_TOKEN` - Telegram Bot Token from BotFather
- `MONGO_DB_URI` - MongoDB connection URI
- `DURATION_LIMIT` - Maximum duration of audio files in minutes
- `SUDO_USERS` - List of user IDs who have full control over the bot

See `sample.env` for all available configuration options.

## Commands

- `/start` - Start the bot
- `/help` - Show help message
- `/ping` - Check bot response time
- `/play [song name or YouTube link]` - Play a song in voice chat
- `/pause` - Pause the current song
- `/resume` - Resume the paused song
- `/skip` - Skip the current song
- `/stop` - Stop playing and clear the queue
- `/shuffle` - Shuffle the queue
- `/seek` - Seek the song to a specific position
- `/settings` - Open bot settings panel

## Support

- Updates Channel: [@SANATANI_TECH](https://t.me/SANATANI_TECH)
- Support Group: [@SANATANI_SUPPORT](https://t.me/SANATANI_SUPPORT)

## Credits

- [Pyrogram](https://github.com/pyrogram/pyrogram)
- [Py-TgCalls](https://github.com/pytgcalls/pytgcalls)

## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.
