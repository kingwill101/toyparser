from scanner import Scanner

# (print 'hello world') {} != 1234 5.5

langInput = b'''let x = 100
let z = 1000

x = x + z'''

def main():
    scanner = Scanner(langInput)
    scanner.scanTokens()
    print(f"tokens found: {len(scanner.tokens)}")
    for token in scanner.tokens:
        print(token, "\n")

if __name__ == "__main__":
    main()