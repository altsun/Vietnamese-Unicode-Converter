import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import main


class ConverterGui(QDialog):

    def __init__(self):
        # Initialize QDialog
        QDialog.__init__(self)

        # Default parameters
        self.width = 300
        self.height = 200
        self.margin = 20

        # Parameters
        self.output_string = ''
        self.clipboard = QGuiApplication.clipboard()

        # Create layout
        layout = QGridLayout()

        # Create and set elements
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText('Enter text here...')
        self.button_convert = QPushButton('Convert')
        self.text_output = QTextEdit()
        self.button_copy = QPushButton('Copy')

        self.text_output.setReadOnly(True)

        layout.addWidget(self.text_input, 0, 0)
        layout.addWidget(self.button_convert, 1, 0)
        layout.addWidget(self.text_output, 2, 0)
        layout.addWidget(self.button_copy, 3, 0)

        self.setLayout(layout)

        self.init_ui()

        # Add event handlers
        self.button_convert.clicked.connect(self.convert)
        self.button_copy.clicked.connect(self.copy_clipboard)
        self.button_copy.clicked.connect(self.show_copy_message)

    def init_ui(self):
        self.setWindowTitle('Vietnamese Unicode Converter')
        self.setGeometry(50, 50, self.width, self.height)  # Set window size
        self.center()  # Set window at center
        self.setFocus()  # Remove default focus
        self.show()  # Show window

    def center(self):
        qr = self.frameGeometry()  # geometry of the main window
        screen_center_point = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(screen_center_point)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def convert(self):
        input_string = self.text_input.toPlainText()
        self.output_string = main.convert(input_string)
        self.text_output.setText(self.output_string)

    def copy_clipboard(self):
        if self.output_string:
            self.clipboard.setText(self.output_string)

    def show_copy_message(self):
        msg_box = QMessageBox()
        msg_box.information(self, 'Copy', 'Copy done!')


# Run Gui
app = QApplication(sys.argv)
converter_gui = ConverterGui()
app.exec_()
