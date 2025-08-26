from pydantic import BaseModel #To Import BaseModel from Pydantic for request validation

class DomainRequest(BaseModel): # To Define request model with domain field
    domain: str # To Domain name to be analyzed
