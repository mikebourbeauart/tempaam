css = '''
	QWidget{
		Background: #444444;
		color:rgb(232,232,232) ;
		font:12px bold;
		font-weight:bold;
		border-radius: 0px;
	}
	QLineEdit{
		background: #242424;
		color: #DADADA ;
		font:12px;
		border: none;
		height: 30px;
	}
	QTabWidget:pane{
		border: none;
	}

	QToolTip{
		color: rgb(200,200,200);
		background-color: rgb(20,20,20);
		border: 0px rgb(170,170,170);
	}

	QTabBar::tab::selected{
		Background: #2c998e;
		color: #E8E8E8;
		font-weight:bold;
	}
	QTabBar::tab::!selected{
		Background: #222222;
		color: #E8E8E8;
	}
	QTabBar::tab::hover{
		Background: #29C2B2;
		color: #FFFFFF;
		font-weight:bold;
	}

	QTreeView::indicator:unchecked{
		image: url("S:/_management/_mb_Pipeline/mb_Pipeline/mb_Pipeline/assets/icons/mb_MBP_unchecked.png");
	}
	QTreeView::indicator:checked{
		image: url("S:/_management/_mb_Pipeline/mb_Pipeline/mb_Pipeline/assets/icons/mb_MBP_checked.png");
	}
	QTreeView{
		alternate-background-color: #292929;
		background: #242424;
		color:rgb(218,218,218) ;
		font:12px;
		border: none;
		height: 200px;
	}
	QTreeView::item::hover{
		background: #29C2B2;
		color: #EDEDED;
		font-weight:bold;
	}
	QTreeView::item:selected{
		background-color: #2c998e;
		color:rgb(232,232,232)
	}
	QTreeView QHeaderView:section{
		background: #636363;
		font-weight:bold;
		height: 20px;
	}
	
	QScrollBar::handle{
		background-color: rgb(156, 156, 156);
	}
	QScrollBar::sub-page {
		background: rgb(94, 94, 94);
	}
	QScrollBar::add-page {
		background: rgb(94, 94, 94);
	}

	QPushButton{
		Background:#636363;
		height: 30px
	}
	QPushButton:hover{
		Background: #29C2B2;
	}
	QPushButton:hover:pressed{
		Background: #29C2B2;
	}
	QPushButton:pressed{
		Background:  #22A194;
	}

'''