from flask import Flask, jsonify
from color_extract import extract_color_data
from stats_calculation import get_color_stats
from database import save_to_db
from collections import Counter

app = Flask(__name__)

@app.route('/analyze', methods=['GET'])
def analyze_colors():
    # Extract color data
    all_colors = extract_color_data()

    # Calculate statistics
    mean_color, median_color, variance, prob_red = get_color_stats(all_colors)
    
    # Prepare the response data
    response_data = {
        "mean_color": mean_color,
        "median_color": median_color,
        "variance": variance,
        "probability_of_red": prob_red
    }

    # Save to PostgreSQL
    color_counter = Counter(all_colors)
    save_to_db(color_counter)

    # Return the response as JSON
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)  # Use debug=False in production

