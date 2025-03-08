from flask import Blueprint, jsonify
from .scraper import scrape_jobs

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def home():
  return jsonify({"message": "Job Scraper API is running!"})

@main.route("/jobs", methods=["GET"])
def get_jobs():
  jobs = scrape_jobs()
  return jsonify(jobs)
                  