'''
'''
from abc import abstractmethod, ABC

class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

class Editable(ABC):
    @abstractmethod
    def save(self, new_data):
        pass

class EditableDocument(Document, Editable):
    def __init__(self, data):
        self.data = data

    def open(self):
        print("Editable Document opened. Data:", self._preview())

    def save(self, new_data):
        self.data = new_data
        print("Document saved.")

    def get_data(self):
        return self.data

    def _preview(self):
        return self.data[:20] + "..."

class ReadOnlyDocument(Document):
    def __init__(self, data):
        self.data = data

    def open(self):
        print("Read-Only Document opened. Data:", self._preview())

    def get_data(self):
        return self.data

    def _preview(self):
        return self.data[:20] + "..."

class DocumentProcessor:
    def process(self, doc: Document):
        doc.open()
        print("Document processed.")

    def process_and_save(self, doc: Document, additional_info: str):
        if not isinstance(doc, Editable):
            raise ValueError("Document is not editable.")

        doc.open()
        current_data = doc.get_data()
        new_data = current_data + " | Processed: " + additional_info
        doc.save(new_data)
        print("Editable document processed and saved.")

if __name__ == "__main__":
    editable = EditableDocument("Draft proposal for Q3.")
    read_only = ReadOnlyDocument("Top secret strategy.")

    processor = DocumentProcessor()

    print("--- Processing Editable Document ---")
    processor.process_and_save(editable, "Reviewed by Alice")

    print("\n--- Processing Read-Only Document ---")
    processor.process(read_only)  # This works fine

