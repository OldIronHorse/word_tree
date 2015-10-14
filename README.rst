word_tree
---------

Efficient lookup of next possible character(s) given a starting word fragment.
This is intended for use in word game strategies (Boggle, Scrabble, Anagram).

To use:

  >>> import word_tree
  >>> with open('words.lst') as wl:
  ...   wt = word_tree.make_word_tree([w.strip() for w in wl])
  ...
  >>> wt.next_char('do')
  ['c', 'e', 'd', 'g', 'i', 'm', 'l', 'o', 'n', 'p', 's', 'r', 'u', 't', 'w',
   'v', 'z', None]

