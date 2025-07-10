from PySide6.QtWidgets import QApplication
from ui.ui import KanaMail

def main():
    app = QApplication([])
    window = KanaMail()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()