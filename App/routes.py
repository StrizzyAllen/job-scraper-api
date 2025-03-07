from flask import Blueprint, jsonify
main = Blueprint("main", __name__)
@main.route("/", methods=["GET"])
def home():
  return jsonify({"message: "Job Scraper API is running!"}) 
