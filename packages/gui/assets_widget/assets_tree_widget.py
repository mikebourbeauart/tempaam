
from Qt import QtWidgets
from Qt import QtCore

import assets_item
import utils_aam


class AssetsTreeWidget(QtWidgets.QTreeView):

	def __init__(self):
		super(AssetsTreeWidget, self).__init__()

		# Variables
		self._filter = []
		self._folders = {}
		self._isLocked = False
		self._blockSignals = False
		self._enableFolderSettings = False

		# Model stuff
		self._sourceModel = FileSystemModel(self)
		proxy_model = SortFilterProxyModel(self)
		proxy_model.setSourceModel(self._sourceModel)
		proxy_model.sort(0)
		self.setModel(proxy_model)

		# Settings
		self.setAcceptDrops(True)
		self.setHeaderHidden(True)
		self.setMouseTracking(True)
		self.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.setSelectionMode(QtWidgets.QTreeWidget.ExtendedSelection)
		self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
		self.setMinimumHeight(500)
		self.setMinimumWidth(400)

		# Commands
		self.setDpi(1)
		self.set_root_path(utils_aam.asset_builds_root(self))

		# Connections ---------------------
		# self.selectionModel().selectionChanged.connect(self._selection_changed)

	def setModel(self, model):
		"""Override setModel method"""
		super(AssetsTreeWidget, self).setModel(model)
		self.selection_model = self.selectionModel()

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

	def _selection_changed(self):
		"""
		Triggered when the folder item changes selection.
		"""
		path = self.current_folder_selection()
		print 'init signal'
		self.itemSelectionChanged.emit(path)

	def current_folder_selection(self):
		# Get current selection
		index = self.currentIndex()
		return self.path_from_index(index)

	def path_from_index(self, index):
		"""
		:type index: QtCore.QModelIndex
		:rtype: str
		"""
		# Get index from source model
		index = self.model().mapToSource(index)
		return self.model().sourceModel().filePath(index)

	def index_from_path(self, path):
		"""
		:type path: str
		:rtype: QtCore.QModelIndex
		"""
		# Get index
		index = self.model().sourceModel().index(path)
		# Map index from source to sort filter
		return self.model().mapFromSource(index)

	def set_root_path(self, path):
		"""Set the model's root :path:
		:type path: str
		"""
		# Set root path
		self.model().sourceModel().setRootPath(path)
		index = self.index_from_path(path) # hide until i figure this out
		# Set root index
		self.setRootIndex(index)


class FileSystemModel(QtWidgets.QFileSystemModel):

	def __init__(self, foldersWidget):
		"""
		:type foldersWidget: FileSystemWidget
		"""
		super(FileSystemModel, self).__init__(foldersWidget)

		self._ignoreFilter = []
		self._foldersWidget = foldersWidget
		self.setFilter(QtCore.QDir.Files | QtCore.QDir.NoDotAndDotDot)


class SortFilterProxyModel(QtCore.QSortFilterProxyModel):

	def __init__(self, folderWidget):
		"""
		:type folderWidget: FileSystemWidget
		"""

		super(SortFilterProxyModel, self).__init__(folderWidget)

		self._folderWidget = folderWidget













