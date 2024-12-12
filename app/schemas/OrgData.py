from pydantic import BaseModel


class OrgData(BaseModel):
    rubrics: str
    name_org: str
    org_address: str
    rating: int
 