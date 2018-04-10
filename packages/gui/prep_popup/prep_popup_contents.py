"""
Module for options tab within publish tab
"""

import os
import re
import platform

from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets

from aamUI import LineEdit

from aamCmds.treeView import tv_item_json_data

# TEMP for selection
import maya.cmds as mc

try:
	from mb_logger import mb_logging as logging
except:
	import logging

logger = logging.getLogger(__name__)

class PrepPopupContents(QtWidgets.QTabWidget):
	'''Fills prep UI with an options tab widget

	@param parent:
	@param mTaskTypes: lst, Ftrack task types - Queried from MainWindow during startup

	''' 
	
	def __init__( 
		self, 
		parent = None, 
		mTaskTypes = None
	):
		super(PrepPopupContents, self).__init__()

		self.parent = parent
		self.task_types = mTaskTypes

		self.software = os.getenv('SOFTWARE')
		self.icon_dir = os.getenv('ICONS_PATH').replace('\\', '/')

		self.setFixedHeight(200)
		
		# Set variable for toggling UE4 project path layout
		self.is_ue4_set = False

		self.create_gui()
		self.create_layout()
		self.create_connections()

	#------------------------------------------------------
	def create_gui(self):

		# Asset type
		self.lbl_asset_type = QtWidgets.QLabel( "Type:" )
		self.cb_asset_type = QtWidgets.QComboBox()
		#for task_type in self.task_types:
		#	self.cb_asset_type.addItem(task_type['name'], task_type['id'])
		self.cb_asset_type.addItems(['None', 'Scene', 'OBJ', 'FBX', 'DAE FBX', 'Rig', 'Animation', 'Alembic',  'Lights', 'Camera', 
			'UE4 SkelMesh', 'UE4 StaticMesh', 'UE4 CharAnim']
		)

		# UE4 Directory (only visible if user selects an UE4 asset type)
		self.lbl_asset_game_path = QtWidgets.QLabel('Game Path:')
		self.lbl_asset_game_path.hide()
		self.le_asset_game_path = QtWidgets.QLineEdit(self.parent.ftrack_data['game_data'])
		self.le_asset_game_path.setAlignment(QtCore.Qt.AlignRight)
		self.le_asset_game_path.hide()
		self.btn_asset_game_path = QtWidgets.QPushButton('Browse')
		self.btn_asset_game_path.hide()

		# UE4 Asset Name
		self.lbl_asset_game_name = QtWidgets.QLabel("UE4 Asset:")
		self.lbl_asset_game_name.hide()
		self.le_asset_game_name = QtWidgets.QLineEdit()
		self.le_asset_game_name.setAlignment(QtCore.Qt.AlignRight)
		self.le_asset_game_name.hide()

		# Asset name
		self.lbl_asset_name = QtWidgets.QLabel("Name:")
		self.le_asset_name = LineEdit_AssetName(
			mGameNameWidget = self.le_asset_game_name,
			mCheckboxWidget = self.cb_asset_type
		)
		self.le_asset_name.setAlignment(QtCore.Qt.AlignRight)
		#self.le_asset_name.setMaximumWidth( 195 )


		# Asset selection
		self.lbl_asset_selection = QtWidgets.QLabel("Selection:")
		self.lw_asset_selection = QtWidgets.QListWidget()
		self.btn_asset_store = QtWidgets.QPushButton("Store Selection")
		self.btn_asset_store.setMaximumWidth( 130 )

	#------------------------------------------------------
	def create_layout(self):
		self.type_layout = QtWidgets.QHBoxLayout()
		self.type_layout.addWidget( self.lbl_asset_type )
		self.type_layout.addWidget( self.cb_asset_type )

		self.name_layout = QtWidgets.QHBoxLayout()
		self.name_layout.addWidget( self.lbl_asset_name )
		self.name_layout.addWidget( self.le_asset_name )

		self.game_name_layout = QtWidgets.QHBoxLayout()
		self.game_name_layout.addWidget( self.lbl_asset_game_name )
		self.game_name_layout.addWidget( self.le_asset_game_name )

		self.game_path_layout = QtWidgets.QHBoxLayout()
		self.game_path_layout.addWidget(self.lbl_asset_game_path)
		self.game_path_layout.addWidget(self.le_asset_game_path)
		self.game_path_layout.addWidget(self.btn_asset_game_path)

		self.selection_layout = QtWidgets.QHBoxLayout()
		self.selection_layout.addWidget( self.lbl_asset_selection )
		self.selection_layout.addWidget( self.lw_asset_selection )

		self.store_layout = QtWidgets.QHBoxLayout()
		self.store_layout.addWidget( self.btn_asset_store )
		self.store_layout.setAlignment( QtCore.Qt.AlignRight )

		self.main_layout = QtWidgets.QVBoxLayout( self )
		self.main_layout.addStretch()
		self.main_layout.addLayout( self.type_layout )
		self.main_layout.addSpacing(7)
		self.main_layout.addLayout( self.game_path_layout )
		self.main_layout.addSpacing(7)
		self.main_layout.addLayout( self.name_layout )
		self.main_layout.addSpacing(7)
		self.main_layout.addLayout( self.game_name_layout )
		self.main_layout.addSpacing(7)
		self.main_layout.addLayout( self.selection_layout )
		self.main_layout.addLayout( self.store_layout )

		self.setLayout( self.main_layout )


	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	def create_connections(self):
		self.btn_asset_store.clicked.connect(self.on_store_selection)
		self.btn_asset_game_path.clicked.connect(self.on_browse_selection)
		self.cb_asset_type.currentIndexChanged.connect(self.on_type_selected)


	#-----#-----#-----#-----#-----#-----#-----#-----#-----#
	def on_type_selected(self):
		'''Execute when the asset type is changed'''

		# If the asset type is an UE4 asset, add the UE4 project path UI
		if 'UE4' in self.cb_asset_type.currentText():
			self.lbl_asset_game_path.show()
			self.le_asset_game_path.show()
			self.btn_asset_game_path.show()
			self.lbl_asset_game_name.show()
			self.le_asset_game_name.show()

		else:
			# Turn the toggle off
			self.lbl_asset_game_path.hide()
			self.le_asset_game_path.hide()
			self.btn_asset_game_path.hide()
			self.lbl_asset_game_name.hide()
			self.le_asset_game_name.hide()
		
		self.le_asset_game_name.setText('{0}_{1}'.format(self.le_asset_name.text(), self.cb_asset_type.currentText().replace('UE4 ', '')))

	#-----#-----#-----#-----#-----#-----#-----#-----#-----#
	def on_browse_selection(self):
		'''Execute when the browse button is pressed'''      

		if platform.system().lower() in ['windows']:
			executable = 'explorer'

		full_path = os.path.expanduser("~/Desktop")

		self.file_dialog = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select UE4 project path', full_path)

		self.le_asset_game_path.clear()
		self.le_asset_game_path.setText(self.file_dialog.replace('\\', '/'))

		logger.info(u'Browsed to directory : "%s"' % self.file_dialog)

	
	#-----#-----#-----#-----#-----#-----#-----#-----#-----#
	def on_store_selection(self):
		'''Stores the current selection in the popup's QListWidget''' 
		
		self.lw_asset_selection.clear()
		
		selection_list = []
		selection_list = mc.ls(sl=True)

		for item in selection_list:
			sel_item = QtWidgets.QListWidgetItem(self.lw_asset_selection)
			sel_item.setText(item)


