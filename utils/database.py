import yaml

from copy import deepcopy

class yamlDatabase(object):
	def __init__(self):
		print "Database initialized..."

	def write_to_yaml(self, path_to_yaml, user_info):
		with open(path_to_yaml, 'r') as yaml_data:
			all_user_info_list = yaml.load(yaml_data)
		if not all_user_info_list:
			all_user_info_list = list()
			all_user_info_list.append(user_info)
		else:
			if not type(all_user_info_list) == list:
				all_user_info_dict = deepcopy(all_user_info_list)
				all_user_info_list = list()
				all_user_info_list.append(all_user_info_dict)
			else:
				all_user_info_list.append(user_info)
		with open(path_to_yaml, 'w') as user_info_yaml:
			yaml.safe_dump(all_user_info_list, user_info_yaml, default_flow_style=False)

	def check_and_write_info_to_yaml(self, path_to_yaml, user_info):
		if not type(user_info) == dict:
			user_info = self.viber_request_to_dict(user_info)
		with open(path_to_yaml, 'r') as yaml_data:
			all_user_info_list = yaml.load(yaml_data)
		id_already_exists = False
		for entry in all_user_info_list:
			if user_info["user"]["id"] == entry["user"]["id"]:
				id_already_exists = True
		if not id_already_exists:
			self.write_to_yaml(path_to_yaml, user_info)

	def viber_request_to_dict(self, viber_info):
		user_info_dict = dict()
		user_info_dict["user"] = dict()
		user_info_dict["user"]["name"] = "{}".format(viber_info.sender.name)
		user_info_dict["user"]["id"] = viber_info.sender.id
		user_info_dict["user"]["country"] = viber_info.sender.country
		
		return user_info_dict
