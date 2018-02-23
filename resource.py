
import os

from Qt import QtGui

PATH = os.path.abspath(__file__)
DIRNAME = os.path.dirname(PATH)
RESOURCE_DIRNAME = os.path.join(DIRNAME, "resource")


def get(*args):
	"""
	Convenience function for returning the resource path.

	:rtype: str 
	"""
	return Resource().get(*args)


def icon(*args, **kwargs):
	"""
	Convenience function for returning an Icon object from the given resource name.
	:rtype: str 
	"""
	return Resource().icon(*args, **kwargs)


def pixmap(*args, **kwargs):
	"""
	Convenience function for returning a Pixmap object from the given resource name.
	:rtype: str 
	"""
	return Resource().pixmap(*args, **kwargs)


def style_sheet(*args):
	"""
	Convenience function for returning a style sheet css object from the given resource name.
	:rtype: str 
	"""
	return Resource().style_sheet(*args)


class Resource(object):
	DEFAULT_DIRNAME = RESOURCE_DIRNAME
	def __init__(self, *args):

		dirname = ""
		
		if args:
			dirname = os.path.join(*args)
			
		if os.path.isfile(dirname):
			dirname = os.path.dirname(dirname)

		self._dirname = dirname or self.DEFAULT_DIRNAME

	def get(self, *args):
		"""
		Return the resource path for the given args.

		:rtype: str
		"""
		return os.path.join(self.dirname(), *args)

	def dirname(self):
		"""
		:rtype: str
		"""
		return self._dirname

	def icon(self, name, extension="png", color=None):
		"""
		Return an Icon object from the given resource name.

		:type name: str
		:type extension: str
		:rtype: QtGui.QIcon
		"""
		p = self.pixmap(name, extension=extension, color=color)

		return QtGui.QIcon(p)

	def pixmap(self, name, scope="icon", extension="png", color=None):
		"""
		Return a Pixmap object from the given resource name.

		:type name: str
		:type scope: str
		:type extension: str
		:rtype: QtWidgets.QPixmap
		"""
		path = self.get(scope, name + "." + extension)

		p = QtGui.QPixmap(path)

		#if color:
		#	p.setColor(color)

		return p

	def style_sheet(self, css_module):
		"""
		Return a style sheet css object from the given resource name.
		:rtype: str 
		"""
		imported = getattr(__import__('css', fromlist=[css_module]), css_module)

		return imported.css


		