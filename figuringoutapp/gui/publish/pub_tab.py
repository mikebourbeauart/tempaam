"""
Module for main PublishTab

The PublishTab only reads data from xml files saved in the open file's Publish directory
"""

import os

from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets

import mbqt

from publish import pub_selection_tab_info
from publish import pub_options_tab

try:
	from mb_logger import mb_logging as logging
except:
	import logging

logger = logging.getLogger(__name__)

class PubTab(QtWidgets.QWidget):
	'''Fills publish UI with contents''' 
	
	def __init__(self, parent=None):
		super(PubTab, self).__init__(parent)

		logger.warning('Building Publish tab...')

		self.parent = parent
		self.setObjectName('aamPublishTab')
		self.icon_dir = self.parent.icon_dir

		# Commands
		self.create_gui()
		self.create_layout()
		self.create_connections()


	#------------------------------------------------------
	def create_gui( self ):
		val = 100

		# Refresh Button
		self.btn_refresh = QtWidgets.QPushButton()
		icon = QtGui.QIcon(QtGui.QPixmap(os.path.join(self.icon_dir, 'aam_refresh.png')))
		self.btn_refresh.setIcon(icon)
		self.btn_refresh.setMaximumWidth(40)
		
		self.trw_folders = mbqt.FoldersWidget()
		self.trw_publish = mbqt.TreeWidget()

		self.tw_selection_info = mbqt.SelTabWidget()
		self.tw_selection_info.addTab(pub_selection_tab_info.Build(), "Selection Info")

		self.tw_options = mbqt.OptionTabWidget()
		self.tw_options.addTab(pub_options_tab.Build(), "Options")


	#------------------------------------------------------
	def create_layout(self):
		prep_layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
		prep_layout.addWidget(self.btn_refresh) 

		self.splt_widgets = QtWidgets.QSplitter()
		self.splt_widgets.addWidget(self.trw_folders)
		self.splt_widgets.addWidget(self.trw_publish)
		self.splt_widgets.setChildrenCollapsible(False)
		self.splt_widgets.setHandleWidth(10)

		asset_list_layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
		asset_list_layout.addWidget(self.splt_widgets)
		asset_list_layout.addWidget(self.tw_selection_info)
		
		self.main_layout = QtWidgets.QVBoxLayout(self)
		self.main_layout.addLayout(prep_layout)
		self.main_layout.addLayout(asset_list_layout)
		
		self.main_layout.addWidget(self.tw_options)


		self.setLayout(self.main_layout)

	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	def create_connections(self):
		
		pass
	
	
