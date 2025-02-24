# converter_utils.py

from docling.document_converter import DocumentConverter
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

def convert_document_to_markdown(source):
    """
    Convert a document (local path or URL) to Markdown using docling.

    Args:
        source (str): The file path or URL of the document.

    Returns:
        str: The Markdown version of the document.
    """
    converter = DocumentConverter()
    result = converter.convert(source)
    return result.document.export_to_markdown()

def convert_document_to_markdown_marker(source, force_ocr=False):
    """
    Convert a document to Markdown using marker.

    Args:
        source (str): The file path of the document.
        force_ocr (bool): Whether to force OCR processing.

    Returns:
        str: The Markdown version of the document.
    """
    converter = PdfConverter(
        artifact_dict=create_model_dict(),
        config={"force_ocr": force_ocr}
    )
    rendered = converter(source)
    text, _, _ = text_from_rendered(rendered)
    return text
