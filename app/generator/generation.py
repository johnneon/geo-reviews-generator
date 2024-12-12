from fastapi import APIRouter
from app.schemas.OrgData import OrgData
from app.services.generation import generation as generation_fn
from app.services.dataconvert import dataconvert as dataconvert_fn


router = APIRouter(prefix="/generation", tags=["generation"])


@router.post("")
async def generation(request: OrgData):
    """"""

    def prepare(data):
        res = {
            'rubrics': data.rubrics,
            'name_org': data.name_org,
            'org_address': data.org_address,
            'rating': data.rating
            }
        
        return res
    
    rubrics, name_org, org_address, org_coordinates, rating = dataconvert_fn(prepare(request))
    result = generation_fn(rubrics, name_org, org_address, rating)
    print(result)
    #response_generate = {'result': result, 'org_coordinates': org_coordinates}
    #result =2
    #org_coordintes = 3
    latitude = org_coordinates.latitude
    longitude = org_coordinates.longitude
    response_generate = {'result': result, 'latitude': latitude, 'longitude': longitude}
    return response_generate