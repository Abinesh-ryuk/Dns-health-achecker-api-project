# I added inline comments to all modules to reflect full understanding of project
# main.py — Entry point for the FastAPI application
# This module defines the API endpoints for starting and retrieving DNS analysis

from fastapi import FastAPI, HTTPException # TO Import FastAPI and HTTPException for building API and error handling
from app.models import DomainRequest # To Import request model for domain input
from app.database import collection # TO Import MongoDB collection object
from app.analyzer import run_dns_analysis # To Import DNS analysis logic
from bson import ObjectId # To Import ObjectId to query MongoDB documents by ID

# Initialize FastAPI app
app = FastAPI()

# To define POST endpoint to start DNS analysis
# Accepts a domain name, runs analysis, stores result in MongoDB, and returns analysis ID
@app.post("/start-analysis")
def start_analysis(request: DomainRequest):
    result = run_dns_analysis(request.domain) # Run DNS analysis on the provided domain
    analysis = {"domain": request.domain, "result": result}  # Prepare document to insert into MongoDB
    inserted = collection.insert_one(analysis) # # Insert document and get inserted ID
    return {"analysis_id": str(inserted.inserted_id)} # Return analysis ID to the user

# Define GET endpoint to retrieve analysis result by ID
@app.get("/get-analysis/{analysis_id}")
def get_analysis(analysis_id: str):
    analysis = collection.find_one({"_id": ObjectId(analysis_id)})# Find document in MongoDB using ObjectId
    if not analysis: # If not found, raise 404 error
        raise HTTPException(status_code=404, detail="Analysis not found")
    return {"domain": analysis["domain"], "result": analysis["result"]}# Return domain and result from the document
