# Exercise 10 - Interface Segregation
class Printable:
    def print(self, document):
        raise NotImplementedError

class Scannable:
    def scan(self, document):
        raise NotImplementedError

class Faxable:
    def fax(self, document):
        raise NotImplementedError

class Printer(Printable):
    def print(self, document):
        print(f"Printing: {document}")

class Scanner(Scannable):
    def scan(self, document):
        print(f"Scanning: {document}")

class MultiFunctionPrinter(Printable, Scannable, Faxable):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")

    def fax(self, document):
        print(f"Faxing: {document}")

if __name__ == '__main__':
    printer = Printer()
    printer.print("Test Document")
    scanner = Scanner()
    scanner.scan("Test Document")
    mfp = MultiFunctionPrinter()
    mfp.print("Test Document")
    mfp.scan("Test Document")
    mfp.fax("Test Document")
