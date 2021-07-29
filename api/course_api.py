import fastapi
from fastapi.responses import JSONResponse
from fastapi import Depends
from services.db_service import get_one_course, all_courses

from models.course import Course

router = fastapi.APIRouter()

@router.get('/api/rec/{course_id}')
def rec(crs: Course = Depends()):
    result = get_one_course(crs.course_id)
    if result is None:
        return JSONResponse(content={"Result": f"THis course {crs.course_id} is not not foud"}, status_code=200)
    else:
        return JSONResponse(content={"Result" :{"course_id":result.course_id,
                                        "title":result.title,
                                        "speciality":result.speciality    
        }}, status_code=200)


@router.get('/api/rec/')
def rec_all():
    return JSONResponse( content={"Results":all_courses()} , status_code=200)