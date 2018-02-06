"""
Module for options tab within publish tab
"""


from Qt import QtWidgets
from Qt	import QtCore

import options_tab

class OptionsTabWidget(QtWidgets.QTabWidget):
	''' 
	Fills selection info tab with an options tab widget

	''' 
	
	def __init__(self):
		super(OptionsTabWidget, self).__init__()

		self.setMinimumHeight(120)
		self.setMaximumHeight(300)
		
		self.create_gui()
		self.create_layout()


	#------------------------------------------------------
	def create_gui( self ):
		self.addTab(options_tab.OptionsTab(), "Options")
		pass

	#------------------------------------------------------
	def create_layout( self ):

		self.main_layout = QtWidgets.QVBoxLayout( self )
		#self.main_layout.addWidget( self.option_tab_contents )

				
		self.setLayout( self.main_layout )
		
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	def create_connections( self ):
		
		pass

