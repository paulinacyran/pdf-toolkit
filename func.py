from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyPDF2 import PdfMerger, PdfFileReader, PdfFileWriter
import os

class Merger():

	def open_files(self):
		# Specify the files types
		files_types = 'All Files(*);; PDF Files (*.pdf)'
		# Open dialog box
		self.files_paths = QFileDialog.getOpenFileNames(
			filter=files_types,
			initialFilter='PDF Files (*.pdf)'
			)
		# Verify that the correct format files was selected
		error_message = []
		for i in range(len(self.files_paths[0])):
			if self.files_paths[0][i][-4:] != '.pdf':
				error_message.append('error')
		if len(error_message) != 0:
			# Show information about incorrect file format in statusbar
			self.statusbar.showMessage(f'Incorrect file format selected. Choose again.')
		else:
			# Show selected files in statusbar
			self.statusbar.showMessage(f'Selected files: {self.files_paths[0]}')
			# Set the 'select_location_button' 'select_location_label' enabled
			self.select_location_button.setEnabled(True)
			self.select_location_label.setEnabled(True)

	def select_location(self):
		# Open dialog box
		self.new_file_path = QFileDialog.getExistingDirectory()
		# Show selected directory in statusbar
		self.statusbar.showMessage(f'Selected directory: {self.new_file_path}')
		# Set the 'enter_name label','enter_name_button' and 'enter_name_label' enabled
		self.enter_name_text_browser.setEnabled(True)
		self.enter_name_button.setEnabled(True)
		self.enter_name_label.setEnabled(True)

	def select_name(self):
		# Set the new file name
		text_content = self.enter_name_text_browser.toPlainText()
		if text_content[-4:].lower() == ".pdf":
			text_content = text_content[:-4]
		self.new_file_name = f'{text_content}.pdf'
		# Verify that the new file name is correct
		if text_content == "":
			# Show message in statusbar
			self.statusbar.showMessage(f'Invalid file name. Enter the file name again.')
		else:
			# Show message in statusbar
			self.statusbar.showMessage(f'Selected name of the new file: {self.new_file_name}. Press Merge Button to merge your files.')
			# Set the 'merge_button' enabled
			self.merge_button.setEnabled(True)

	def merge_files(self):
		try:
			# Merge PDFs
			merger = PdfMerger()
			for path in self.files_paths[0]:
				merger.append(path)
			# Write out the new PDF file
			new_file = os.path.join(self.new_file_path, self.new_file_name)
			merger.write(new_file)
			merger.close()
			# Show message in statusbar
			self.statusbar.showMessage(f'New PDF created: {self.new_file_name} in {self.new_file_path}')
		except:
			# Show message in statusbar
			self.statusbar.showMessage(f'Something went wrong. Try again.')


class Splitter():

	def open_file(self):
		# Specify the file type
		file_type = 'All Files(*);; PDF Files (*.pdf)'
		# Open dialog box
		self.file_path = QFileDialog.getOpenFileName(
			filter=file_type,
			initialFilter='PDF Files (*.pdf)'
			)
		# Verify that the correct format file was selected
		if self.file_path[0][-4:] != '.pdf':
			# Show information about incorrect file format in statusbar
			self.statusbar.showMessage(f'Incorrect file format selected. Choose again.')
		else:
			# Show selected file in statusbar
			self.statusbar.showMessage(f'Selected file: {self.file_path[0]}')
			# Set the 'select_location_button' and 'select_location_label' enabled
			self.select_location_button.setEnabled(True)	
			self.select_location_label.setEnabled(True)

	def select_location(self):
		# Open dialog box
		self.new_files_path = QFileDialog.getExistingDirectory()
		# Show selected directory in statusbar
		self.statusbar.showMessage(f'Selected directory: {self.new_files_path}. Press Split Button to split your file.')
		# Set the 'split_button' and 'select_location_label' enabled
		self.split_button.setEnabled(True)
		

	def split_file(self):
		try:
			# Split PDF
			input_pdf_name = os.path.basename(self.file_path[0])[:-4]
			pdf_reader = PdfFileReader(self.file_path[0])
			output_pdf_names = []
			for page in range(pdf_reader.getNumPages()):
				pdf_writer = PdfFileWriter()
				pdf_writer.addPage(pdf_reader.getPage(page))
				output_pdf_name = f'{input_pdf_name}_{page+1}.pdf'
				# Write out the new PDF
				new_file = os.path.join(self.new_files_path, output_pdf_name)
				pdf_writer.write(new_file)
				output_pdf_names.append(output_pdf_name)
			# Show message in statusbar
			self.statusbar.showMessage(f'New PDFs created: {output_pdf_names} in {self.new_files_path}')
		except:
			# Show message in statusbar
			self.statusbar.showMessage(f'Something went wrong. Try again.')


