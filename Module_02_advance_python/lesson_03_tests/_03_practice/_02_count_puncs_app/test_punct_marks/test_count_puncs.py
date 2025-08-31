from count_puncs import count_punct_marks  # для запуска из терминала находясь в текущей директории


def test_empty_string():
    assert count_punct_marks('') == 0


def test_no_punctuation():
    assert count_punct_marks('Hello World') == 0


def test_single_punctuation(string_for_test):
    assert count_punct_marks(string_for_test) == 1


def test_multiple_punctuation(string_for_test):
    assert count_punct_marks('Hello, World! How are you?') == 3


def test_edge_case():
    assert count_punct_marks('!!!') == 3


def test_all_punctuation():
    assert count_punct_marks(",.:;'!?") == 7
