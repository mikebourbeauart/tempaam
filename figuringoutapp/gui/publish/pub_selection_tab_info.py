"""
Module for options tab within publish tab
"""


from Qt import QtWidgets
from Qt	import QtCore

class Build(QtWidgets.QTabWidget):
	''' 
	Fills selection info tab with an options tab widget
	''' 
	
	def __init__(self):
		super( Build, self ).__init__()

		self.setMaximumWidth(10)

		self.create_gui()
		self.create_layout()


	#------------------------------------------------------
	def create_gui( self ):
		pass
		#self.option_tab_contents = pub_options_tab_contents.Fill( mAssetType = self.asset_type)

	#------------------------------------------------------
	def create_layout( self ):

		self.main_layout = QtWidgets.QVBoxLayout( self )
		#self.main_layout.addWidget( self.option_tab_contents )

				
		self.setLayout( self.main_layout )
		
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	def create_connections( self ):
		
		pass