class Build_ScreenshotTab( QtWidgets.QTabWidget ):
	'''Fills publish UI with an options tab widget

	@param parent:
	@param mSoftware:
	@param mDataDir:
	@param wButtonPosition:
	@param mAssetType:
	''' 
	
	def __init__( 
		self, 
		parent = None, 
		mDataDir = None, 
		wButtonPosition = None,
		mAssetType = None,
	):

		super( Build_ScreenshotTab, self ).__init__()
		
		self.data_dir = mDataDir
				
		self.software = os.getenv('SOFTWARE')
		self.icon_dir = os.getenv('ICONS_PATH').replace('\\', '/')

		self.setFixedHeight(250)
		
		self.create_gui()
		self.create_layout()
		self.create_connections()

	#------------------------------------------------------
	def create_gui(self):

		pixmap = QtGui.QPixmap(os.path.join(self.icon_dir, 'mb_AAM_default_screenshot.png'))
		self.px_screenshot = QtWidgets.QLabel(self)
		self.px_screenshot.setPixmap(pixmap)
		self.px_screenshot.fileName = pixmap
		self.btn_take_screenshot = QtWidgets.QPushButton("Take Screenshot")
		

	#------------------------------------------------------
	def create_layout(self):

		self.main_layout = QtWidgets.QVBoxLayout(self)
		self.main_layout.addWidget(self.px_screenshot)
		self.main_layout.addWidget(self.btn_take_screenshot)

		self.setLayout(self.main_layout)
		
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	def create_connections(self):
		
		self.btn_take_screenshot.clicked.connect(self.on_take_screenshot_pressed)

	#-----#-----#-----#-----#-----#-----#-----#-----#-----#
	def on_take_screenshot_pressed(self):
		'''Take screenshot button pressed 
		'''

		self.prep_user = "_temp_{0}".format( os.getenv( 'USER' ) )

		tv_item_json_data.take_screenshot(
			mDataDir = self.data_dir,
			mAssetName = self.prep_user
		)

		pixmap = os.path.join(self.data_dir, '{0}_image.png'.format(self.prep_user)).replace('\\', '/')
		self.px_screenshot.setPixmap(pixmap)
		self.px_screenshot.fileName = pixmap


