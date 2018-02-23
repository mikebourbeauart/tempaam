import os

from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui

import folders_item
import utils


class FoldersTreeView(QtWidgets.QTreeView):

	itemSelectionChanged = QtCore.Signal()

	def __init__(self, parent=None):
		super(FoldersTreeView, self).__init__(parent)

		self._filter = []
		self._folders = {}
		self._isLocked = False
		self._blockSignals = False
		self._enableFolderSettings = False

		self._sourceModel = FileSystemModel(self)

		self.setDpi(1)

		proxyModel = SortFilterProxyModel(self)
		proxyModel.setSourceModel(self._sourceModel)
		proxyModel.sort(0)

		self.setAcceptDrops(True)
		self.setModel(proxyModel)
		self.setHeaderHidden(True)
		self.setMouseTracking(True)
		self.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.setSelectionMode(QtWidgets.QTreeWidget.ExtendedSelection)
		self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
		self.setMinimumWidth(200)
		self.setMaximumWidth(600)

		self.setRootPath(utils.asset_builds_root(self))

		self.selectionModel().selectionChanged.connect(self._selectionChanged)

		self.create_gui()
		self.create_layout()


	def setModel(self, model):

		super(FoldersTreeView, self).setModel(model)

		self.selection_model = self.selectionModel()

	def _selectionChanged(self, selected=None, deselected=None):
		"""
		Triggered when the folder item changes selection.

		:type selected: list[Folder] or None
		:type deselected: list[Folder] or None
		:rtype: None
		"""
		print 'hey'
		if not self._blockSignals:
			self.itemSelectionChanged.emit()

	def create_gui(self):
		pass

	def create_layout(self):
		pass

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

	def folderFromPath(self, path):
		"""Create a folder item from path
		:type path: str
		:rtype: Folder
		"""
		folders = self._folders
		if path not in folders:
			folders[path] = folders_item.FoldersItem(path, self)
		return folders[path]

	def indexFromPath(self, path):
		"""Get the model index from :path:
		:type path: str
		:rtype: QtCore.QModelIndex
		"""
		print path
		index = self.model().sourceModel().index(path)
		return self.model().mapFromSource(index)

	def setRootPath(self, path):
		"""Set the model's root :path:
		:type path: str
		"""
		self.model().sourceModel().setRootPath(path)
		index = self.indexFromPath(path)
		self.setRootIndex(index)



class FileSystemModel(QtWidgets.QFileSystemModel):

	def __init__(self, foldersWidget):
		"""
		:type foldersWidget: FileSystemWidget
		"""
		super(FileSystemModel, self).__init__(foldersWidget)

		self._ignoreFilter = []
		self._foldersWidget = foldersWidget
		self.setFilter(QtCore.QDir.AllDirs)

	def foldersWidget(self):
		"""
		:rtype: FileSystemWidget
		"""
		return self._foldersWidget

	def columnCount(self, *args):
		"""
		:type args: list
		:rtype: int
		"""
		return 1

	def ignoreFilter(self):
		"""
		:rtype: list or None
		"""
		return self._ignoreFilter

	def setIgnoreFilter(self, ignoreFilter):
		"""
		:type ignoreFilter: list or None
		"""
		self._ignoreFilter = ignoreFilter or []

	def isPathValid(self, path):
		"""
		:type path: str
		:rtype: bool
		"""
		if os.path.isdir(path):
			path = path.lower()
			valid = [item for item in self._ignoreFilter if path.endswith(item)]
			if not valid:
				return True
		return False

	def hasChildren(self, index):
		"""
		:type index: QtCore.QModelIndex
		:rtype: bool
		"""
		path = self.filePath(index)
		if os.path.isdir(path):
			for name in os.listdir(path):
				if self.isPathValid(path + "/" + name):
					return True
		return False




	def data(self, index, role):
		"""
		:type index: QtCore.QModelIndex
		:type role:
		:rtype: QtWidgets.QVariant
		"""
		if role == QtCore.Qt.DecorationRole:
			if index.column() == 0:
				dirname = self.filePath(index)
				folder = self.foldersWidget().folderFromPath(dirname)
				pixmap = QtGui.QIcon(folder.pixmap())

				if pixmap:
					pixmap = pixmap.pixmap(self.foldersWidget().iconSize(),
								  transformMode=QtCore.Qt.SmoothTransformation)

					return QtGui.QIcon(pixmap)
				else:
					return None

		if role == QtCore.Qt.FontRole:
			if index.column() == 0:
				dirname = self.filePath(index)
				folder = self.foldersWidget().folderFromPath(dirname)
				if folder.exists():
					#if folder.isBold():
					font = QtGui.QFont()
					font.setBold(True)
					return font

		if role == QtCore.Qt.DisplayRole:
			text = QtWidgets.QFileSystemModel.data(self, index, role)
			return text

		return QtWidgets.QFileSystemModel.data(self, index, role)


class SortFilterProxyModel(QtCore.QSortFilterProxyModel):

	def __init__(self, folderWidget):
		"""
		:type folderWidget: FileSystemWidget
		"""

		super(SortFilterProxyModel, self).__init__(folderWidget)

		self._folderWidget = folderWidget



	def folderWidget(self):
		"""
		:rtype: FileSystemWidget
		"""
		return self._folderWidget

	def lessThan(self, leftIndex, rightIndex):
		"""
		:type leftIndex: QtWidgets.QModelIndex
		:type rightIndex: QtWidgets.QModelIndex
		:rtype: bool
		"""
		path1 = self.sourceModel().filePath(leftIndex)
		path2 = self.sourceModel().filePath(rightIndex)

		folder1 = self.folderWidget().folderFromPath(path1)
		folder2 = self.folderWidget().folderFromPath(path2)

		orderIndex1 = folder1.orderIndex()
		orderIndex2 = folder2.orderIndex()

		if orderIndex1 >= 0 and orderIndex2 >= 0:

			if orderIndex1 < orderIndex2:
				return True
			else:
				return False

		elif orderIndex1 >= 0:
			return True

		else:
			return False

	def filterAcceptsRow(self, sourceRow, sourceParent):
		"""
		:type sourceRow:
		:type sourceParent:
		:rtype: bool
		"""

		index = self.sourceModel().index(sourceRow, 0, sourceParent)
		path = self.sourceModel().filePath(index)
		return self.sourceModel().isPathValid(path)















