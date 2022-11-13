from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5 import uic
from func import Merger, Splitter, Rotator
import sys


class OpenWindow():
	def open_MainWindow(self):
		main_window = Ui_MainWindow()
		widget.addWidget(main_window)
		widget.setCurrentIndex(widget.currentIndex()+1)	

	def open_MergerWindow(self):
		merger_window = Ui_MergerWindow()
		widget.addWidget(merger_window)
		widget.setCurrentIndex(widget.currentIndex()+1)

	def open_SplitterWindow(self):
		splitter_window = Ui_SplitterWindow()
		widget.addWidget(splitter_window)
		widget.setCurrentIndex(widget.currentIndex()+1)

	def open_RotatorWindow(self):
		rotator_window = Ui_RotatorWindow()
		widget.addWidget(rotator_window)
		widget.setCurrentIndex(widget.currentIndex()+1)


class Ui_MainWindow(QMainWindow, OpenWindow):
	def __init__(self):
		super(Ui_MainWindow, self).__init__()

		# Load the ui file
		uic.loadUi('main.ui', self) 

		# -------- Push buttons settings --------
		# Add the 'open_MergerWindow' function to the 'merge_push_button'
		self.merge_push_button.clicked.connect(self.open_MergerWindow)

		# Add the 'open_SplitterWindow' function to the 'split_push_button'
		self.split_push_button.clicked.connect(self.open_SplitterWindow)

		# # Add the 'open_RotatorWindow' function to the 'rotate_push_button'
		self.rotate_push_button.clicked.connect(self.open_RotatorWindow)

		# -------- QAction widgets settings --------
		# Set the 'Home' QAction widget disabled
		self.actionMenu.setEnabled(False)

		# Add the 'open_MergerWindow' function to the 'Merge_PDF' QAction widget
		self.actionMerge_PDF.triggered.connect(self.open_MergerWindow)

		# Add the 'open_SplitterWindow' function to the 'Split_PDF' QAction widget
		self.actionSplit_PDF.triggered.connect(self.open_SplitterWindow)

		# Add the 'open_RotatorWindow' function to the 'Rotate_PDF' QAction widget
		self.actionRotate_PDF.triggered.connect(self.open_RotatorWindow)


class Ui_MergerWindow(QMainWindow, OpenWindow, Merger):
	def __init__(self):
		super(Ui_MergerWindow, self).__init__()

		# Load the ui file
		uic.loadUi('merger.ui', self)

		# -------- App widgets settings --------
		# Add the 'open_files' function to the 'select_files_button'
		self.select_files_button.clicked.connect(self.open_files)

		# Add the 'select_location' function to the 'select_location_button'
		self.select_location_button.clicked.connect(self.select_location)

		# Add the 'select_name' function to the 'enter_name_button'
		self.enter_name_button.clicked.connect(self.select_name)

		# Add the 'merge_files' function to the 'merge_button'
		self.merge_button.clicked.connect(self.merge_files)

		# -------- QAction widgets settings --------
		# Set the 'Merge PDF' QAction widget disabled
		self.actionMerge_PDF.setEnabled(False)

		# Add the 'open_Main' function to the 'Home' QAction widget
		self.actionMenu.triggered.connect(self.open_MainWindow)

		# Add the 'open_SplitterWindow' function to the 'Split_PDF' QAction widget
		self.actionSplit_PDF.triggered.connect(self.open_SplitterWindow)

		# Add the 'open_RotatorWindow' function to the 'Rotate_PDF' QAction widget
		self.actionRotate_PDF.triggered.connect(self.open_RotatorWindow)


class Ui_SplitterWindow(QMainWindow, OpenWindow, Splitter):
	def __init__(self):
		super(Ui_SplitterWindow, self).__init__()

		# Load the ui file
		uic.loadUi('splitter.ui', self)

		# -------- App widgets settings --------
		# Add the 'open_file' function to the 'select_file_button'
		self.select_file_button.clicked.connect(self.open_file)

		# Add the 'select_location' function to the 'select_location_button'
		self.select_location_button.clicked.connect(self.select_location)

		# Add the 'split_file' function to the 'split_button'
		self.split_button.clicked.connect(self.split_file)

		# -------- QAction widgets settings --------
		# Set the 'Split PDF' QAction widget disabled
		self.actionSplit_PDF.setEnabled(False)

		# Add the 'open_Main' function to the 'Home' QAction widget
		self.actionMenu.triggered.connect(self.open_MainWindow)

		# Add the 'open_MergerWindow' function to the 'Merge_PDF' QAction widget
		self.actionMerge_PDF.triggered.connect(self.open_MergerWindow)

		# Add the 'open_RotatorWindow' function to the 'Rotate_PDF' QAction widget
		self.actionRotate_PDF.triggered.connect(self.open_RotatorWindow)


class Ui_RotatorWindow(QMainWindow, OpenWindow, Rotator):
	def __init__(self):
		super(Ui_RotatorWindow, self).__init__()

		# Load the ui file
		uic.loadUi('rotator.ui', self)

		# -------- App widgets settings --------
		# Add the 'open_file' function to the 'select_file_button'
		self.select_file_button.clicked.connect(self.open_file)

		# Add the 'select_location' function to the 'select_location_button'
		self.select_location_button.clicked.connect(self.select_location)

		# Add the 'degree_button_state' function to the 'radioButton_90', 'radioButton_180' and 'radioButton_270'
		self.radioButton_90.toggled.connect(lambda: self.degree_button_state(self.radioButton_90))
		self.radioButton_180.toggled.connect(lambda: self.degree_button_state(self.radioButton_180))
		self.radioButton_270.toggled.connect(lambda: self.degree_button_state(self.radioButton_270))

		# Add the 'select_name_enable' function to the 'radioButton_yes'
		self.radioButton_yes.toggled.connect(self.select_name_enable)

		# Add the 'select_name_disable' function to the 'radioButton_no'
		self.radioButton_no.toggled.connect(self.select_name_disable)

		# Add the 'select_name' function to the 'enter_name_button'
		self.enter_name_button.clicked.connect(self.select_name)

		# Add the 'rotate_file' function to the 'rotate_button'
		self.rotate_button.clicked.connect(self.rotate_file)

		# -------- QAction widgets settings --------
		# Set the 'Rotate PDF' QAction widget disabled
		self.actionRotate_PDF.setEnabled(False)

		# Add the 'open_Main' function to the 'Home' QAction widget
		self.actionMenu.triggered.connect(self.open_MainWindow)

		# Add the 'open_MergerWindow' function to the 'Merge_PDF' QAction widget
		self.actionMerge_PDF.triggered.connect(self.open_MergerWindow)

		# Add the 'open_SplitterWindow' function to the 'Split_PDF' QAction widget
		self.actionSplit_PDF.triggered.connect(self.open_SplitterWindow)


# Initialize the app
app = QApplication(sys.argv)
main_window = Ui_MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_window)
widget.setMinimumWidth(701)
widget.setMinimumHeight(620)
widget.show()
app.exec_()