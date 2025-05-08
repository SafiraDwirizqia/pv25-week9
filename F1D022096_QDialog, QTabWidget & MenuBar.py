import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 9 - QDialog, QTabWidget & MenuBar")
        self.setFixedSize(840, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.menu_bar = self.menuBar()
        self.setup_menu()

        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabBar::tab:selected {
                background: #0078d7;
                color: white;
                font-weight: bold;
            }
            QTabBar::tab {
                padding: 10px;
                min-width: 120px;
            }
        """)

        self.input_tab = QWidget()
        self.font_tab = QWidget()
        self.file_tab = QWidget()

        self.tabs.addTab(self.input_tab, "Input Nama")
        self.tabs.addTab(self.font_tab, "Pilih Font")
        self.tabs.addTab(self.file_tab, "Buka File")

        self.setup_input_tab()
        self.setup_font_tab()
        self.setup_file_tab()

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.central_widget.setLayout(layout)

    def setup_menu(self):
        file_menu = self.menu_bar.addMenu("File")
        fitur_menu = self.menu_bar.addMenu("Fitur")

        keluar_action = QAction("Keluar", self)
        keluar_action.triggered.connect(self.close)
        file_menu.addAction(keluar_action)

        input_nama_action = QAction("Input Nama", self)
        input_nama_action.triggered.connect(lambda: self.tabs.setCurrentWidget(self.input_tab))
        pilih_font_action = QAction("Pilih Font", self)
        pilih_font_action.triggered.connect(lambda: self.tabs.setCurrentWidget(self.font_tab))
        buka_file_action = QAction("Buka File", self)
        buka_file_action.triggered.connect(lambda: self.tabs.setCurrentWidget(self.file_tab))

        fitur_menu.addAction(input_nama_action)
        fitur_menu.addAction(pilih_font_action)
        fitur_menu.addAction(buka_file_action)

    def setup_input_tab(self):
        layout = QVBoxLayout()
        self.btn_input_nama = QPushButton("Input Nama")
        self.btn_input_nama.clicked.connect(self.input_nama)
        self.output_line = QLineEdit()
        self.output_label = QLabel("Nama:")

        layout.addWidget(self.btn_input_nama)
        layout.addWidget(self.output_line)
        layout.addWidget(self.output_label)
        self.input_tab.setLayout(layout)

    def setup_font_tab(self):
        layout = QVBoxLayout()
        self.btn_pilih_font = QPushButton("Pilih Font")
        self.btn_pilih_font.clicked.connect(self.pilih_font)
        self.font_line = QLineEdit("")
        self.font_line.setReadOnly(True)

        layout.addWidget(self.btn_pilih_font)
        layout.addWidget(self.font_line)
        self.font_tab.setLayout(layout)

    def setup_file_tab(self):
        layout = QVBoxLayout()
        self.btn_buka_file = QPushButton("Buka File .txt")
        self.btn_buka_file.clicked.connect(self.buka_file)
        self.file_display = QTextEdit()
        self.file_display.setReadOnly(True)

        layout.addWidget(self.btn_buka_file)
        layout.addWidget(self.file_display)
        self.file_tab.setLayout(layout)

    def input_nama(self):
        nama = self.output_line.text().strip()
        if nama:
            self.output_line.clear()
            self.output_label.setText(f"Nama: {nama}")
        else:
            QMessageBox.warning(self, "Peringatan", "Silakan masukkan nama terlebih dahulu.")

    def pilih_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.font_line.setFont(font)
            self.font_line.setText(f"{font.family()}, {font.pointSize()}pt")

    def buka_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if file_name:
            try:
                with open(file_name, 'r') as file:
                    self.file_display.setText(file.read())
            except Exception as e:
                self.file_display.setText(f"Error: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
