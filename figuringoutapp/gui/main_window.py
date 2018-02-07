import os
import sys

import os

if "QT_PREFERRED_BINDING" not in os.environ:
	os.environ["QT_PREFERRED_BINDING"] = os.pathsep.join(
		["PySide2", "PyQt5", "PySide", "PyQt4"]
	)


from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets

MB_AAM_PATH = os.path.join('D:/Git_Stuff/temp-aam/figuringoutapp')
if not MB_AAM_PATH in sys.path:
	sys.path.append(MB_AAM_PATH)

packages_path = os.path.join('D:/Git_Stuff/temp-aam/figuringoutapp/', 'packages')
if not packages_path in sys.path:
	sys.path.append(packages_path)

from css import main_window_css
from css import push_button_w_icon_css

from publish.pub_tab import PubTab

import mbqt
import resource

class MainAAM(QtWidgets.QWidget):
	
	def __init__(self):
		super(MainAAM, self).__init__()

		self.resize(900, 800)  
		self.setStyleSheet(resource.style_sheet('main_window_css'))

		self.create_gui()
		self.create_layout()
		self.create_connections()
		self.show()

	def create_gui(self):
		self.title_image = QtWidgets.QLabel(self)
		self.title_image.setPixmap(resource.pixmap('aam_banner_left'))

		# Address bar
		self.le_address_bar = QtWidgets.QLineEdit()
		self.le_address_bar.setText('S:/STUDIO_TEAMSPACE/Episodes/Mike_Bourbeau/Maya/Publish/RandomTest')
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
		self.tabw_publish =PubTab(self)
		self.main_tab_widget.addTab(self.tabw_manager, "Manager")
		self.main_tab_widget.addTab(self.tabw_import, "Import")
		self.main_tab_widget.addTab(self.tabw_publish, "Publish")
		self.main_tab_widget.setCurrentIndex(2)


	def create_layout(self):
		
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
		
	def create_connections(self):
		pass

def main():

	app = QtWidgets.QApplication(sys.argv)
	ex = MainAAM()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
