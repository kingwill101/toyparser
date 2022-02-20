from scanner import Scanner


def test_token_count():
  scan = Scanner(b'let')
  assert(len(scan.tokens) == 0)
  scan.scanTokens()
  assert(len(scan.tokens) == 1)