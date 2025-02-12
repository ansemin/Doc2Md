from pathlib import Path
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    TesseractCliOcrOptions,
    PdfPipelineOptions,
)
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

def apply_full_force_ocr(file_path):
    """
    Apply full force OCR to a document and convert it to Markdown using docling.

    Args:
        file_path (str): The file path of the document.

    Returns:
        str: The Markdown version of the document with OCR applied.
    """
    input_doc = Path(file_path)

    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = True
    pipeline_options.do_table_structure = True
    pipeline_options.table_structure_options.do_cell_matching = True

    ocr_options = TesseractCliOcrOptions(force_full_page_ocr=True)
    pipeline_options.ocr_options = ocr_options

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(
                pipeline_options=pipeline_options,
            )
        }
    )

    doc = converter.convert(input_doc).document
    return doc.export_to_markdown()
