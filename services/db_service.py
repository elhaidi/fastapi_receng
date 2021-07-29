
from models.course import Course
from typing import List, Tuple

DB_DUMP: List[Course] = [
    Course(course_id =1, title ="Pain Medicine Management: Pain Management of the Lower Back", speciality ="Family Practice"),
    Course(course_id =2, title ="eCysticFibrosis Review:Vol 5 Issue 12: Non-pulmonary CFTR", speciality ="Internal Medicine"),
    Course(course_id =3, title =" eNeonatal Review Vol10,", speciality ="Nursing"),
    Course(course_id =4, title ="Addressing the Challenges of HPV Vaccination: Clinical Dialogue", speciality ="Pediatrics"),
    Course(course_id =5, title ="eCysticFibrosis Review:Vol 5 ", speciality ="Internal Medicine"),
    Course(course_id =6, title ="Gastrointestinal and Liver Pathology", speciality ="Gastroenterology, Hematology"),
    Course(course_id =7, title ="Pain Medicine Management: The Treatment of Opioid Dependence", speciality ="Internal Medicine"),
    Course(course_id =8, title ="title 1 of the pre", speciality="Physician Assistant"),
    Course(course_id =9, title ="Addressing the Challenges of HPV Vaccination: eCase Challenge", speciality ="Infectious Diseases"),
    Course(course_id =10,title = "Body CT:  Back to Basics and Beyond - VASCULAR", speciality ="Radiologic Tech, Radiology"),
   
]

def get_one_course(id: int) -> Course:
    for crs in DB_DUMP:
        if crs.course_id == id:
            return crs
    
    return None

def all_courses() -> List[Course]:
    return   [crs.dict() for crs in DB_DUMP]