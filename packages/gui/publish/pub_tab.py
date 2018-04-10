"""
Module for main PublishTab

The PublishTab only reads data from xml files saved in the open file's Publish directory
"""

from Qt import QtCore
from Qt import QtWidgets

from ...gui import folders_widget
from ...gui import assets_widget
from ...gui import selection_tab
from ...gui import options_tab

try:
	from mb_logger import mb_logging as logging
except:
	import logging

logger = logging.getLogger(__name__)


class PubTab(QtWidgets.QWidget):
	"""
	Fills publish UI with contents

	Connection gets data from folders_tree_view and sends it to assets_tree_view
	"""
	
	def __init__(self, parent=None):
		super(PubTab, self).__init__(parent)

		logger.warning('Building Publish tab...')

		self.parent = parent
		self.setObjectName('PublishTab')

		# GUI -----------------------------
		self.folders_widget = folders_widget.FoldersWidget()
		self.assets_widget = assets_widget.AssetsWidget()
		self.tw_selection_info = selection_tab.SelTabWidget()
		self.tw_options = options_tab.OptionsTabWidget()

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
		self.folders_widget.tv_folders.itemSelectionChanged.connect(self.assets_widget.tv_assets.set_root_path)
	
	
