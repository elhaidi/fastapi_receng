import fastapi

router = fastapi.APIRouter()

@router.get('/api/rec/')
def rec():
    return {'course' : 'Course id 1'}