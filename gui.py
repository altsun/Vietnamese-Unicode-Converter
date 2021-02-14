# Import
import os
import sys

# PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import main



# Class ConverterGui
class ConverterGui(QDialog):

    def __init__(self):
        # Initialize QDialog
        QDialog.__init__(self)

        # Default parameters
        self.width = 300
        self.height = 200
        self.margin = 20

        # Parameters
        self.clipboard = QGuiApplication.clipboard()

        # Create layout
        layout = QGridLayout()

        # Create and set elements
        ## Input string
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText('Nhập chuỗi')
        ## Button convert
        self.button_convert = QPushButton('Chuyển đổi')
        ## Output string
        self.text_output = QTextEdit()
        ## Button copy to clipboard
        self.button_copy = QPushButton('Sao chép')

        # Prepare elements
            # Set output_string to read-only
        self.text_output.setReadOnly(True)

        # Add elements to layout
        layout.addWidget(self.text_input, 0, 0)
        layout.addWidget(self.button_convert, 1, 0)
        layout.addWidget(self.text_output, 2, 0)
        layout.addWidget(self.button_copy, 3, 0)

        # Set layout
        self.setLayout(layout)

        # Initialize UI
        self.init_ui()

        # Handle events
        self.button_convert.clicked.connect(self.convert)
        self.button_copy.clicked.connect(self.copy_clipboard)
        self.button_copy.clicked.connect(self.set_copied_message)


    # Front-end functions
    def init_ui(self):
        # Set window title
        self.setWindowTitle('Vietnamese Unicode Converter')

        # Set window size
        self.setGeometry(50, 50, self.width, self.height)

        # Set window at center
        self.center()

        # Remove default focus
        self.setFocus()

        # Show window
        self.show()


    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())


    # Back-end functions
    def convert(self):
        input_string = self.text_input.toPlainText()
        self.output_string = main.converter(input_string)
        self.text_output.setText(self.output_string)

    def copy_clipboard(self):
        if self.output_string:
            self.clipboard.setText(self.output_string)
    
    def set_copied_message(self):
        msg_box = QMessageBox()
        msg_box.information(self, 'Copied', 'Copied: ' + self.text_output.toPlainText())


# Run Gui
app = QApplication(sys.argv)
converter_gui = ConverterGui()
app.exec_()