from app import create_app

app = Flask(__name__)

@app.route('/')
def home():
  return{"message": "Job Scraper API is running!"}

if __name__ == "__main__":
  app.run(debug=True)
  
