import os
import sys

from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui


class FoldersWidget(QtWidgets.QWidget):

	def __init__(self):
		super(FoldersWidget, self).__init__()

		self.create_gui()
		self.create_layout()
		self.create_connections()

	def create_gui(self):
		# Browse folders button
		self.btn_folders_options = QtWidgets.QPushButton(self)
		self.btn_folders_options.setIconSize(QtCore.QSize(30, 30))
		self.btn_folders_options.setMaximumHeight(50)
		self.btn_folders_options.setObjectName('aamBrowseFolders')

		self.trw_folders = FoldersTreeView()
		self.trw_files = FilesTreeView()

	def create_layout(self):
		self.main_layout = QtWidgets.QHBoxLayout(self)
		self.main_layout.addWidget(self.btn_folders_options)
		self.main_layout.addWidget(self.trw_folders)
		self.main_layout.addWidget(self.trw_files)

		self.setLayout(self.main_layout)


	def create_connections(self):
		self.trw_folders.selectionModel().selectionChanged.connect(self.trw_folders._selectionChanged)


class FoldersTreeView(QtWidgets.QTreeView):

	def __init__(self, parent=None):
		super(FoldersTreeView, self).__init__(parent)

		self.mPath = "S:/STUDIO_TEAMSPACE/Episodes/fake/_ArmadaData/PublishData/Asset_Builds"

		self._sourceModel = FolderSystemModel(self)

		proxyModel = FolderSortFilterProxyModel(self)
		proxyModel.setSourceModel(self._sourceModel)
		proxyModel.sort(0)

		self.setModel(proxyModel)
		self.setRootPath(self.mPath)

		#self.selectionModel().selectionChanged.connect(self._selectionChanged)

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
		print selected
		print deselected
		index = self.selectedIndex() #self.model().sourceModel().index(path)
		indexPath = self.pathFromIndex(index)

		#mPath = self.selectionModel().sourceModel().fileInfo(fileIndex)#.absoluteFilePath()
		#self._sourceModel.setRootIndex(self._sourceModel.setRootPath(mPathindexPath))


	def selectedIndex(self):
		"""
		:rtype: list[Folder]
		"""

		folders = []

		for index in self.selectionModel().selectedIndexes():

			return index

	def pathFromIndex(self, index):
		"""
		:type index: QtCore.QModelIndex
		:rtype: str
		"""
		index = self.model().mapToSource(index)
		return self.model().sourceModel().filePath(index)

	def indexFromPath(self, path):
		"""
		:type path: str
		:rtype: QtCore.QModelIndex
		"""
		index = self.model().sourceModel().index(path)
		return self.model().mapFromSource(index)

	def setRootPath(self, path):
		"""Set the model's root :path:
		:type path: str
		"""
		self.model().sourceModel().setRootPath(path)
		index = self.indexFromPath(path)
		self.setRootIndex(index)

class FolderSystemModel(QtWidgets.QFileSystemModel):

	def __init__(self, foldersWidget):
		"""
		:type foldersWidget: FileSystemWidget
		"""
		super(FolderSystemModel, self).__init__(foldersWidget)


		self.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)


class FolderSortFilterProxyModel(QtCore.QSortFilterProxyModel):

	def __init__(self, folderWidget):
		"""
		:type folderWidget: FileSystemWidget
		"""

		super(FolderSortFilterProxyModel, self).__init__(folderWidget)

		self._folderWidget = folderWidget


class FilesTreeView(QtWidgets.QTreeView):

	def __init__(self, parent=None):
		super(FilesTreeView, self).__init__(parent)

		self.mPath = "S:/STUDIO_TEAMSPACE/Episodes/fake/_ArmadaData/PublishData/Asset_Builds"

		self._sourceModel = FilesSystemModel(self)

		proxyModel = FilesSortFilterProxyModel(self)
		proxyModel.setSourceModel(self._sourceModel)
		proxyModel.sort(0)

		self.setModel(proxyModel)

		self.setRootPath(self.mPath)

	def indexFromPath(self, path):
		"""
		:type path: str
		:rtype: QtCore.QModelIndex
		"""
		index = self.model().sourceModel().index(path)
		return self.model().mapFromSource(index)

	def setRootPath(self, path):
		"""Set the model's root :path:
		:type path: str
		"""
		self.model().sourceModel().setRootPath(path)
		index = self.indexFromPath(path)
		self.setRootIndex(index)

class FilesSystemModel(QtWidgets.QFileSystemModel):

	def __init__(self, foldersWidget):
		"""
		:type foldersWidget: FileSystemWidget
		"""
		super(FilesSystemModel, self).__init__(foldersWidget)


		self.setFilter(QtCore.QDir.Files | QtCore.QDir.NoDotAndDotDot)


class FilesSortFilterProxyModel(QtCore.QSortFilterProxyModel):

	def __init__(self, folderWidget):
		"""
		:type folderWidget: FileSystemWidget
		"""

		super(FilesSortFilterProxyModel, self).__init__(folderWidget)

		self._folderWidget = folderWidget

'''
	// FILES

	fileModel = new QFileSystemModel(this);

	// Set filter
	fileModel->setFilter(QDir::NoDotAndDotDot |
						QDir::Files);

	// QFileSystemModel requires root path
	fileModel->setRootPath(mPath);

	// Attach the file model to the view
	ui->listView->setModel(fileModel);
}

QFileSystemModelDialog::~QFileSystemModelDialog()
{
	delete ui;
}

void QFileSystemModelDialog::on_treeView_clicked(const QModelIndex &index;)
{
	// TreeView clicked
	// 1. We need to extract path
	// 2. Set that path into our ListView

	// Get the full path of the item that's user clicked on
	QString mPath = dirModel->fileInfo(index).absoluteFilePath();
	ui->listView->setRootIndex(fileModel->setRootPath(mPath));

}
'''


def main():
    '''For developing JUST from an IDE'''
    app = QtWidgets.QApplication(sys.argv)
    ex = FoldersWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    #main()

    '''For developing using MayaCharm from an IDE'''
    try:
        ui.close()
    except:
        pass

    ui = FoldersWidget()
    ui.show()
