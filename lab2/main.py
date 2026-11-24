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

        self.combo = QComboBox()
        self.combo.addItems(["Ч/б", "Размытие", "Яркость"])
        self.label = QLabel(self.combo.currentText())
        self.combo.currentIndexChanged.connect(self.on_combo_select)

        layout.addWidget(self.combo)
        layout.addWidget(self.label)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_combo_select(self, index):
        """Отображает выбранный фильтр."""
        self.label.setText(self.combo.itemText(index))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
