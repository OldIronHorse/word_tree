from word_tree import make_word_tree
from unittest import main, TestCase

class TestTreeDictionary(TestCase):
  def setUp(self):
    self.dictionary = make_word_tree(['cat', 'dog', 'do', 'dot', 'pig'
                                            'quit', 'deque'])

  def test_next_char_word_no_next(self):
    self.assertEqual([None], self.dictionary.next_char('dog'))

  def test_next_char_word_multiple_next(self):
    self.assertEqual(['g', 't', None],
                     self.dictionary.next_char('do'))

  def test_next_char_not_a_word(self):
    self.assertEqual([], self.dictionary.next_char('date'))

  def test_qu_next(self):
    self.assertEqual(['q'], self.dictionary.next_char('de'))


if __name__ == '__main__':
  main()
