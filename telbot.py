import sys
import time
import telepot
import datetime

now = datetime.datetime.now()

def main(msg):
	contentType, chatType, chatId = telepot.glance(msg)
	with open("file.log", 'a') as out:
		out.write(now.strftime("%d.%m.%Y %H:%M") + "\n")

	if (telepot.glance(msg)[0] == 'text'):
		bot.sendMessage(telepot.glance(msg)[2], "It works!")

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(main)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)