"""
This is a class
"""
class Perceptron:
    """
    This is perceptron
    """
    def __init__(self):
        self._weights = 0
    def train(self, inputs, labels):
        """
        This is train
        """
        dummied_inputs = [x + [-1] for x in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])
        for _ in range(5000):
            for input_iterable, label in zip(dummied_inputs, labels):
                label_delta = (label - self.predict_function(input_iterable))
                for index_iterable, x_iterable in enumerate(input_iterable):
                    self._weights[index_iterable] += .1 * x_iterable * label_delta
    def predict_function(self, input_def):
        """
        This is predict
        """
        if len(input_def) == 0:
            return None
        input_def = input_def + [-1]
        return int(0 < sum([x[0]*x[1] for x in zip(self._weights, input_def)]))
