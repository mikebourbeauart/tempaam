"""
Module for prep asset popup. 
"""


import os
import maya.cmds as mc

from Qt import QtCore
from Qt import QtWidgets

from aamCmds.treeView import get_tv_contents
from aamCmds.treeView import tv_item_json_data

import PrepPopupContents

from aamUI.StyleSheets import popup_window

class PrepPopup(QtWidgets.QWidget):
	'''Builds the PrepAssetPopup

	@param parent           str, 
	@param mSoftware:       str,  maya - houdini - nuke 
	@param mDataDir:        str,  directory of the data folder within the Publish folder
	@param wMainWindow:     str,  PublishTab's prepped_tv_view
	@param wButtonPosition: str,  PublishTab's prepped_tv_model 
	@param mAamIconDir:     str,  publish location 
	'''

	# Signal vars
	enter_pressed = QtCore.Signal(str)
	enter_signal_str = "returnPressed"
	esc_pressed = QtCore.Signal(str)
	esc_signal_str = "escPressed"
	
	def __init__( 
		self, 
		parent = None,
		mDataDir = None,
		wMainWindow = None, 
		wButtonPosition = None,
		mTaskTypes = None
	):
		super(PrepPopup, self).__init__()
		
		# Variables
		self.parent = parent
		self.data_dir = mDataDir
		self.main_window = wMainWindow
		self.button_pos = wButtonPosition	
		self.task_types = mTaskTypes

		self.ftrack_data = self.parent.ftrack_data

		self.setWindowFlags( QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
		self.setAttribute( QtCore.Qt.WA_DeleteOnClose )

		self.resize(300, 400)

		# Commands
		self.move_UI()
		self.create_gui() 
		self.create_layout()
		self.create_connections()

		self.setStyleSheet(popup_window.css)

		#self.le_comments.setFocus()
		
	#------------------------------------------------------
	def move_UI( self ):
		'''Moves the UI to window's edge'''

		# Get button position, get window position, get popup size,
		# move the window.
		btn_global_point = self.button_pos.mapToGlobal(self.button_pos.rect().topLeft())  
		win_global_point = self.parent.mapToGlobal(self.rect().topLeft()) 
		popup_size = self.mapToGlobal(self.rect().topRight())
		self.move(win_global_point.x()-popup_size.x()-8,btn_global_point.y())
		
	#------------------------------------------------------
	def create_gui( self ):
		tab_val = 60

		# Asset tab
		self.tw_asset = QtWidgets.QTabWidget( self )
		self.tw_asset.addTab(
			PrepPopupContents.Build_AssetTab(
				parent = self.parent,
				mTaskTypes = self.task_types
			),
			'Asset'
		)

		# Screenshot tab
		self.tw_screenshot = QtWidgets.QTabWidget( self )
		self.tw_screenshot.addTab(
			PrepPopupContents.Build_ScreenshotTab(
				parent = self.parent,
				mDataDir = self.data_dir,
			),
			'Screenshot'
		)

		self.btn_accept = QtWidgets.QPushButton("Accept")

		self.cancel_btn = QtWidgets.QPushButton("Cancel") 
	
	#------------------------------------------------------
	def create_layout( self ):
		self.button_layout = QtWidgets.QHBoxLayout()
		self.button_layout.addWidget( self.btn_accept ) 
		self.button_layout.addWidget( self.cancel_btn )

		self.main_layout = QtWidgets.QVBoxLayout( self )
		self.main_layout.addWidget( self.tw_asset )
		self.main_layout.addWidget( self.tw_screenshot )
		self.main_layout.addLayout( self.button_layout )
		self.main_layout.addStretch()

		self.setLayout( self.main_layout )
		
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	def create_connections( self ):
		'''Connections'''
		self.btn_accept.clicked.connect( self.on_accept_pressed )
		self.cancel_btn.clicked.connect( self.on_cancel_pressed )
		
		self.enter_pressed.connect( self.on_accept_pressed )
		self.esc_pressed.connect( self.on_cancel_pressed )
		
	#-----#-----#-----#-----#-----#-----#-----#-----#-----#    
	def on_accept_pressed( self ):
		'''Accept button pressed'''

		self.tw_asset.widget(0).le_asset_name.clean_text()

		# Vars
		self.asset_name = self.tw_asset.widget(0).le_asset_name.text()
		self.game_name = self.tw_asset.widget(0).le_asset_game_name.text()
		#if self.tw_asset.widget(0).le_asset_name.text() != None:
		self.game_data =  self.tw_asset.widget(0).le_asset_game_path.text()
		self.asset_type = self.tw_asset.widget(0).cb_asset_type.currentText()
		self.asset_sel = [i.text() for i in self.tw_asset.widget(0).lw_asset_selection.findItems("", QtCore.Qt.MatchContains)]
		self.asset_img = self.tw_screenshot.widget(0).px_screenshot.fileName
		
		# Make sure the user filled out all of the fields, otherwise prompt them to fill out all the fields
		if self.asset_name != '' and self.asset_type != 'None' and self.asset_sel != [] and self.asset_img != 'S:\_management\_mb_Pipeline\mb_AzureAssetManagement\mb_AzureAssetManagement/assets/icons/mb_AAM_default_screenshot.png' :
			
			self.prep_user = os.getenv("USER")

			# Rename temp image to asset name with version
			if "{0}/{1}_{2}_image.png".format( self.data_dir, self.asset_name, self.asset_type ):
				QtCore.QFile.remove(  "{0}/{1}_{2}_image.png".format( self.data_dir, self.asset_name, self.asset_type ) )
				self.init_file_name = "{0}/_temp_{1}_image.png".format( self.data_dir, self.prep_user )
				self.new_file_name = "{0}/{1}_{2}_image.png".format( self.data_dir, self.asset_name, self.asset_type )
				QtCore.QFile.rename( self.init_file_name, self.new_file_name )
			
			else:
				self.init_file_name = "{0}/_temp_{1}_image.png".format( self.data_dir, self.prep_user )
				self.new_file_name = "{0}/{1}_{2}_image.png".format( self.data_dir, self.asset_name, self.asset_type )
				QtCore.QFile.rename( self.init_file_name, self.new_file_name )

			# Write JSON data
			tv_item_json_data.write(
				mDataDir = self.data_dir,
				mAssetName = self.asset_name,
				mAssetType = self.asset_type,
				mAssetSel = self.asset_sel,
				mAssetImg = self.new_file_name,
				mPrepUser = self.prep_user,
				mGamePath = self.game_data,
				mGameName = self.game_name
			)
			
			get_tv_contents.get(
				mDataDir = self.data_dir,
				wView = self.parent.tv_prepped_view, 
				wModel = self.parent.tv_prepped_model, 
				wLineEdit = self.main_window.le_address_bar
			)

			self.close()
		
			self.parent.cbox_filter.clear()
			self.parent.cbox_filter.addItems(self.parent.update_filter_list())
			self.parent.cbox_filter.setCurrentIndex(0)

		else:
			print '// You need to add data!'

	#-----#-----#-----#-----#-----#-----#-----#-----#-----#
	def on_cancel_pressed( self ):
		'''Cancel button pressed 
		'''

		self.close() 
		