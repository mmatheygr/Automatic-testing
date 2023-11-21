from bin.perceptron import Perceptron

def test_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    assert the_perceptron.predict([1,1]) ==  1, "assert comment"
    assert the_perceptron.predict([1,0]) ==  1, "assert comment"
    assert the_perceptron.predict([0,1]) ==  1, "assert comment"
    assert the_perceptron.predict([0,0]) ==  0, "assert comment"
