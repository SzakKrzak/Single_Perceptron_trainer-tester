import random
from pathlib import Path

from PySide6.QtCore import QThread, Signal

from MyPerceptron import Trainer


class Model:
    def __init__(self):
        self.train_path = None
        self.test_path = None
        self.train_set = None
        self.test_set = None
        self.trainer = None

    def create_trainer(self):
        self.trainer = Trainer(self.train_set, self.test_set)
    def initialize_test_set(self,file_path):
        with open(file_path, 'r') as f:
            result = [line.strip().split(';') for line in f.readlines()]
            random.shuffle(result)
            self.test_set = result
            self.test_path = Path(file_path).name

    def initialize_train_set(self,file_path):
        with open(file_path, 'r') as f:
            result = [line.strip().split(';') for line in f.readlines()]
            random.shuffle(result)
            self.train_set = result
            self.train_path = Path(file_path).name

    def approve_sets(self):
        return len(self.train_set[0]) == len(self.test_set[0])

    def test(self):
        return self.trainer.test()
class TrainThread(QThread):
    progress_changed = Signal(int)
    finished = Signal()
    def __init__(self, trainer, learning_rate, epochs):
        super().__init__()
        self.trainer = trainer
        self.learning_rate = float(learning_rate)
        self.epochs = int(epochs)
    def run(self):
        progress = 0
        for perceptron in self.trainer.perceptrons:
            for epoch in range(self.epochs):
                progress += 1
                for line in self.trainer.training_set:
                    perceptron.learn(line, line[-1], self.learning_rate)
                self.progress_changed.emit(progress)
        self.finished.emit()