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
		self.setObjectName('PublishTab')

		# Commands
		self.create_gui()
		self.create_layout()
		self.create_connections()


	#------------------------------------------------------
	def create_gui( self ):

		self.trw_folders = mbqt.FoldersWidget()
		self.trw_publish = mbqt.AssetsWidget()
		self.tw_selection_info = mbqt.SelTabWidget()
		self.tw_options = mbqt.OptionsTabWidget()

	#------------------------------------------------------
	def create_layout(self):		

		self.asset_splt = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
		self.asset_splt.addWidget(self.trw_folders)
		self.asset_splt.addWidget(self.trw_publish)
		self.asset_splt.addWidget(self.tw_selection_info)
		self.asset_splt.setChildrenCollapsible(False)
		self.asset_splt.setStretchFactor(1,1)
		self.asset_splt.setHandleWidth(5)

		self.vert_splt = QtWidgets.QSplitter(QtCore.Qt.Vertical)
		self.vert_splt.addWidget(self.asset_splt)
		self.vert_splt.addWidget(self.tw_options)
		self.vert_splt.setChildrenCollapsible(False)
		self.vert_splt.setStretchFactor(0,1)
		self.vert_splt.setHandleWidth(5)

		self.main_layout = QtWidgets.QVBoxLayout(self)		
		self.main_layout.addWidget(self.vert_splt)

		self.setLayout(self.main_layout)

	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	def create_connections(self):
		
		pass
	
	
