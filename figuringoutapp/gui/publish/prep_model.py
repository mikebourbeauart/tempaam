"""
Module for view's model 
"""


from Qt import QtCore
from Qt import QtGui


#######################################################
class Build(QtGui.QStandardItemModel):
	''' Model for tree view '''
	#-----------------------------------------------------------------------
	def __init__(self, parent=None):
		super(Build, self).__init__(parent)

		#self.header_labels = ["Prepped Asset","Type", "Latest"]

		# Instead of an info area, a the tooltip will show the relevant comments and stuff
		#self.setHorizontalHeaderLabels(self.header_labels)

	def flags(self, index):
		flag = QtCore.Qt.ItemIsEnabled
		if index.isValid():
			flag |= QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable 
		return flag
		


