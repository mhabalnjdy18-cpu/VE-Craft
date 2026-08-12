# VE Craft Discord Bot

مرحبا انا بوت VE Craft تم إنشاء من قبل مهاب بلايز

A Discord bot with a welcome system for new members.

## Features

- ✅ Welcome system that greets new members
- ✅ Displays member's username and avatar
- ✅ Shows account creation date and member count
- ✅ Admin command to set welcome channel
- ✅ Easy to extend with more features

## Setup

### Prerequisites
- Python 3.8+
- A Discord bot token

### Installation

1. Clone the repository
```bash
git clone https://github.com/mhabalnjdy18-cpu/VE-Craft.git
cd VE-Craft
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your bot token
```bash
cp .env.example .env
```

Then edit `.env` and add your Discord bot token:
```
DISCORD_TOKEN=your_actual_token_here
```

### Running the Bot

```bash
python main.py
```

## Configuration

### Setting the Welcome Channel

Use the following command in Discord (requires admin permissions):
```
!setwelcome #channel-name
```

This will set the channel where welcome messages are sent when new members join.

## Bot Permissions

Make sure your bot has the following permissions:
- Send Messages
- Embed Links
- Read Message History
- View Channels

## File Structure

```
VE-Craft/
├── main.py              # Main bot entry point
├── cogs/
│   └── welcome.py       # Welcome system
├── requirements.txt     # Dependencies
├── .env.example         # Environment template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Security Notes

⚠️ **Never share your bot token!**
- Keep your `.env` file private
- Never commit `.env` to version control
- The `.gitignore` file protects it automatically

## Support

For issues or feature requests, please create an issue on GitHub.

---

Created with ❤️ by مهاب بلايز
