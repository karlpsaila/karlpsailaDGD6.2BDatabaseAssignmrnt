# karlpsailaDGD6.2BDatabaseAssignmrnt

## Task 1: Environment Setup

in terminal to create env

py -m venv env -- 
source env\Scripts\activate



## 1.2 Installed Packages

pip install requests
pip install python-dotenv
pip install pydantic
pip install motor
pip install uvicorn
pip install fastapi


##  GitHub Repository

This project is hosted on GitHub:

https://github.com/karlpsaila/karlpsailaDGD6.2BDatabaseAssignmrnt.git -- Link to github
C:\Users\karlp\OneDrive\Documents\DGD\Year_2\Database\karlpsailaDGD6.2BDatabaseAssignmrnt  -- local save


##  Environment Variables (Mongodb)

username = 'karl'
password = '1234'
connectionString = f'mongodb+srv://{username}:{password}@cluster0.pukpg.mongodb.net/'


---

##  Running the App

Start the development server locally:

```bash
uvicorn main:app --reload
```

http://127.0.0.1:8000/docs  -- URL

---

##  Testing

Use **Postman** to test the following endpoints:

- [`POST /upload_sprite`](http://127.0.0.1:8000/upload_sprite) – Upload image files
- [`POST /upload_audio`](http://127.0.0.1:8000/upload_audio) – Upload audio files
- [`POST /player_score](http://127.0.0.1:8000/player_score)` – Submit player scores




##  Technologies Used

- FastAPI – RESTful API Framework
- MongoDB Atlas – Cloud NoSQL Database
- Postman – API Testing
- GitHub – Version Control
- GitHubDesktop – update github
---