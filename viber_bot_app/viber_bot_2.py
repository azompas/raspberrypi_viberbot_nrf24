from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

import time
import logging
import sched
import threading
import yaml

from sys import path
path.append('/home/anastasis/code/raspberrypi_viberbot_nrf24')
from utils.database import yamlDatabase
from utils.menu import homeSensorMenu

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)

with open(path_to_cred_yaml, 'r') as cred_yaml:
	cred_list = yaml.load(cred_yaml)
name = None
avatar = None
auth_token = None
for cred in cred_list:
	if "name" in cred:
		name = cred["name"]
	elif "avatar" in cred:
		avatar = cred["avatar"]
	elif "auth_token" in cred:
		auth_token = cred["auth_token"]

viber = Api(BotConfiguration(
  name=name,
  avatar=avatar,
  auth_token=auth_token
))

@app.route('/', methods=['POST'])
def incoming():
	logger.debug("received request. post data: {0}".format(request.get_data()))

	viber_request = viber.parse_request(request.get_data())
	db = yamlDatabase()
	hm = homeSensorMenu()
	hm.help_function()

	if isinstance(viber_request, ViberMessageRequest):
		#~ message = viber_request.message
		viber_request_dict = db.viber_request_to_dict(viber_request)
		db.check_and_write_info_to_yaml("/home/anastasis/code/viber_bot/test_db_users.yaml", viber_request_dict)
		viber.send_messages(viber_request.sender.id, [
			#~ message
			TextMessage(text="Hello {}".format(viber_request.sender.name))
		])
	elif isinstance(viber_request, ViberConversationStartedRequest) \
			or isinstance(viber_request, ViberSubscribedRequest) \
			or isinstance(viber_request, ViberUnsubscribedRequest):
		viber.send_messages(viber_request.user.id, [
			TextMessage(text="Welcome to my Bot!!!")
		])
	elif isinstance(viber_request, ViberFailedRequest):
		logger.warn("client failed receiving message. failure: {0}".format(viber_request))

	return Response(status=200)

def set_webhook(viber):
	viber.set_webhook('https://3ba42f5e.ngrok.io')

if __name__ == "__main__":
	scheduler = sched.scheduler(time.time, time.sleep)
	scheduler.enter(5, 1, set_webhook, (viber,))
	t = threading.Thread(target=scheduler.run)
	t.start()

	#~ context = ('server.crt', 'server.key')
	#~ app.run(host='0.0.0.0', port=8443, debug=True, ssl_context=context)
	app.run(host='0.0.0.0', port=8080)
