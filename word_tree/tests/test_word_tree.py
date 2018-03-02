from word_tree import make_word_tree, next_char
from unittest import main, TestCase

class TestTreeDictionary(TestCase):
  def setUp(self):
    self.dictionary = make_word_tree(['cat', 'dog', 'do', 'dot', 'pig'
                                            'quit', 'deque'])

  def test_next_char_word_no_next(self):
    self.assertEqual([None], next_char(self.dictionary, 'dog'))

  def test_next_char_word_multiple_next(self):
    self.assertEqual(['g', 't', None],
                     next_char(self.dictionary, 'do'))

  def test_next_char_not_a_word(self):
    self.assertEqual([], next_char(self.dictionary, 'date'))

  def test_qu_next(self):
    self.assertEqual(['q'], next_char(self.dictionary, 'de'))


if __name__ == '__main__':
  main()
