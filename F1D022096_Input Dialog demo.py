import sys
from PyQt5.QtWidgets import *


class InputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog demo")
        self.setFixedSize(640, 200)

        # Komponen UI
        self.list_button = QPushButton("Choose from list")
        self.name_button = QPushButton("get name")
        self.int_button = QPushButton("Enter an integer")

        self.list_output = QLineEdit()
        self.name_output = QLineEdit()
        self.int_output = QLineEdit()

        # Layout horizontal untuk tiap baris
        row1 = QHBoxLayout()
        row1.addWidget(self.list_button)
        row1.addWidget(self.list_output)

        row2 = QHBoxLayout()
        row2.addWidget(self.name_button)
        row2.addWidget(self.name_output)

        row3 = QHBoxLayout()
        row3.addWidget(self.int_button)
        row3.addWidget(self.int_output)

        # Layout vertikal utama
        main_layout = QVBoxLayout()
        main_layout.addLayout(row1)
        main_layout.addLayout(row2)
        main_layout.addLayout(row3)

        self.setLayout(main_layout)

        # Koneksi aksi tombol
        self.list_button.clicked.connect(self.show_list_dialog)
        self.name_button.clicked.connect(self.show_text_dialog)
        self.int_button.clicked.connect(self.show_int_dialog)

    def show_list_dialog(self):
        items = ("C", "C++", "Java", "Python")
        item, ok = QInputDialog.getItem(self, "select input dialog", "list of languages", items, 0, False)
        if ok and item:
            self.list_output.setText(item)

    def show_text_dialog(self):
        text, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your name:")
        if ok and text:
            self.name_output.setText(text)

    def show_int_dialog(self):
        number, ok = QInputDialog.getInt(self, "integer input dualog", "enter a number")
        if ok:
            self.int_output.setText(str(number))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputDialogDemo()
    window.show()
    sys.exit(app.exec_())
