"""
Module for the main view
"""


from Qt import QtCore
from Qt import QtWidgets

#######################################################
class Build(QtWidgets.QTreeView):
	'''Create the tree view widget where files are displayed 
	'''

	def __init__(self, parent=None):
		super(Build, self).__init__(parent)
		
		self.setModel(parent.tv_prepped_model)
		self.setIndentation(0)
		self.setFocusPolicy(QtCore.Qt.NoFocus)  
		self.setAlternatingRowColors(True)
		self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
		self.setUniformRowHeights(True)
		
		# Sizing
		self.setMinimumHeight(300)
		self.setMinimumWidth(500)
		self.index_1_col_width = 300
		self.index_2_col_width = 70
		self.setColumnWidth(0, self.index_1_col_width) # Name
		self.setColumnWidth(1, self.index_2_col_width) # Type

		self.delegate = MyDelegate()
		self.setItemDelegate(self.delegate)
		self.setIconSize( QtCore.QSize(15, 15) )

	#---------------------------------------------------------------------------
	def setModel(self, model):

		super(Build, self).setModel(model)

		self.selection_model = self.selectionModel()

		#self.selection_model.selectionChanged.connect(self.store_current_selection)

		""" moved to another module
		self.connect(self.selectionModel(),  
					 QtCore.SIGNAL("selectionChanged(QItemSelection, QItemSelection)"),  
					 self.store_current_selection ) 
		"""
	'''
	#---------------------------------------------------------------------------
	def store_current_selection(self, newSelection, oldSelection):
		
		indexes_new = newSelection.indexes()
		indexes_old = oldSelection.indexes()

		if indexes_new:
			if indexes_new[1]:
				print 'index new data = {0}'.format( indexes_new[1].data() )
			print('row: %d' % indexes_new[1].row())


		if indexes_old:
			print '______________________________changed'
			print 'index old data = {0}'.format( indexes_old[1].data() )
			print('row: %d' % indexes_old[1].row())

			active_tabs = self.tw_options.count()

			if active_tabs != 0:
				for tab_index in range(active_tabs):
					self.tw_options.removeTab(tab_index)

		#index = self.tv_file_list.selectedIndexes()[0]
		#item = self.tv_model.itemFromIndex(index).text()

	'''

class MyDelegate(QtWidgets.QStyledItemDelegate):
	'''Edit row display settings'''
	def sizeHint(self, option, index):
		size = super(MyDelegate, self).sizeHint(option, index)
		size.setHeight(20)
		return QtCore.QSize(20, 20)
