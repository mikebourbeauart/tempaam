import os

from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui



class FoldersTreeWidget(QtWidgets.QTreeWidget):

	def __init__(self):
		super(FoldersTreeWidget, self).__init__()

		self._dpi = 1

		self.setDpi(1)

		self.setAcceptDrops(True)
		self.setHeaderHidden(True)
		self.setMouseTracking(True)
		self.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.setSelectionMode(QtWidgets.QTreeWidget.ExtendedSelection)
		self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
		self.setMinimumWidth(200)
		self.setMaximumWidth(600)

		self.create_gui()
		self.create_layout()

	def create_gui(self):
		pass

	def create_layout(self):
		pass

	def dpi(self):
		"""
		Return the dots per inch multiplier.

		:rtype: float
		"""
		return self._dpi

	def setDpi(self, dpi):
		"""
		Set the dots per inch multiplier.

		:type dpi: float
		:rtype: None
		"""
		size = 24 * dpi
		self.setIndentation(15 * dpi)
		self.setMinimumWidth(35 * dpi)
		self.setIconSize(QtCore.QSize(size, size))
		self.setStyleSheet("height: {size}".format(size=size))

	def update(self, *args):
		"""
		:rtype: None
		"""
		for item in self.items():
			item.update()

	def items(self):
		"""
		Return a list of all the items in the tree widget.

		:rtype: list[NavigationWidgetItem]
		"""
		items = self.findItems(
			"*",
			QtCore.Qt.MatchWildcard | QtCore.Qt.MatchRecursive
		)

		return items