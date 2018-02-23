import os


def readJson(path):
	"""
	Read a json file to a python dict.

	:type path: str
	:rtype: dict
	"""
	data = {}

	if os.path.exists(path):
		with open(path, "r") as f:
			data_ = f.read()
			if data_:
				data = json.loads(data_)

	return data


def saveJson(path, data):
	"""
	Write a python dict to a json file.

	:type path: str
	:type data: dict
	:rtype: None
	"""
	dirname = os.path.dirname(path)

	if not os.path.exists(dirname):
		os.makedirs(dirname)

	with open(path, "w") as f:
		data = json.dumps(data, indent=4)
		f.write(data)


def localPath(*args):
	"""
	Return the users preferred disc location.

	:rtype: str
	"""
	path = os.getenv('APPDATA') or os.getenv('HOME')
	path = os.path.join(path, "AAM", *args)

	return path


def data_root():
	"""
	Return a Pixmap object from the given resource name.
	:rtype: str 
	"""
	return FtrackData().data_root(*args)


def asset_builds_root(*args):
	"""
	Return a Pixmap object from the given resource name.
	:rtype: str 
	"""
	print FtrackData().asset_builds_root()
	return FtrackData().asset_builds_root()







class FtrackData(object):
	def __init__(self):
		'''At startup, all ftrack data should be queried for the current task
		
		When the task is switched, a method should be used to dump the old data and
		cache the new data for future requests

		Would be great to do this on a separate thead in the background
		'''

		global _ftrack_data


	def data_root(self):
		'''Root path for Armada's data
		
		:param str data_path: Publish path

		returns: "path/to/_ArmadaDAta"
		return type str
		'''

		return "S:/STUDIO_TEAMSPACE/Episodes/fake/_ArmadaData"

	def publish_data_root(self):
		'''Root path for Armada's publish data
		
		:param str data_path: Publish path

		returns: "path/to/_ArmadaDAta"
		return type str
		'''

		return os.path.join(self.data_root(), 'PublishData')

	def asset_builds_root(self):
		'''Root path for current episode's project hierarchy
		
		:param str data_path: Publish path

		returns: "path/to/_ArmadaDAta"
		return type str
		'''

		return os.path.join(self.publish_data_root(), 'Asset_Builds')

	def publish_root(self):
		'''Root path for task publish. This is generated by ftrack's resource identifier

		:param str data_path: Publish path

		returns: "path/to/publish"
		return type str
		'''

		return "S:/STUDIO_TEAMSPACE/Episodes/fake/ANOTHER_SEQUENCE/Publish/CharAnims'"

	def query_ftrack_data(self):
		'''This will query all the ftrack data, but for now i'm hardcoding values
		'''
		self.episode = 'fake'
		self.shot_name = 'CharAnims'
		self.task_name = 'CharacterAAnims'
		self.publish_path = 'S:/STUDIO_TEAMSPACE/Episodes/fake/ANOTHER_SEQUENCE/Publish/CharAnims'  
		self.game_data = ''

		return {
			'episode': self.episode,
			'shot_name': self.shot_name,
			'task_name': self.task_name,
			'publish_path': self.publish_path,
			'game_data' : self.game_data
		}