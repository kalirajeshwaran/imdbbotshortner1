



### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com)
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.


## Deploy
<a href="https://heroku.com/deploy?template=https://github.com/PrinceStarLord/imerimdb">

  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">

</a>

</p>

</details>




<details><summary>Deploy To VPS</summary>
<p>
<pre>
git clone https://github.com/PrinceStarLord/imdbbot
# Install Packages
pip3 install -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>







