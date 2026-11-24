import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLabel, QComboBox
)


class MainWindow(QMainWindow):
    """Главное окно приложения."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Выбор фильтра")
        self.setGeometry(100, 100, 400, 200)
        self.init_ui()

    def init_ui(self):
        """Инициализация пользовательского интерфейса."""
        central_widget = QWidget()
        layout = QVBoxLayout()

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
