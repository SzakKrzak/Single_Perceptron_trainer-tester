class MyPerceptron:
    def __init__(self, label, dimension):
        self.weights = [1.0 for _ in range(dimension)]
        self.threshold = 1.0
        self.label = label

    @property
    def dimension(self):
        return len(self.weights)

    def calculate_net(self, input_vector: [float]) -> float:
        return sum(float(i) * w for i, w in zip(input_vector, self.weights)) - self.threshold

    def compute(self, input_vector) -> int:
        net = self.calculate_net(input_vector)
        return 1 if net >= 0 else 0

    def learn(self, input_vector, decision, alfa):
        d = 1 if decision == self.label else 0
        prediction = self.compute(input_vector)
        self.weights = [
            w + (d - prediction) * alfa * float(i)
            for w, i in zip(self.weights, input_vector)
        ]
        self.threshold = self.threshold - (d - prediction) * alfa


class Trainer:
    def __init__(self, training_set, test_set):
        self.training_set = training_set
        self.test_set = test_set
        self.dimension = len(training_set[0]) - 1  # last column = label
        self.labels = {sample[-1] for sample in training_set}
        self.perceptrons = [MyPerceptron(label, self.dimension) for label in self.labels]

    def test(self):
        accuracy_dict = dict()
        for perceptron in self.perceptrons:
            accurate_count = 0
            for line in self.test_set:
                y_label = line[-1]
                y = perceptron.compute(line[:-1])
                p_label = perceptron.label
                if (y == 1 and p_label == y_label) or (y == 0 and p_label != y_label):
                    accurate_count += 1
            accuracy_dict[perceptron.label] = accurate_count / len(self.test_set) * 100
        return accuracy_dict

    def train(self, learning_rate, epochs, on_epoch_done=None):
        progress = 0
        for perceptron in self.perceptrons:
            for epoch in range(epochs):
                for line in self.training_set:
                    perceptron.learn(line[:-1], line[-1], learning_rate)
                progress += 1
                if on_epoch_done:
                    on_epoch_done(progress)
    def predict(self, input_vector):
        max_net = self.perceptrons[0].calculate_net(input_vector)
        max_label = self.perceptrons[0].label
        for perceptron in self.perceptrons[1:]:
            net = perceptron.calculate_net(input_vector)
            if net >= max_net:
                max_net = net
                max_label = perceptron.label

        return max_label