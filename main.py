import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class myForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.rollPrice.textChanged.connect(self.roll_counter)
        self.ui.rollSpin.textChanged.connect(self.roll_counter)
        self.ui.nutPrice.textChanged.connect(self.nut_counter)
        self.ui.nuttSpin.textChanged.connect(self.nut_counter)
        self.show()

    def roll_counter(self):
        price = self.ui.rollPrice.text()
        count = self.ui.rollSpin.value()
        try:
            price = float(price)
            self.ui.rollTotalPrice.setText(f'{price * count:.2f}zł')
        except ValueError:
            self.ui.rollPrice.setText('')

    def nut_counter(self):
        price = self.ui.nutPrice.text()
        count = self.ui.nuttSpin.value()
        try:
            price = float(price)
            self.ui.nutTotalPrice.setText(f'{price * count:.2f}zł')
        except ValueError:
            self.ui.nutPrice.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myForm()
    sys.exit(app.exec())