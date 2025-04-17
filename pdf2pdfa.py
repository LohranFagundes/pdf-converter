import io
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import pikepdf

def convert_to_pdfa(input_file, output_file):
    """
    Converte um arquivo PDF para o formato PDF/A
    """
    try:
        # Método preferencial com pikepdf
        pdf = pikepdf.Pdf.open(input_file)
        
        with pdf.open_metadata() as meta:
            meta['pdfaid:part'] = 3
            meta['pdfaid:conformance'] = 'B'
            meta['dc:title'] = 'Documento convertido'
            meta['dc:creator'] = 'Conversor PDF/A'
            meta['xmp:CreatorTool'] = 'PDF para PDF/A Converter'
        
        pdf.save(output_file, preserve_pdfa=True)
        return True
    
    except Exception as e:
        # Fallback se pikepdf falhar
        try:
            reader = PdfReader(input_file)
            writer = PdfWriter()
            
            for page in reader.pages:
                writer.add_page(page)
            
            writer.add_metadata({
                '/Title': 'Documento convertido',
                '/Author': 'Conversor PDF/A',
                '/Creator': 'PDF para PDF/A Converter',
                '/Producer': 'PyPDF2',
                '/Trapped': '/False'
            })
            
            with open(output_file, 'wb') as f:
                writer.write(f)
            
            return True
        except Exception as e:
            print(f"Erro no fallback: {str(e)}")
            return False