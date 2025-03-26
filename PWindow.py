from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import (QDialog, QProgressBar, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit,
                               QListWidgetItem)
from UI import Ui_Dialog


class MyView(QDialog):
    def __init__(self):
        super().__init__()

        # Inicjalizacja interfejsu
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Okno postępu
        self.progress_window = QWidget()
        self.progressBar = QProgressBar()
        self.label = QLabel()  # bez rodzica, trafi do progress_window

        # Layout progress window
        self.progress_layout = QVBoxLayout()
        self.progress_layout.addWidget(self.progressBar)
        self.progress_layout.addWidget(self.label)
        self.progress_window.setLayout(self.progress_layout)
        self.progress_window.setWindowTitle("Training Progress")
        self.progress_window.resize(300, 100)

        # Główne okno
        self.resize(800, 600)

    def set_train_file_path_label(self, file_path):
        self.ui.label_3.setText(f"Train file selected: {file_path}")

    def set_test_file_path_label(self, file_path: str):
        self.ui.label_4.setText(f"Test file selected: {file_path}")

    def enable_trainer_creation(self):
        self.ui.btn_create_trainer.setEnabled(True)

    def enable_test_train(self):
        self.ui.btn_trainer_test.setEnabled(True)
        self.ui.btn_trainer_train.setEnabled(True)

    def set_trainer_label(self, text):
        self.ui.label_5.setText(f"{text}")

    def get_learning_rate(self):
        return self.ui.lineEdit_2.text()

    def get_epochs(self):
        return self.ui.lineEdit.text()

    def set_result_label(self, result: dict):
        self.ui.listWidget_2.clear()
        for res in result.keys():
            self.ui.listWidget_2.addItem(f"Accuracy of {res} : {result[res]:.2f}%")

    def pop_up_progress_bar(self, maximum):
        self.progressBar.setMaximum(maximum)
        self.progressBar.setValue(0)
        self.label.setText("Training...")
        self.progress_window.show()

    def update_progress_bar(self, value):
        self.progressBar.setValue(value)

    def training_finished(self):
        self.label.setText("Training complete!")
    def enable_prediction(self):
        self.ui.pushButton.setEnabled(True)

    def fill_prediction(self, dimension):
        self.ui.listWidget.clear()
        for i in range(dimension):
            # Tworzenie kontenera z layoutem i polem tekstowym
            widget = QWidget()
            layout = QHBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)  # Bez marginesów
            line_edit = QLineEdit()
            validator = QDoubleValidator()
            validator.setNotation(QDoubleValidator.Notation.StandardNotation)
            line_edit.setValidator(validator)
            line_edit.setPlaceholderText(f"Feature {i + 1}")
            layout.addWidget(line_edit)
            widget.setLayout(layout)

            # Dodanie do listWidgeta
            item = QListWidgetItem()
            item.setSizeHint(widget.sizeHint())
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, widget)
