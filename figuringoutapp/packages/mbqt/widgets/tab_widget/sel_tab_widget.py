"""
Module for options tab within publish tab
"""


from Qt import QtWidgets
from Qt	import QtCore


class SelTabWidget(QtWidgets.QTabWidget):
	''' 
	Fills selection info tab with an options tab widget

	''' 
	
	def __init__(self):
		super( SelTabWidget, self ).__init__()


		self.setMinimumWidth(200)
		self.setMaximumWidth(200)

		self.create_gui()
		self.create_layout()



	#------------------------------------------------------
	def create_gui( self ):

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

