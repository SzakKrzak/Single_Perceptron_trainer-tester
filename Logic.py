import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox, QLineEdit

from Model import Model, TrainThread
from PWindow import MyView


class Controller:
    def __init__(self, model, view: MyView):
        self.model = model
        self.view = view
        self.train_thread = None  # Referencja do wątku

        # Podłączenie przycisków
        self.view.ui.btn_sel_test.clicked.connect(self.assign_test_file)
        self.view.ui.btn_sel_train.clicked.connect(self.assign_train_file)
        self.view.ui.btn_create_trainer.clicked.connect(self.create_trainer)
        self.view.ui.btn_trainer_train.clicked.connect(self.trainer_train)
        self.view.ui.btn_trainer_test.clicked.connect(self.trainer_test)
        self.view.ui.pushButton.clicked.connect(self.predict)

    def assign_test_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self.view, "Select a test file", "", "CSV Files (*.csv)")
        if not file_path:
            return
        self.model.initialize_test_set(file_path)
        self.view.set_test_file_path_label(Path(file_path).name)
        if self.model.train_set is not None:
            self.view.enable_trainer_creation()

    def assign_train_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self.view, "Select a train file", "", "CSV Files (*.csv)")
        if not file_path:
            return
        self.model.initialize_train_set(file_path)
        self.view.set_train_file_path_label(Path(file_path).name)
        if self.model.test_set is not None:
            self.view.enable_trainer_creation()

    def create_trainer(self):
        if not self.model.approve_sets():
            QMessageBox.warning(self.view, "Warning", "Sets have different dimensions.")
            return
        self.model.create_trainer()
        self.view.enable_test_train()
        self.view.set_trainer_label(
            f"Trainer created for\n"
            f"train_set: {self.model.train_path}\n"
            f"test_set: {self.model.test_path}\n"
        )
        self.view.fill_prediction(self.model.trainer.dimension)
        self.view.enable_prediction()

    def trainer_train(self):
        try:
            learning_rate = float(self.view.get_learning_rate().replace(',', '.'))
            epochs = int(self.view.get_epochs())
        except ValueError:
            QMessageBox.warning(self.view, "Warning", "Learning rate and epochs must be valid numbers.")
            return

        max_progress = len(self.model.trainer.labels) * epochs
        self.view.pop_up_progress_bar(max_progress)

        self.train_thread = TrainThread(self.model.trainer, learning_rate, epochs)
        self.train_thread.progress_changed.connect(self.view.update_progress_bar)
        self.train_thread.finished.connect(self.view.training_finished)
        self.train_thread.start()

    def trainer_test(self):
        accuracy = self.model.test()
        self.view.set_result_label(accuracy)

    def predict(self):
        input_vector = []
        for i in range(self.view.ui.listWidget.count()):
            item = self.view.ui.listWidget.item(i)
            widget = self.view.ui.listWidget.itemWidget(item)
            line_edit = widget.findChild(QLineEdit)
            if line_edit:
                input_vector.append(float(line_edit.text()))
        prediction = self.model.trainer.predict(input_vector)
        self.view.ui.listWidget_2.addItem(f"Prediction: {prediction}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewDialog = MyView()
    myModel = Model()
    controller = Controller(myModel, viewDialog)
    viewDialog.show()
    sys.exit(app.exec())
