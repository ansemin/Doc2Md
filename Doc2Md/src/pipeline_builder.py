import logging
import time
from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    AcceleratorDevice,
    AcceleratorOptions,
    PdfPipelineOptions,
)
from docling.models.tesseract_ocr_model import TesseractOcrOptions
from docling.models.tesseract_ocr_cli_model import TesseractCliOcrOptions
from docling.models.ocr_mac_model import OcrMacOptions


def build_docling_pipeline(pipeline_choice):
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_table_structure = True
    pipeline_options.table_structure_options.do_cell_matching = True

    backend = None

    if pipeline_choice == "PyPdfium no OCR":
        pipeline_options.do_ocr = False
        backend = PyPdfiumDocumentBackend

    elif pipeline_choice == "PyPdfium EasyOCR":
        pipeline_options.do_ocr = True
        backend = PyPdfiumDocumentBackend

    elif pipeline_choice == "Docling parse no OCR":
        pipeline_options.do_ocr = False

    elif pipeline_choice == "Docling parse EasyOCR":
        pipeline_options.do_ocr = True
        pipeline_options.ocr_options.lang = ["es"]
        pipeline_options.accelerator_options = AcceleratorOptions(
            num_threads=4, device=AcceleratorDevice.AUTO
        )

    elif pipeline_choice == "Docling parse EasyOCR (CPU only)":
        pipeline_options.do_ocr = True
        pipeline_options.ocr_options.lang = ["es"]
        pipeline_options.ocr_options.use_gpu = False

    elif pipeline_choice == "Docling parse Tesseract":
        pipeline_options.do_ocr = True
        pipeline_options.ocr_options = TesseractOcrOptions()

    elif pipeline_choice == "Docling parse Tesseract CLI":
        pipeline_options.do_ocr = True
        pipeline_options.ocr_options = TesseractCliOcrOptions()

    elif pipeline_choice == "Docling parse ocrmac":
        pipeline_options.do_ocr = True
        pipeline_options.ocr_options = OcrMacOptions()

    return pipeline_options, backend
