import os
import sys
#
# if "QT_PREFERRED_BINDING" not in os.environ:
# 	os.environ["QT_PREFERRED_BINDING"] = os.pathsep.join(
# 		["PySide2", "PyQt5", "PySide", "PyQt4"]
# 	)

from Qt import QtCore
from Qt import QtWidgets

from packages import gui
import resource


AAM_PATH = 'D:/Git_Stuff/temp-aam'
if AAM_PATH not in sys.path:
	sys.path.append(AAM_PATH)

PACKAGES_PATH = os.path.join('D:/Git_Stuff/temp-aam/', 'packages')
if PACKAGES_PATH not in sys.path:
	sys.path.append(PACKAGES_PATH)

episode_root = 'S:/STUDIO_TEAMSPACE/fake'
ARMADA_DATA_PATH = os.path.join(episode_root, '_ArmadaData')
if ARMADA_DATA_PATH not in sys.path:
	sys.path.append(ARMADA_DATA_PATH)


class MainAAM(QtWidgets.QWidget):
	
	def __init__(self):
		super(MainAAM, self).__init__()

		self.resize(900, 800)  
		self.setStyleSheet(resource.style_sheet('main_window_css'))

		# GUI -----------------------------
		self.title_image = QtWidgets.QLabel(self)
		self.title_image.setPixmap(resource.pixmap('aam_banner_left'))

		# Address bar
		self.le_address_bar = QtWidgets.QLineEdit()
		self.le_address_bar.setText('S:/STUDIO_TEAMSPACE/fake/Asset_Builds/Character/CharacterA/Publish')
		self.le_address_bar.setReadOnly(True)
		self.le_address_bar.setObjectName('aamAddressBar')

		# Browse folders button
		self.btn_browse_folders = QtWidgets.QPushButton(self)
		self.icon = resource.icon('aam_browse_folders')
		self.btn_browse_folders.setIcon(self.icon)
		self.btn_browse_folders.setIconSize(QtCore.QSize(30, 30))
		self.btn_browse_folders.setMaximumHeight(50)
		self.btn_browse_folders.setStyleSheet(resource.style_sheet('push_button_w_icon_css'))
		self.btn_browse_folders.setObjectName('aamBrowseFolders')

		# Refresh Button
		self.btn_refresh = QtWidgets.QPushButton(self)
		self.icon = resource.icon('aam_refresh')
		self.btn_refresh.setIcon(self.icon)
		self.btn_refresh.setIconSize(QtCore.QSize(30, 30))
		self.btn_refresh.setMaximumHeight(50)
		self.btn_refresh.setStyleSheet(resource.style_sheet('push_button_w_icon_css'))
		self.btn_refresh.setObjectName('aamRefresh')

		# self.tv_browse_folders = Browser.Build(self)

		# Tab widget
		self.main_tab_widget = QtWidgets.QTabWidget()
		self.tabw_manager = QtWidgets.QWidget()
		self.tabw_import = QtWidgets.QWidget()
		self.tabw_publish =	gui.PubTab(self)
		self.main_tab_widget.addTab(self.tabw_manager, "Manager")
		self.main_tab_widget.addTab(self.tabw_import, "Import")
		self.main_tab_widget.addTab(self.tabw_publish, "Publish")
		self.main_tab_widget.setCurrentIndex(2)

		# Layout -----------------------------
		
		title_image_layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
		title_image_layout.addWidget(self.title_image)
		title_image_layout.addWidget(self.le_address_bar)
		title_image_layout.addWidget(self.btn_browse_folders)
		title_image_layout.addWidget(self.btn_refresh)



		self.main_layout = QtWidgets.QVBoxLayout()
		self.main_layout.addLayout(title_image_layout)
		# self.main_layout.addWidget(self.tv_browse_folders)
		self.main_layout.addWidget(self.main_tab_widget)

		self.setLayout(self.main_layout)


