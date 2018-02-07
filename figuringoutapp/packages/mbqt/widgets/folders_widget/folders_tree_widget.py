import os

from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui



class FoldersTreeWidget(QtWidgets.QTreeWidget):

	itemDropped = QtCore.Signal(object)
	itemRenamed = QtCore.Signal(str, str)
	itemSelectionChanged = QtCore.Signal()

	def __init__(self, parent=None):
		super(FoldersTreeWidget, self).__init__(parent)

		self._dpi = 1

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

		self.create_gui()
		self.create_layout()

	def create_gui(self):
		pass

	def create_layout(self):
		pass

	def setModel(self, model):

		super(FoldersTreeWidget, self).setModel(model)

		self.selection_model = self.selectionModel()

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

class FileSystemModel(QtWidgets.QFileSystemModel):

	def __init__(self, foldersWidget):
		"""
		:type foldersWidget: FileSystemWidget
		"""
		QtWidgets.QFileSystemModel.__init__(self, foldersWidget)

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
					if folder.isBold():
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
		self._folderWidget = folderWidget
		QtCore.QSortFilterProxyModel.__init__(self, folderWidget)

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