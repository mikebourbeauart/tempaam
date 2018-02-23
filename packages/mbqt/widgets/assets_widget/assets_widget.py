
from Qt import QtWidgets
from Qt import QtCore

from assets_tree_widget import AssetsTreeWidget

import resource

class AssetsWidget(QtWidgets.QWidget):

	def __init__(self):
		super(AssetsWidget, self).__init__()

		# GUI -----------------------------
		# Browse folders button
		self.btn_folders_options = QtWidgets.QPushButton(self)
		self.icon = resource.icon('aam_browse_folders')
		self.btn_folders_options.setIcon(self.icon)
		self.btn_folders_options.setIconSize(QtCore.QSize(30, 30))
		self.btn_folders_options.setMaximumHeight(50)
		self.btn_folders_options.setStyleSheet(resource.style_sheet('push_button_w_icon_css'))
		self.btn_folders_options.setObjectName('aamBrowseFolders')

		self.tv_assets = AssetsTreeWidget()

		# Layout -------------------------
		self.main_layout = QtWidgets.QVBoxLayout(self)		
		self.main_layout.addWidget(self.btn_folders_options)
		self.main_layout.addWidget(self.tv_assets)

		self.setLayout(self.main_layout)
