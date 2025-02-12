import tempfile
import json
import logging
import time
import os
from pathlib import Path

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

from converter_utils import convert_document_to_markdown_marker
from full_force_ocr import apply_full_force_ocr
from pipeline_builder import build_docling_pipeline


def convert_file(file_path, pipeline_choice, output_format):
    if not file_path:
        return "Please upload a file.", None

    if pipeline_choice == "Marker parse no OCR":
        try:
            content = convert_document_to_markdown_marker(file_path, force_ocr=False)
        except Exception as e:
            return f"Error: {e}", None

    elif pipeline_choice == "Marker parse Force OCR":
        try:
            content = convert_document_to_markdown_marker(file_path, force_ocr=True)
        except Exception as e:
            return f"Error: {e}", None

    elif pipeline_choice == "Docling parse full force OCR":
        try:
            content = apply_full_force_ocr(file_path)
        except Exception as e:
            return f"Error: {e}", None

    else:
        pipeline_options, backend = build_docling_pipeline(pipeline_choice)

        if backend is not None:
            pdf_format_option = PdfFormatOption(
                pipeline_options=pipeline_options,
                backend=backend
            )
        else: 
            pdf_format_option = PdfFormatOption(
                pipeline_options=pipeline_options
            )
        
        converter = DocumentConverter(
            format_options={
                InputFormat.PDF: pdf_format_option
            }
        )
        try:
            start = time.time()
            result = converter.convert(Path(file_path))
            duration = time.time() - start
            logging.info(f"Processed in {duration:.2f} seconds.")
            doc = result.document

            if output_format == "Markdown":
                content = doc.export_to_markdown()
            elif output_format == "JSON":
                content = json.dumps(doc.export_to_dict(), ensure_ascii=False, indent=2)
            elif output_format == "Text":
                content = doc.export_to_text()
            elif output_format == "Document Tags":
                content = doc.export_to_document_tokens()
            else:
                content = "Unknown format"
        except Exception as e:
            return f"Error: {e}", None

    if pipeline_choice in [
        "Marker parse no OCR",
        "Marker parse Force OCR",
        "Docling parse full force OCR"
    ]:
        if output_format == "Markdown":
            pass
        elif output_format == "JSON":
            content = json.dumps({"content": content}, ensure_ascii=False, indent=2)
        elif output_format == "Text":
            content = content.replace("#", "").replace("*", "").replace("_", "")
        elif output_format == "Document Tags":
            content = f"<doc>\n{content}\n</doc>"

    if output_format == "Markdown":
        ext = ".md"
    elif output_format == "JSON":
        ext = ".json"
    elif output_format == "Text":
        ext = ".txt"
    elif output_format == "Document Tags":
        ext = ".doctags"
    else:
        ext = ".txt"

    try:
        with tempfile.NamedTemporaryFile(mode="w", suffix=ext, delete=False, encoding="utf-8") as tmp:
            tmp.write(content)
            tmp_path = tmp.name
        return content, tmp_path
    except Exception as e:
        return f"Error: {e}", None
