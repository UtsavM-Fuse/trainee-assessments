from abc import ABC, abstractmethod


# Abstract Builder class
class DocumentBuilder(ABC):
    @abstractmethod
    def create_document(self):
        """
        Create a new document.

        Returns:
            None
        """
        pass

    @abstractmethod
    def add_heading(self, text: str):
        """
        Add a heading to the document.

        Args:
            text (str): The heading text.

        Returns:
            None
        """
        pass

    @abstractmethod
    def add_paragraph(self, text: str):
        """
        Add a paragraph to the document.

        Args:
            text (str): The paragraph text.

        Returns:
            None
        """
        pass

    @abstractmethod
    def save_document(self, filename: str):
        """
        Save the document to a file.

        Args:
            filename (str): The name of the file to save the document.

        Returns:
            None
        """
        pass


# Concrete PDF Document Builder
class PDFDocumentBuilder(DocumentBuilder):
    def create_document(self):
        print("Creating PDF document...")
        # Code to create a new PDF document

    def add_heading(self, text: str):
        print(f"Adding PDF heading: {text}")
        # Code to add a heading to the PDF document

    def add_paragraph(self, text: str):
        print(f"Adding PDF paragraph: {text}")
        # Code to add a paragraph to the PDF document

    def save_document(self, filename: str):
        print(f"Saving PDF document to {filename}")
        # Code to save the PDF document to the specified file


# Concrete HTML Document Builder
class HTMLDocumentBuilder(DocumentBuilder):
    def create_document(self):
        print("Creating HTML document...")
        # Code to create a new HTML document

    def add_heading(self, text: str):
        print(f"Adding HTML heading: {text}")
        # Code to add a heading to the HTML document

    def add_paragraph(self, text: str):
        print(f"Adding HTML paragraph: {text}")
        # Code to add a paragraph to the HTML document

    def save_document(self, filename: str):
        print(f"Saving HTML document to {filename}")
        # Code to save the HTML document to the specified file


# Concrete Plain Text Document Builder
class PlainTextDocumentBuilder(DocumentBuilder):
    def create_document(self):
        print("Creating Plain Text document...")
        # Code to create a new Plain Text document

    def add_heading(self, text: str):
        print(f"Adding Plain Text heading: {text}")
        # Code to add a heading to the Plain Text document

    def add_paragraph(self, text: str):
        print(f"Adding Plain Text paragraph: {text}")
        # Code to add a paragraph to the Plain Text document

    def save_document(self, filename: str):
        print(f"Saving Plain Text document to {filename}")
        # Code to save the Plain Text document to the specified file


# Director class
class DocumentGenerator:
    def __init__(self, builder: DocumentBuilder):
        self.builder = builder

    def generate_document(self, heading: str, paragraphs: list[str], filename: str):
        self.builder.create_document()
        self.builder.add_heading(heading)
        for paragraph in paragraphs:
            self.builder.add_paragraph(paragraph)
        self.builder.save_document(filename)


# Client code
if __name__ == "__main__":
    pdf_builder = PDFDocumentBuilder()
    html_builder = HTMLDocumentBuilder()
    plain_text_builder = PlainTextDocumentBuilder()

    document_generator = DocumentGenerator(pdf_builder)
    document_generator.generate_document(
        "Sample PDF Document",
        ["This is a sample PDF document.", "It contains multiple paragraphs."],
        "sample.pdf",
    )

    document_generator = DocumentGenerator(html_builder)
    document_generator.generate_document(
        "Sample HTML Document",
        ["This is a sample HTML document.", "It contains multiple paragraphs."],
        "sample.html",
    )

    document_generator = DocumentGenerator(plain_text_builder)
    document_generator.generate_document(
        "Sample Plain Text Document",
        ["This is a sample plain text document.", "It contains multiple paragraphs."],
        "sample.txt",
    )
