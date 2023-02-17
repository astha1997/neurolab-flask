from fpdf import FPDF
from Scrapper import all_course, scrap_all, get_course
pdf = FPDF()
pdf.add_page()
# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 15)




list_courses = all_course()
for i in list_courses:
    filename=i+'.pdf'
    for key, value in get_course(i).items():
        #print(type(str(key)))
        #print(type(str(value)))
        pdf.set_font("Arial", size = 10)
        pdf.set_auto_page_break(auto= bool, margin = 0.0)
# create a cell
        pdf.cell(200, 10,  txt = str(key),ln = 1, align = 'L')
        pdf.set_font("Arial", size = 8)
# add another cell
        pdf.cell(1000, 10, txt = str(value),ln=2, align = 'L')
 
# save the pdf with name .pdf
    pdf.output(filename)
    
    



 

 


 


                    
    

    