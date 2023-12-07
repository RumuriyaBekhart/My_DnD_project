from character import Character
from create_db import create_db
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    create_db()
    app = QApplication(sys.argv)
    ex = Character()
    ex.show()
    sys.exit(app.exec())
