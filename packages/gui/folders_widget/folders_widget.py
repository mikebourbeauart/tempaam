from Qt import QtWidgets
from Qt import QtCore

import folders_tree_view

import resource

class FoldersWidget(QtWidgets.QWidget):
	"""Folder selection widget
	"""
	def __init__(self, parent=None):
		super(FoldersWidget, self).__init__(parent)

		self.setObjectName('foldersWidget')

		# GUI -----------------------------
		# Browse folders button
		self.btn_folders_options = QtWidgets.QPushButton(self)
		self.btn_folders_options.setIcon(resource.icon('aam_browse_folders'))
		self.btn_folders_options.setIconSize(QtCore.QSize(30, 30))
		self.btn_folders_options.setMaximumHeight(50)
		self.btn_folders_options.setStyleSheet(resource.style_sheet('push_button_w_icon_css'))
		self.btn_folders_options.setObjectName('aamBrowseFolders')

		self.tv_folders = folders_tree_view.FoldersTreeView()

		# Layout --------------------------
		self.main_layout = QtWidgets.QVBoxLayout(self)		
		self.main_layout.addWidget(self.btn_folders_options)
		self.main_layout.addWidget(self.tv_folders)

		self.setLayout(self.main_layout)

