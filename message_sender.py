class Printer:
    def print_document(self, document, copies=1):
        print(f"Printing {copies} copy/copies of '{document}'")

class LaserPrinter(Printer):
    def print_document(self, document, copies=1):
        print("LaserPrinter:", end=" ")
        super().print_document(document, copies)

class InkjetPrinter(Printer):
    def print_document(self, document, copies=1):
        print("InkjetPrinter:", end=" ")
        super().print_document(document, copies)

class MultiFunctionPrinter(LaserPrinter, InkjetPrinter):
    pass

if __name__ == "__main__":
    print("Printer System Example:")

    # Overloading (default argument copies)
    p = Printer()
    p.print_document("Report.pdf")
    p.print_document("Invoice.pdf", 3)

    # Overriding
    laser = LaserPrinter()
    laser.print_document("Thesis.docx", 2)

    # MRO with multiple inheritance
    mfp = MultiFunctionPrinter()
    mfp.print_document("Presentation.pptx", 5)
    print("MRO:", [cls.__name__ for cls in MultiFunctionPrinter.mro()])