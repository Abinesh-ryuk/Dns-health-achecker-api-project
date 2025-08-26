# DNS Health Checker API Project
 
 This project was assigned to me as part of a technical interview, and I approached it with full ownership—from setting up the environment to delivering a working backend system. The DNS Health Checker API is a FastAPI-based application that analyzes the DNS health of any domain name and stores the results in MongoDB. It provides two endpoints: one to start the analysis and another to retrieve the result using a unique ID.

I built this project line by line, debugged every issue, and verified every result using Swagger UI and MongoDB Compass. This README reflects my understanding and the steps I followed to complete the task within 24 hours—well ahead of the 48-hour deadline.

Built from Scratch by Abinesh T



## Tech stack
**Python** – Core language used for backend development
- **FastAPI** – Lightweight and fast web framework for building APIs
- **MongoDB** – NoSQL database for storing DNS analysis results
- **dnspython** – Python library for DNS record analysis
- **Swagger UI** – Auto-generated API documentation and testing interface
- **VS Code** – Development environment
- **Git & GitHub** – Version control and commit history
- **MongoDB Compass** – GUI for verifying stored data


## Project Structure

<img width="1024" height="1536" alt="dns project structure img" src="https://github.com/user-attachments/assets/e31972b0-c564-4ba6-8d10-00b3ea89ee85" />

## Screen shots
- Swagger UI — Testing Endpoints
<img width="1920" height="1020" alt="Screenshot 2025-08-26 123252" src="https://github.com/user-attachments/assets/48ddbffc-1683-46d2-a98f-17f125eeccff" />

 <img width="1920" height="1020" alt="Screenshot 2025-08-26 123300" src="https://github.com/user-attachments/assets/3de88886-f67f-4369-9998-440d22a4c6b0" />

<img width="1920" height="1020" alt="Screenshot 2025-08-26 124345" src="https://github.com/user-attachments/assets/2e307eda-cb1d-4bd9-b507-47c0028b143e" />

 <img width="1920" height="1020" alt="Screenshot 2025-08-26 131512" src="https://github.com/user-attachments/assets/0e721dc5-3563-4cf0-9442-f5c2e6ba6661" />
<img width="1920" height="1020" alt="Screenshot 2025-08-26 131515" src="https://github.com/user-attachments/assets/3bacec2e-d306-4998-85ea-a57886aafa01" />
<img width="1920" height="1020" alt="Screenshot 2025-08-26 131554" src="https://github.com/user-attachments/assets/b45d2df7-d293-481d-88b7-7036950fdcb7" />
<img width="1920" height="1020" alt="Screenshot 2025-08-26 131558" src="https://github.com/user-attachments/assets/67dc07b7-9904-490a-a13c-ea1a888fd00e" />

- MongoDB Compass — Stored DNS Result
<img width="1920" height="1020" alt="Screenshot 2025-08-26 132223" src="https://github.com/user-attachments/assets/15e5ff39-f1ad-4ce2-b296-2a8a38c2d92a" />


## API usage
- Start DNS Analysis
POST /start-analysis
{
  "domain": "google.com"
}

## Response:
{
  "domain": "google.com",
  "result": {
    "MX": "ASPMX.L.GOOGLE.COM",
    "score": 100
  }
}
## Screen shots
- Swagger UI — Testing Endpoints
<img width="1920" height="1020" alt="Screenshot 2025-08-26 123252" src="https://github.com/user-attachments/assets/48ddbffc-1683-46d2-a98f-17f125eeccff" />

 <img width="1920" height="1020" alt="Screenshot 2025-08-26 123300" src="https://github.com/user-attachments/assets/3de88886-f67f-4369-9998-440d22a4c6b0" />

<img width="1920" height="1020" alt="Screenshot 2025-08-26 124345" src="https://github.com/user-attachments/assets/2e307eda-cb1d-4bd9-b507-47c0028b143e" />

 <img width="1920" height="1020" alt="Screenshot 2025-08-26 131512" src="https://github.com/user-attachments/assets/0e721dc5-3563-4cf0-9442-f5c2e6ba6661" />