#######################################################
class LineEdit_AssetName(LineEdit.Build_Sub):
	'''Line edit that will take user input. Extends my custom user input line edit
	
	:param widget parent: Parent object
	:param str mPlaceHolder: Text displayed before user input
	:param widget mGameNameWidget: Widget to send edited text to
	:param widget mCheckboxWidget: Widget to send edited text to
	'''

	# Signal vars
	enter_pressed = QtCore.Signal(str)
	enter_signal_str = "returnPressed"
	esc_pressed = QtCore.Signal(str)
	esc_signal_str = "escPressed" 

	def __init__(
		self, 
		parent = None,
		mGameNameWidget = None,
		mCheckboxWidget = None
	):
		super(LineEdit_AssetName, self).__init__(parent)
		
		val = 30

		self.game_name_widget = mGameNameWidget
		self.cb_asset_type = mCheckboxWidget

		self.create_connections()

	#-----------------------------------------------------------------------
	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key.Key_Control:
			pass
		elif event.key() == QtCore.Qt.Key.Key_Shift:
			pass
		if event.key() == QtCore.Qt.Key_Return:
			self.enter_pressed.emit( self.enter_signal_str )
			return True
		if event.key() == QtCore.Qt.Key_Escape:
			self.esc_pressed.emit( self.esc_signal_str )
			return True
		else:
			super(LineEdit_AssetName, self).keyPressEvent(event)


	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	def create_connections(self):
		'''Connections 
		'''
		self.enter_pressed.connect(self.clean_text)
		self.esc_pressed.connect(self.clean_text)
		self.editingFinished.connect(self.clean_text)


	#-----#-----#-----#-----#-----#-----#-----#-----#-----#
	def clean_text(self):
		# Clean name
		remove_digits = ''.join([i for i in self.text() if not i.isdigit()])
		#print remove_digits
		
		# CamelCase the words
		word_list = remove_digits.replace("_", ' ').replace("-", ' ').split()

		asset_name = []
		for word in word_list:
			asset_name.append('{0}{1}'.format(word[0].upper(), word[1:]))

		cleaned_name = ''.join(asset_name)

		# Remove non letters
		final_name = "".join(re.findall("[a-zA-Z]+", cleaned_name))

		# Set text in line edit
		self.setText(final_name)

		# Game engine asset name stuff
		self.game_name_widget.setText('{0}_{1}'.format(final_name, self.cb_asset_type.currentText().replace('UE4 ', '')))

		self.clearFocus()

	#-----------------------------------------------------------------------
	def focusOutEvent(self, event):
		#super(LineEdit_AssetName, self).focusOutEvent(event)
		
		self.clean_text()