class Rotator():

	def open_file(self):
		# Specify the file type
		file_type = 'All Files(*);; PDF Files (*.pdf)'
		# Open dialog box
		self.file_path = QFileDialog.getOpenFileName(
			filter=file_type,
			initialFilter='PDF Files (*.pdf)'
			)
		# Verify that the correct format file was selected
		if self.file_path[0][-4:] != '.pdf':
			# Show information about incorrect file format in statusbar
			self.statusbar.showMessage(f'Incorrect file format selected. Choose again.')
		else:
			# Show selected file in statusbar
			self.statusbar.showMessage(f'Selected file: {self.file_path[0]}')
			# Set the 'select_location_button' and 'select_location_label' enabled
			self.select_location_button.setEnabled(True)	
			self.select_location_label.setEnabled(True)


	def select_location(self):
		# Open dialog box
		self.new_file_path = QFileDialog.getExistingDirectory()
		# Show selected directory in statusbar
		self.statusbar.showMessage(f'Selected directory: {self.new_file_path}.')
		# Set the 'select_angle_label', 'rename_label' and radio buttons  enabled
		self.select_angle_label.setEnabled(True)
		self.rename_label.setEnabled(True)
		self.radioButton_90.setEnabled(True)
		self.radioButton_180.setEnabled(True)
		self.radioButton_270.setEnabled(True)
		self.radioButton_yes.setEnabled(True)
		self.radioButton_no.setEnabled(True)

	def degree_button_state(self, radioButton):
		if radioButton.isChecked():
			self.degree = radioButton.text()


	def select_name_enable(self):
		if self.radioButton_yes.isChecked():
			# Set the 'enter_name label','enter_name_button' and 'enter_name_label' enabled
			self.enter_name_text_browser.setEnabled(True)
			self.enter_name_button.setEnabled(True)
			self.enter_name_label.setEnabled(True)
			# Set the 'rotate_button' disabled
			self.rotate_button.setEnabled(False)


	def select_name_disable(self):
		if self.radioButton_no.isChecked():
			# Set the 'enter_name label','enter_name_button' and 'enter_name_label' enabled
			self.enter_name_text_browser.setEnabled(False)
			self.enter_name_button.setEnabled(False)
			self.enter_name_label.setEnabled(False)
			# Set the 'rotate_button' enabled
			self.rotate_button.setEnabled(True)
			# Set the new file name
			self.new_file_name = os.path.basename(self.file_path[0])


	def select_name(self):
		# Set the new file name
		text_content = self.enter_name_text_browser.toPlainText()
		if text_content[-4:].lower() == ".pdf":
			text_content = text_content[:-4]
		self.new_file_name = f'{text_content}.pdf'
		# Verify that the new file name is correct
		if text_content == "":
			# Show message in statusbar
			self.statusbar.showMessage(f'Invalid file name. Enter the file name again.')
		else:
			# Show message in statusbar
			self.statusbar.showMessage(f'Selected name of the new file: {self.new_file_name}. Press Rotate Button to rotate your file.')
			# Set the 'rotate_button' enabled
			self.rotate_button.setEnabled(True)


	def rotate_file(self):
		try:
			# Rotate PDF
			input_pdf_name = os.path.basename(self.file_path[0])[:-4]
			pdf_reader = PdfFileReader(self.file_path[0])
			pdf_writer = PdfFileWriter()
			for page in range(pdf_reader.getNumPages()):
				page_r = pdf_reader.getPage(page)
				page_r.rotateClockwise(int(self.degree))
				pdf_writer.addPage(page_r)
				# Write out the new PDF
				new_file = os.path.join(self.new_file_path, self.new_file_name)
				pdf_writer.write(new_file)
			# Show message in statusbar
			self.statusbar.showMessage(f'New PDFs created: {self.new_file_name} in {self.new_file_path}')
			# Set the 'rotate_button' disabled
			self.rotate_button.setEnabled(False)
			# Uncheck radiobuttons
			self.radioButton_yes.setAutoExclusive(False)
			self.radioButton_yes.setChecked(False)
			self.radioButton_yes.setAutoExclusive(True)
			self.radioButton_no.setAutoExclusive(False)
			self.radioButton_no.setChecked(False)
			self.radioButton_no.setAutoExclusive(True)
		except:
			# Show message in statusbar
			self.statusbar.showMessage(f'Something went wrong. Try again.')


