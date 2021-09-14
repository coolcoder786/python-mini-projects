from fpdf import FPDF

pdf_file = FPDF()
pdf_file.add_page()
pdf_file.set_font("Arial" , size=20)
pdf_file.cell(200 , 10 , "follow python_is_fun for more stuffs like this" )
pdf_file.output("python.pdf" ) 