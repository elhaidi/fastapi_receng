import fastapi
from fastapi import Depends

from models.course import Course

router = fastapi.APIRouter()

@router.get('/api/rec/{course_id}')
def rec(crs: Course = Depends()):
    return f" The course id is :{crs.course_id} ,  course title is :{crs.title} and the speciality is: {crs.speciality}"