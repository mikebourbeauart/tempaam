import sys

from Qt import QtWidgets
from Qt import QtCore

# import maya.cmds as mc

WINDOW_TITLE = 'Folders Widget'
WINDOW_OBJECT = 'mainWindow'


# def _maya_delete_ui():
# 	"""Delete existing UI in Maya"""
# 	if mc.window(WINDOW_OBJECT, q=True, exists=True):
# 		mc.deleteUI(WINDOW_OBJECT)  # Delete window
# 	if mc.dockControl('MayaWindow|' + WINDOW_TITLE, q=True, ex=True):
# 		mc.deleteUI('MayaWindow|' + WINDOW_TITLE)  # Delete docked window
#
#
# def _maya_main_window():
# 	"""Return Maya's main window"""
# 	app = QtWidgets.QApplication.instance()
# 	for obj in app.topLevelWidgets():
# 		if obj.objectName() == 'MayaWindow':
# 			return obj
# 	raise RuntimeError('Could not find MayaWindow instance')


class FoldersWidget(QtWidgets.QDialog):

	def __init__(self, parent=None):
		super(FoldersWidget, self).__init__(parent)

		self.setObjectName(WINDOW_OBJECT)
		self.setMinimumSize(400, 300)
		self.setWindowTitle(WINDOW_TITLE)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

		# GUI -----------------------------
		self.btn_folders_options = QtWidgets.QPushButton(self) # Browse folders button
		self.btn_folders_options.setIconSize(QtCore.QSize(30, 30))
		self.btn_folders_options.setMaximumHeight(50)
		self.btn_folders_options.setObjectName('aamBrowseFolders')

		self.tv_folders = FoldersTreeView()
		self.tv_files = FilesTreeView()

		# Layout -------------------------
		self.main_layout = QtWidgets.QHBoxLayout(self)
		self.main_layout.addWidget(self.btn_folders_options)
		self.main_layout.addWidget(self.tv_folders)
		self.main_layout.addWidget(self.tv_files)

		self.setLayout(self.main_layout)

		# Connections ---------------------
		self.tv_folders.itemSelectionChanged.connect(self.tv_files.set_root_path)


class FoldersTreeView(QtWidgets.QTreeView):

	itemSelectionChanged = QtCore.Signal(str)

	def __init__(self, parent=None):
		super(FoldersTreeView, self).__init__(parent)

		self.mPath = 'S:/STUDIO_TEAMSPACE/Episodes/fake/_ArmadaData/PublishData/Asset_Builds'  # "S:/Projects/Firstborn/STUDIO_TEAMSPACE/Episodes/fake/_ArmadaData/PublishData/Asset_Builds"

		self._sourceModel = FolderSystemModel(self)

		proxy_model = FolderSortFilterProxyModel(self)
		proxy_model.setSourceModel(self._sourceModel)
		proxy_model.sort(0)

		self.setModel(proxy_model)

		self.set_root_path(self.mPath)

		# Connections ---------------------
		self.selectionModel().selectionChanged.connect(self.selection_changed)

	def setModel(self, model):
		super(FoldersTreeView, self).setModel(model)
		self.selection_model = self.selectionModel()

	def current_folder_selection(self):
		# Get current selection
		index = self.currentIndex()
		return self.path_from_index(index)

	def selection_changed(self, index=None):
		"""
		Triggered when the folder item changes selection.

		:type selected: list[Folder] or None
		:type deselected: list[Folder] or None
		:rtype: None
		"""
		path = self.current_folder_selection()
		print 'init signal'
		self.itemSelectionChanged.emit(path)

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

		self.mPath = 'S:/STUDIO_TEAMSPACE/Episodes/fake/_ArmadaData/PublishData/Asset_Builds'  # "S:/Projects/Firstborn/STUDIO_TEAMSPACE/Episodes/fake/_ArmadaData/PublishData/Asset_Builds"

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
		print path
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


########################################################################################################################
# def main():
# 	"""Run in Maya"""
# 	_maya_delete_ui()  # Delete any existing existing UI
# 	global window
# 	window = FoldersWidget(parent=_maya_main_window())
# 	window.show()  # Show the UI
#
# 	"""
# 	elif DOCK_WITH_MAYA_UI:
# 		allowedAreas = ['right', 'left']
# 		cmds.dockControl(WINDOW_TITLE, label=WINDOW_TITLE, area='left',
# 						 content=WINDOW_OBJECT, allowedArea=allowedAreas)
# 	"""

def main():

	app = QtWidgets.QApplication(sys.argv)
	window = FoldersWidget()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

