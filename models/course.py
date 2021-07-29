from pydantic import BaseModel
from typing import Optional

class Course(BaseModel):
    course_id : int
    title: Optional[str] = "This si the first of the  brainsurgery "
    speciality: Optional[str] = "Surgery"