import sys
from PyQt5.QtWidgets import *

class TabDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Widget")
        self.setFixedSize(640, 200)

        # Inisialisasi tab
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabs.addTab(self.tab1, "Contact Details")
        self.tabs.addTab(self.tab2, "Personal Details")
        self.tabs.addTab(self.tab3, "Education Details")

        # Setup tiap tab
        self.create_tab1()
        self.create_tab2()
        self.create_tab3()

        # Layout utama
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

    def create_tab1(self):
        layout = QFormLayout()
        self.name_input = QLineEdit()
        self.address_input = QLineEdit()

        layout.addRow(QLabel("Name"), self.name_input)
        layout.addRow(QLabel("Address"), self.address_input)

        self.tab1.setLayout(layout)

    def create_tab2(self):
        layout = QFormLayout()

        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")

        sex_layout = QHBoxLayout()
        sex_layout.addWidget(self.male_radio)
        sex_layout.addWidget(self.female_radio)

        self.dob_input = QLineEdit()

        layout.addRow(QLabel("Sex"), sex_layout)
        layout.addRow(QLabel("Date of Birth"), self.dob_input)

        self.tab2.setLayout(layout)

    def create_tab3(self):
        layout = QHBoxLayout()
        label = QLabel("subjects")
        self.physics_checkbox = QCheckBox("Physics")
        self.maths_checkbox = QCheckBox("Maths")

        layout.addWidget(label)
        layout.addWidget(self.physics_checkbox)
        layout.addWidget(self.maths_checkbox)

        self.tab3.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = TabDemo()
    demo.show()
    sys.exit(app.exec_())
