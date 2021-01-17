**The AntiCorruptionBot** is a WhatsApp chatbot built using Flask, [Chatterbot](https://chatterbot.readthedocs.io/en/stable/index.html) Python library and Twilio. 
The chatbot has been trained on an edited conversation using material from this [source](http://www.ecba.org/extdocserv/projects/ace/20160114_ACE_CountryreportRomania.pdf) in order to answer specific questions about corruption offences, anticorruption laws and institutions in Romania.

**Set-up**

In order to run the project locally, you will need to take the following steps:

1. git clone project on your local machine
2. create virtual environment in Terminal or Command Prompt: `python3 -m venv anticorruption-bot`
3. activate virtual environment: 
   - Mac command: `source anticorruption-bot/bin/activate`
   - Windows command: `anticorruption-bot\Scripts\activate`
4. install requirements: `pip install -r requirements.txt`
5. change database_uri in line 11 of bot.py module to your database location, or remove to use default sqlite3 database.
6. sign up to [Twilio](https://www.twilio.com/try-twilio) & follow instructions
7. download ngrok
8. in the Terminal/Command Prompt window where you activated the virtual env, run command: `python3 bot.py`
9. open new Terminal/Command Prompt window, cd in the folder where you unzipped ngrok download, run command: `ngrok http 500`
10. Copy paste the http ngrok URL mapped to localhost:5000 in Twilio WhatsApp Sandbox Settings, against the input required for WHEN A MESSAGE COMES IN form field.

Enjoy!
