# **Job Scraper API** 🏗️
A Flasked-based API that scrapes job postings across online sources and gives structured job data.

## 📌 **Overview**
I am building a job scraping API with Flask and BeautifulSoup. This tool will extract job postings from websites like Indeed or ZipRecruiter and store them in a PostgreSQL Database. The API provides endpoints to fetch and fliter job listings.

🔷 **Tech Stack:**\
✅ Flask (For the API)\
✅ BeautifulSoup (For web scraping)\
✅ PostgreSQL (For the Database)\
✅ Requests (For handling HTTP requests)

## 🚀 **Features**
✅ Scrapes job listings across job sites (Indeed, ZipRecruiter, etc.)\
✅ REST API endpoints to fetch job data\
✅ Filters jobs by **keyword, location, remote/hybrid, company**\
✅ Stores job data in a **PostgreSQL Database**\
✅ Handles pagination and job updates

## 📁 **Project Structure**
```plaintext
job-scraper-api/
│── app/
│   ├── __init__.py        # Initializes Flask app
│   ├── routes.py          # API routes
│   ├── scraper.py         # Web scraper logic
│── config.py              # Configuration settings
│── run.py                 # Main entry point for Flask app
│── requirements.txt       # Dependencies list
│── README.md              # Project documentation
```

## ⚡ **Hot To Run Locally**
### 1️⃣ **clone the Repository**
```bash
git clone https://github.com/StrizzyAllen/job-scraper-api
```
### 2️⃣ **Set Up a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows
```
### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```
### 4️⃣ **Run the Flask Server**
```bash
python run.py
```
### 💡 Open https://127.0.0.1:5000/ in your web browser to see the **API** running 🏃


## 📡 **API Endpoints**
```
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/` | API health check |
| `GET`  | `/jobs` | Fetch all job listings |
| `GET`  | `/jobs?keyword=developer` | Fetch jobs with a keyword filter |
| `GET`  | `/jobs?remote=true` | Fetch remote jobs only |
```

## 🛠️ **Future Improvements**
🔷 Add more jobe sites\
🔷 Add authentication for private API
access\
🔷 Optimize web scraping with async tasks

## :trollface: **Contributing**
Feel free to do a pull request if I have issues open, or you can reach out to me directly and we can work something out where you can help me with this project. If I end up scaling this, I will definetly add issues and give the easability to do pull requests.

## 📜 **License**
MIT License

## 📭 **Contact**
👤 Isaiah Strouse\
📧 isaiahstrouse66@gmail.com\
🔗 [GitHub](https://github.com/StrizzyAllen)
