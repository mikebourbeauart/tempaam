import os

from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui

from folders_tree_widget import FoldersTreeWidget
from css import push_button_w_icon_css

import resource

class FoldersWidget(QtWidgets.QWidget):

	def __init__(self):
		super(FoldersWidget, self).__init__()

		self.create_gui()
		self.create_layout()

	def create_gui(self):
		# Browse folders button
		self.btn_folders_options = QtWidgets.QPushButton(self)
		self.btn_folders_options.setIcon(resource.icon('aam_browse_folders'))
		self.btn_folders_options.setIconSize(QtCore.QSize(30, 30))
		self.btn_folders_options.setMaximumHeight(50)
		self.btn_folders_options.setStyleSheet(resource.style_sheet('push_button_w_icon_css'))
		self.btn_folders_options.setObjectName('aamBrowseFolders')

		self.trw_folders = FoldersTreeWidget()

	def create_layout(self):
		self.main_layout = QtWidgets.QVBoxLayout(self)		
		self.main_layout.addWidget(self.btn_folders_options)
		self.main_layout.addWidget(self.trw_folders)

		self.setLayout(self.main_layout)
