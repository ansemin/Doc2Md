# Import all parsers to ensure they register themselves
from parsers.pypdfium_parser import PyPdfiumParser
from parsers.docling_parser import DoclingParser
from parsers.marker_parser import MarkerParser

# You can add new parsers here in the future 

# This file makes the parsers directory a Python package 