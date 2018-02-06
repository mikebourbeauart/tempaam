import os

from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui

class FoldersWidget(QtWidgets.QTreeWidget):

	def __init__(self):
		super(FoldersWidget, self).__init__()

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
		# Browse folders button
		self.btn_browse_folders = QtWidgets.QPushButton(self)
		self.icon = QtGui.QIcon(QtGui.QPixmap(os.path.join(self.icon_dir, 'ftrack_browse_folders.png')))
		self.btn_browse_folders.setIcon(self.icon)
		self.btn_browse_folders.setIconSize(QtCore.QSize(30, 30))
		self.btn_browse_folders.setMaximumHeight(50)
		self.btn_browse_folders.setStyleSheet(push_button_w_icon_css.css)
		self.btn_browse_folders.setObjectName('aamBrowseFolders')

	def create_layout(self):
		self.main_layout = QtWidgets.QVBoxLayout(self)		
		self.main_layout.addWidget(self.btn_browse_folders)
		self.main_layout.addWidget(self)

		self.setLayout(self.main_layout)

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