import json
import logging
import mysql.connector
from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as bs

from mongodb import mongodbconnection
from sql import sqldbconnection

### Setting up Logging file ###
logging.basicConfig(filename="flask_logs.log",
                    format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

### Function to Scrap all course title from iNeuron website ###


def all_course():
    """
    It scrapes the website and returns a list of all the courses available on the website.
    
    Returns:
      A list of all the courses available on the website.
    """
    try:
        ineuron_url = 'https://ineuron.ai/courses'
        uClient = uReq(ineuron_url)
        ineuron_page = uClient.read()
        uClient.close()
        ineuron_html = bs(ineuron_page, 'html.parser')
        course_data = json.loads(ineuron_html.find('script', {"id": "__NEXT_DATA__"}).get_text())
        all_courses = course_data['props']['pageProps']['initialState']['init']['courses']
        course_namelist = list(all_courses.keys())
        return course_namelist
    except:
        logging.error('Error in scraping at all_course()')

### Function to Scrap one Course details from iNeuron website ###


def get_course(coursename):
    """
    It takes a course name as input and returns a dictionary of all the details of the course.
    
    Args:
      coursename: The name of the course you want to scrape.
    
    Returns:
      A dictionary of course details
    """
    ineuron_url = 'https://ineuron.ai/course/'
    
    uClient = uReq(ineuron_url + str(coursename).replace(" ", "-"))
    course_page = uClient.read()
    uClient.close()
    ineuron_html = bs(course_page, 'html.parser')
    course_data1 = json.loads(ineuron_html.find(
        'script', {"id": "__NEXT_DATA__"}).get_text())
    logging.info('Course data saved as JSON format')
    all_dict = {}
    # list = []
    try:
        try:
            all_data = course_data1["props"]["pageProps"]
        except:
            all_data = 'No page'
        try:
            page_data = all_data['data']
        except:
            page_data = 'No data'
        try:
            detailed_data = page_data['details']
        except:
            detailed_data = 'No details'
        try:
            meta_data = page_data['meta']
        except:
            meta_data = 'No meta_data'
        try:
            curriculum_data = meta_data['curriculum']
        except:
            curriculum_data = 'No curriculum_data'
        try:
            overview_data = meta_data['overview']
        except:
            overview_data = 'No overview_data'
# Building a Course Dictionary
        try:
            pricing_inr = detailed_data['pricing']['IN']
        except:
            pricing_inr = 'NULL'
        try:
            course_name = page_data['title']
        except:
            course_name = 'Name NA'
        try:
            description = detailed_data['description']
        except:
            description = "NULL"
        try:
            language = overview_data['language']
        except:
            language = 'NULL'
        try:
            req = overview_data['requirements']
        except:
            req = 'NULL'
        try:
            learn = overview_data['learn']
        except:
            learn = 'NULL'
        curriculum = []
        try:
            for i in curriculum_data:
                curriculum.append(curriculum_data[i]["title"])
                ### Saving all the data in dictionary format ###
            all_dict = {"Course_title": course_name, "Description": description,
                        "Language": language, "Pricing": pricing_inr,
                        "Curriculum_data": curriculum, "Learn": learn,
                        "Requirements": req}
            logging.info('dict is created')
        except:
            curriculum.append('NULL')
        return all_dict
    except:
        logging.error('Error in Scrapping at get_course()')

### Function which gets all the course data and saves it in mongodb ###


def scrap_all():
    """
    It checks if the collection is present in the database, if it is, it does nothing, if it isn't, it
    scrapes the data and inserts it into the database
    """
    dbcon = mongodbconnection(username='mongodb', password='mongodb')
    db_collection = dbcon.getCollection("iNeuron_scrapper", "course_collection")
    try:
        if dbcon.isCollectionPresent("iNeuron_scrapper", "course_collection"):
            pass
        else:
            final_list = []
            list_courses = all_course()
            
            for i in list_courses:
                final_list.append(get_course(i))
            db_collection.insert_many(final_list)
            
    except Exception as e:
        logging.error("error in DB insertion", e)

def sql_insert():
    """
    It checks if the data is present in the table if it is, it does nothing, if it isn't, it
    scrapes the data and inserts it into the table
    """
    
    sqldbcon = sqldbconnection(host="localhost",user="abc",password="password")
     

    try:
        data_list=[]
        final_list = []
        list_courses = all_course()
        mydb = mysql.connector.connect(host="localhost",user="abc",password="password")
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute('use iNeuron_scrapper')
        mycursor.execute('truncate table course_collection')
        count=0        
        for i in list_courses:
            count+=1
            final_list.append(get_course(i).values())
            CourseName=get_course(i)['Course_title']
            Description=get_course(i)['Description']
            Language=get_course(i)['Language']
            Pricing=get_course(i)['Pricing'] 
            Curriculum_data=' '.join(get_course(i)['Curriculum_data'])
            Learn=' '.join(get_course(i)['Learn'])
            Requirements=' '.join(get_course(i)['Requirements'])
            data_tuple=(CourseName,Description,Language,Pricing,Curriculum_data,Learn,Requirements)
            sql="INSERT INTO course_collection  (Course_title  ,Description  ,Language ,Pricing ,Curriculum_data ,Learn ,Requirements   ) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            #mycursor.execute("Insert Into course_collection (Course_title  ,Description  ,Language ,Pricing ,Curriculum_data ,Learn ,Requirements   ) VALUES (%s,%s,%s,%s,%s,%s,%s) " .format( CourseName,Description,Language,Pricing,Curriculum_data,Learn,Requirements))
            mycursor.execute(sql, data_tuple)
            mydb.commit()
            if(count>=100):
                break
                    
    except Exception as e:
        logging.error("error in SQL DB insertion", e)

