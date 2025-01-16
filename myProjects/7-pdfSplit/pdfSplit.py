import sys
from PyPDF2 import PdfReader, PdfWriter

def extract_pages(input_pdf, output_pdf, start_page, end_page):
    try:
        reader = PdfReader(input_pdf)

        # Verificar se o PDF está criptografado
        if reader.is_encrypted:
            try:
                reader.decrypt("")  # Tenta descriptografar com uma senha vazia
                print("PDF criptografado foi descriptografado com sucesso.")
            except Exception:
                raise ValueError("O PDF está criptografado e requer uma senha.")

        writer = PdfWriter()
        total_pages = len(reader.pages)

        if start_page < 1 or end_page > total_pages or start_page > end_page:
            raise ValueError(f"Intervalo de páginas inválido: {start_page} a {end_page} em um PDF com {total_pages} páginas.")

        for page_num in range(start_page - 1, end_page):
            writer.add_page(reader.pages[page_num])

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

        print(f"Páginas {start_page} a {end_page} foram extraídas com sucesso para {output_pdf}.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{input_pdf}' não foi encontrado.")
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python pdfSplit.py <input_pdf> <output_pdf> <start_page> <end_page>")
    else:
        input_pdf = sys.argv[1]
        output_pdf = sys.argv[2]
        try:
            start_page = int(sys.argv[3])
            end_page = int(sys.argv[4])
            extract_pages(input_pdf, output_pdf, start_page, end_page)
        except ValueError:
            print("Erro: As páginas inicial e final devem ser números inteiros.")
# sample:
#  python .\pdfSplit.py '.\Neurociências_Desvendando_o_Sistema_Nervoso_4ª_Ed_Mark_F_Bear (2).pdf' 'C7.pdf' 221 258
#  python .\pdfSplit.py '.\Neurociências_Desvendando_o_Sistema_Nervoso_4ª_Ed_Mark_F_Bear (2).pdf' 'C7-apend.pdf' 261 291
#  python .\pdfSplit.py '.\Neurociências_Desvendando_o_Sistema_Nervoso_4ª_Ed_Mark_F_Bear (2).pdf' 'C8.pdf' 307 334
#  python .\pdfSplit.py '.\Neurociências_Desvendando_o_Sistema_Nervoso_4ª_Ed_Mark_F_Bear (2).pdf' 'C9.pdf' 335 371
#  python .\pdfSplit.py '.\Neurociências_Desvendando_o_Sistema_Nervoso_4ª_Ed_Mark_F_Bear (2).pdf' 'C10.pdf' 335 408