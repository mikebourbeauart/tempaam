"""
Module for main PublishTab

The PublishTab only reads data from xml files saved in the open file's Publish directory
"""

import os

from Qt import QtCore
from Qt import QtWidgets

from packages import mbqt

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

		# GUI -----------------------------
		self.folders_widget = mbqt.FoldersWidget()
		self.assets_widget = mbqt.AssetsWidget()
		self.tw_selection_info = mbqt.SelTabWidget()
		self.tw_options = mbqt.OptionsTabWidget()

		# Layout -------------------------
		self.asset_splt = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
		self.asset_splt.addWidget(self.folders_widget)
		self.asset_splt.addWidget(self.assets_widget)
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

		# Connections ---------------------
		self.folders_widget.itemSelectionChanged.connect(self.assets_widget.set_root_path)
	
	
