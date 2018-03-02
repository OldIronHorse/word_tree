def next_char(node, part_word):
  try:
    c = part_word[0]
    rest_word = part_word[1:]
    try:
      return next_char(node[c], rest_word)
    except KeyError:
      return []
  except IndexError:
    return sorted(node.keys(), key=lambda c: 'zz' if c is None else c)

def add(node, word):
  try:
    c = word[0]
    rest_word = word[1:]
    try:
      child = node[c]
    except KeyError:
      child = {}
      node[c] = child
    add(child, rest_word)
  except IndexError:
    node[None] = True


def make_word_tree(wordlist):
  root_node = {}
  for word in wordlist:
    add(root_node, word)
  return root_node
