import pdfkit

class PdfHandler:
    """
    THis object deals with pdf and converts them to html that are editable
    """

    def __init__(self,pdf_file) -> None:
        self.pdf_file = pdf_file


    def convert_to_html(self)-> str:
        """
        main method to convert pdf to html
        """
        pass
            




class HtmlHandler:
    """
    This object deals with the edited html and converts them to pdf.
    
    """

    def __init__(self,html_content) -> None:
        pass    