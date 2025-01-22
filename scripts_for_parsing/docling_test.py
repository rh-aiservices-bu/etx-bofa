from pathlib import Path
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, OcrMacOptions, TableStructureOptions, TableFormerMode, TesseractOcrOptions
from docling.document_converter import PdfFormatOption
from tqdm import tqdm

def convert_pdf(file: dict):
    # Set up pipeline options
    pipeline_options = PdfPipelineOptions(table_structure_options=TableStructureOptions(do_cell_matching=True, mode=TableFormerMode.ACCURATE))
    pipeline_options.do_ocr = True
    pipeline_options.do_table_structure = True
    pipeline_options.table_structure_options.do_cell_matching = True
    # pipeline_options.ocr_options = OcrMacOptions()  # Configure ocrmac options
    pipeline_options.ocr_options = TesseractOcrOptions()  # Configure ocrmac options
    pdf_path = file['file']
    # Create converter with the options
    doc_converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )

    # Convert the document
    result = doc_converter.convert(pdf_path)
    file['markdown'] = result.document.export_to_markdown()
    return file

from multiprocessing import Pool

def process_all_pdfs_multiprocessing(files, max_processes=14):
    results = []
    with Pool(processes=max_processes) as pool:
        for output in tqdm(pool.imap_unordered(convert_pdf, files), total=len(files)):
            results.append(output)
    return results

if __name__ == "__main__":
    boa_docs_dir = Path.cwd() / "boa_docs"
    files = [f for f in boa_docs_dir.iterdir() if f.suffix.lower() == '.pdf']
    files = [{'file':f} for f in files]

    results = process_all_pdfs_multiprocessing(files)
    # results = [convert_pdf(f) for f in tqdm(files[:2])]
    # Write markdown files with _ocrmac suffix
    for result in results:
        pdf_path = result['file']
        markdown_content = result['markdown']
        # Create output path by removing .pdf and appending _ocrmac.md
        output_path = pdf_path.parent / f"{pdf_path.stem}_ocrmac.md"
        output_path.write_text(markdown_content)

    from IPython import embed; embed()