<img width="1920" height="1020" alt="Screenshot 2025-08-26 131515" src="https://github.com/user-attachments/assets/3bacec2e-d306-4998-85ea-a57886aafa01" />
<img width="1920" height="1020" alt="Screenshot 2025-08-26 131554" src="https://github.com/user-attachments/assets/b45d2df7-d293-481d-88b7-7036950fdcb7" />
<img width="1920" height="1020" alt="Screenshot 2025-08-26 131558" src="https://github.com/user-attachments/assets/67dc07b7-9904-490a-a13c-ea1a888fd00e" />

- MongoDB Compass — Stored DNS Result
<img width="1920" height="1020" alt="Screenshot 2025-08-26 132223" src="https://github.com/user-attachments/assets/15e5ff39-f1ad-4ce2-b296-2a8a38c2d92a" />


## Project Demo

https://github.com/user-attachments/assets/738e99ac-1b5e-41c3-9dbc-184065e5b70d


https://github.com/user-attachments/assets/f3a9a8f0-bee6-455d-becc-c5ab1c1c308e



https://github.com/user-attachments/assets/3a5e2c46-2025-497a-a785-80bfbbafcc16


## What I Learned

- How to build a backend API using FastAPI
- How to connect and interact with MongoDB using Python
- How to analyze DNS records programmatically
- How to handle errors and test endpoints properly
- How to structure and document a real-world project

## About me
About Me
I’m Abinesh T, a fresher with a disciplined mindset and a passion for backend development. I didn’t copy-paste this project—I understood every module, built it from scratch, and tested it thoroughly. I’m confident in my ability to learn fast, solve problems, and contribute meaningfully to a professional team.

## How to run this project
1. Clone the Repository
git clone https://github.com/yourusername/dns-health-api.git
cd dns-health-api

2. Create and Activate Virtual Environment
python -m venv venv
.\venv\Scripts\Activate.ps1   # For PowerShell

3. Install Dependencies
pip install -r requirements.txt

4. Configure MongoDB
Make sure MongoDB is running locally. Then create a  file in the root directory:
MONGO_URI=mongodb://localhost:27017
DB_NAME=dns_health

5. Run the FastAPI Server
uvicorn app.main:app --reload

6. Test the API Using Swagger UI
Open your browser and visithttp://127.0.0.1:8000/docs

You’ll see two endpoints:
• 	 — Start DNS analysis for a domain
• 	 — Retrieve the result using the analysis ID
## How to run this project
1. Clone the Repository
git clone https://github.com/yourusername/dns-health-api.git
cd dns-health-api

2. Create and Activate Virtual Environment
python -m venv venv
.\venv\Scripts\Activate.ps1   # For PowerShell

3. Install Dependencies
pip install -r requirements.txt

4. Configure MongoDB
Make sure MongoDB is running locally. Then create a  file in the root directory:
MONGO_URI=mongodb://localhost:27017
DB_NAME=dns_health

5. Run the FastAPI Server
uvicorn app.main:app --reload

6. Test the API Using Swagger UI
Open your browser and visithttp://127.0.0.1:8000/docs

You’ll see two endpoints:
• 	 — Start DNS analysis for a domain
• 	 — Retrieve the result using the analysis ID
## Note of thanks
 I like to sincerely thank Admin Prakash Sir for giving me the opportunity to attend this interview, and HR Mam for assigning this project task. I genuinely enjoyed working on it and learned a lot in the process. My first-round interview experience was also very positive—it was clear, respectful, and made me feel confident. I truly appreciated the professionalism of your office and the way the entire process was conducted. This isn’t just something I’m saying to get the job—it’s the first time I’ve felt compelled to mention it, and I mean it.
 Thankyou very much ...