import sys

from Qt import QtWidgets
from Qt import QtCore


class FoldersWidget(QtWidgets.QWidget):

	def __init__(self):
		super(FoldersWidget, self).__init__()

		self.btn_folders_options = None
		self.trw_folders = None
		self.trw_files = None
		self.main_layout = None

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
		self.trw_folders.selectionModel().selectionChanged.connect(self.trw_folders.selection_changed)


class FoldersTreeView(QtWidgets.QTreeView):

	def __init__(self, parent=None):
		super(FoldersTreeView, self).__init__(parent)

		self.selection_model = None

		self.mPath = "S:/Projects/Firstborn/STUDIO_TEAMSPACE/Episodes/fake/_ArmadaData/PublishData/Asset_Builds"

		self._sourceModel = FolderSystemModel(self)

		proxy_model = FolderSortFilterProxyModel(self)
		proxy_model.setSourceModel(self._sourceModel)
		proxy_model.sort(0)

		self.setModel(proxy_model)
		self.set_root_path(self.mPath)

	def setModel(self, model):
		super(FoldersTreeView, self).setModel(model)
		self.selection_model = self.selectionModel()

	def selection_changed(self, selected=None, deselected=None):
		"""
		Triggered when the folder item changes selection.

		:type selected: list[Folder] or None
		:type deselected: list[Folder] or None
		:rtype: None
		"""
		print selected
		print deselected
		index = self.selected_index()  # self.model().sourceModel().index(path)
		index_path = self.path_from_index(index[0])

		# mPath = self.selectionModel().sourceModel().fileInfo(fileIndex)#.absoluteFilePath()
		# self._sourceModel.setRootIndex(self._sourceModel.setRootPath(index_path))

	def selected_index(self):
		"""
		:rtype: list[Folder]
		"""

		for index in self.selectionModel().selectedIndexes():
			return index

	def path_from_index(self, index):
		"""
		:type index: QtCore.QModelIndex
		:rtype: str
		"""
		index = self.model().mapToSource(index)
		return self.model().sourceModel().filePath(index)

	def index_from_path(self, path):
		"""
		:type path: str
		:rtype: QtCore.QModelIndex
		"""
		index = self.model().sourceModel().index(path)
		return self.model().mapFromSource(index)

	def set_root_path(self, path):
		"""Set the model's root :path:
		:type path: str
		"""
		self.model().sourceModel().setRootPath(path)
		index = self.index_from_path(path)
		self.setRootIndex(index)


class FolderSystemModel(QtWidgets.QFileSystemModel):

	def __init__(self, folders_widget):
		"""
		:type folders_widget: FileSystemWidget
		"""
		super(FolderSystemModel, self).__init__(folders_widget)

		self.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)


class FolderSortFilterProxyModel(QtCore.QSortFilterProxyModel):

	def __init__(self, folders_widget):
		"""
		:type folders_widget: FileSystemWidget
		"""

		super(FolderSortFilterProxyModel, self).__init__(folders_widget)

		self._folderWidget = folders_widget


class FilesTreeView(QtWidgets.QTreeView):

	def __init__(self, parent=None):
		super(FilesTreeView, self).__init__(parent)

		self.mPath = "S:/Projects/Firstborn/STUDIO_TEAMSPACE/Episodes/fake/_ArmadaData/PublishData/Asset_Builds"

		self._sourceModel = FilesSystemModel(self)

		proxy_model = FilesSortFilterProxyModel(self)
		proxy_model.setSourceModel(self._sourceModel)
		proxy_model.sort(0)

		self.setModel(proxy_model)

		self.set_root_path(self.mPath)

	def index_from_path(self, path):
		"""
		:type path: str
		:rtype: QtCore.QModelIndex
		"""
		index = self.model().sourceModel().index(path)
		return self.model().mapFromSource(index)

	def set_root_path(self, path):
		"""Set the model's root :path:
		:type path: str
		"""
		self.model().sourceModel().setRootPath(path)
		index = self.index_from_path(path)
		self.setRootIndex(index)


class FilesSystemModel(QtWidgets.QFileSystemModel):

	def __init__(self, folders_widget):
		"""
		:type folders_widget: FileSystemWidget
		"""
		super(FilesSystemModel, self).__init__(folders_widget)

		self.setFilter(QtCore.QDir.Files | QtCore.QDir.NoDotAndDotDot)


class FilesSortFilterProxyModel(QtCore.QSortFilterProxyModel):

	def __init__(self, folders_widget):
		"""
		:type folders_widget: FileSystemWidget
		"""

		super(FilesSortFilterProxyModel, self).__init__(folders_widget)

		self._folderWidget = folders_widget


"""
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
"""


def main():
	"""For developing JUST from an IDE"""
	app = QtWidgets.QApplication(sys.argv)
	ex = FoldersWidget()
	ex.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	# main()
	#     '''For developing using MayaCharm from an IDE'''

	ui = None

	try:
		ui.close()
	except:
		pass

	ui = FoldersWidget()
	ui.show()
