# Free Hosting Options for Nexus Discord Bot

## 1. Replit (Recommended for Beginners)

- **Pros:**
  - Free tier available
  - Easy to set up
  - Built-in IDE
  - Automatic HTTPS
  - Community support
- **Cons:**
  - Limited resources
  - May require "Always On" workarounds
  - Can be slow at times

### Setup Guide:

1. Create a Replit account
2. Create a new Python Repl
3. Upload your bot files
4. Install dependencies in the shell:
   ```bash
   pip install -r requirements.txt
   ```
5. Add your environment variables in the "Secrets" tab
6. Use UptimeRobot (free) to keep your bot online

## 2. Railway.app

- **Pros:**
  - Generous free tier
  - Easy deployment
  - Good performance
  - Automatic HTTPS
- **Cons:**
  - Limited free hours per month
  - Requires credit card for verification

### Setup Guide:

1. Create a Railway account
2. Connect your GitHub repository
3. Add environment variables
4. Deploy automatically

## 3. Heroku

- **Pros:**
  - Well-established platform
  - Good documentation
  - Automatic HTTPS
- **Cons:**
  - Free tier discontinued
  - Requires credit card
  - Limited free dyno hours

### Setup Guide:

1. Create a Heroku account
2. Install Heroku CLI
3. Create a Procfile:
   ```
   worker: python nexus.py
   ```
4. Deploy using Git

## 4. Oracle Cloud Free Tier

- **Pros:**
  - Generous free resources
  - Full VM control
  - 24/7 uptime
  - Good performance
- **Cons:**
  - Complex setup
  - Requires credit card
  - Limited regions

### Setup Guide:

1. Create Oracle Cloud account
2. Create a free VM instance
3. Set up Python environment
4. Configure firewall rules
5. Run bot as a service

## 5. Google Cloud Run

- **Pros:**
  - Generous free tier
  - Good performance
  - Automatic scaling
- **Cons:**
  - Complex setup
  - Requires credit card
  - Limited free requests

### Setup Guide:

1. Create Google Cloud account
2. Set up Cloud Run
3. Containerize your bot
4. Deploy to Cloud Run

## Keeping Your Bot Online

### Using UptimeRobot (Free)

1. Create an UptimeRobot account
2. Add your Replit/Heroku URL
3. Set monitoring interval to 5 minutes
4. This will ping your bot to keep it awake

### Using a Keep-Alive Script

Add this to your bot code:

```python
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
```

## Important Considerations

1. **Environment Variables**

   - Never commit your `.env` file
   - Use platform-specific secret management
   - Keep your tokens secure

2. **Resource Management**

   - Monitor memory usage
   - Implement proper error handling
   - Use efficient data structures

3. **Backup Strategy**

   - Regular database backups
   - Version control
   - Configuration backups

4. **Monitoring**
   - Set up basic logging
   - Monitor uptime
   - Track error rates

## Recommended Setup for Beginners

1. Start with Replit + UptimeRobot
2. Use the keep-alive script
3. Monitor your bot's performance
4. Upgrade to more robust hosting as needed

## Troubleshooting

1. **Bot Goes Offline**

   - Check hosting platform status
   - Verify environment variables
   - Check error logs

2. **High Resource Usage**

   - Optimize your code
   - Implement caching
   - Reduce API calls

3. **Connection Issues**
   - Check network settings
   - Verify firewall rules
   - Test API connectivity
