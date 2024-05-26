import pytest

from utils.get_tags import get_tags

testdata = [
    ('#Hello, world!', ['hello']),
    ('#Python is a great language!', ['python']),
    ('#Coding is fun.', ['coding']),
    ('I love #programming.', ['programming']),
    ('#AI is the future.', ['ai']),
    ('#MachineLearning is a subset of AI.', ['machine-learning']),
    ('#DeepLearning is a subset of Machine Learning.', ['deep-learning']),
    ('#NeuralNetworks are used in Deep Learning.', ['neural-networks']),
    ('#DataScience involves a lot of statistics.', ['data-science']),
    ('#BigData is a trending field.', ['big-data']),
    ('#CloudComputing is becoming more popular.', ['cloud-computing']),
    ('#Python and #Java are popular languages.', ['python', 'java']),
    ('#Coding and #programming are fun.', ['coding', 'programming']),
    ('#AI and #MachineLearning are the future.', ['ai', 'machine-learning']),
    ('#DeepLearning and #NeuralNetworks are subsets of AI.', ['deep-learning', 'neural-networks']),
    ('#DataScience and #BigData involve a lot of statistics.', ['data-science', 'big-data']),
    ('#CloudComputing and #BigData are becoming more popular.', ['cloud-computing', 'big-data']),
    ('#SuperAwesomeTag and his #friends.', ['super-awesome-tag', 'friends']),
]


@pytest.mark.parametrize("content,expected", testdata)
def test_get_tags(content, expected):
    assert get_tags(content) == expected
