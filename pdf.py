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
        print(filename)
        if filename=='Be A DevOps Pro Tech Neuron.pdf' or filename=='Cyber Security Masters.pdf' or filename=='Tibco Business Works.pdf' or filename=='Cyber Security Foundations.pdf' or filename=='Explainable AI.pdf' or filename=='Be A DevOps Pro.pdf' or filename=='Youtube Mastery Course in Hindi Tech Neuron.pdf' or filename=='Cyber Security Masters Tech Neuron.pdf':
                continue
        
        CourseName=get_course(i)['Course_title']
        pdf.set_font("Arial", size = 11)
        pdf.cell(200, 10,  txt = 'CourseName',ln = 1, align = 'L')
        #pdf.set_font("Arial", size = 9)
        pdf.multi_cell( 200,10,txt = CourseName)
            
        Description=get_course(i)['Description']
        pdf.set_font("Arial", size = 11)
        pdf.cell(200, 10,  txt = 'Description',ln = 1, align = 'L')
        #pdf.set_font("Arial", size = 9)
        pdf.multi_cell( 200,10,txt = Description)
            
        Language=get_course(i)['Language']
        pdf.set_font("Arial", size = 11)
        pdf.cell(200, 10,  txt = 'Language',ln = 1, align = 'L')
        #pdf.set_font("Arial", size = 9)
        pdf.multi_cell( 200,10,txt = Language)
            
        Pricing=get_course(i)['Pricing'] 
        pdf.set_font("Arial", size = 11)
        pdf.cell(200, 10,  txt = 'Pricing',ln = 1, align = 'L')
        #pdf.set_font("Arial", size = 9)
        pdf.multi_cell( 200,10,txt = str(Pricing))
            
        Curriculum_data=' '.join(get_course(i)['Curriculum_data'])
        pdf.set_font("Arial", size = 11)
        pdf.cell(200, 10,  txt = 'Curriculum_data',ln = 1, align = 'L')
        #pdf.set_font("Arial", size = 9)
        pdf.multi_cell( 200,10,txt = Curriculum_data)
            
        Learn=' '.join(get_course(i)['Learn'])
        pdf.set_font("Arial", size = 11)
        pdf.cell(200, 10,  txt = 'Learn',ln = 1, align = 'L')
        #pdf.set_font("Arial", size = 9)
        pdf.multi_cell( 200,10,txt = Learn)
            
        Requirements=' '.join(get_course(i)['Requirements'])
        pdf.set_font("Arial", size = 11)
        pdf.cell(200, 10,  txt = 'Requirements',ln = 1, align = 'L')
        #pdf.set_font("Arial", size = 9)
        pdf.multi_cell( 200,10,txt = Requirements)
               
               
                
        # save the pdf with name .pdf
        pdf.output(filename)
    
    
    



 

 


 


                    
    

    
