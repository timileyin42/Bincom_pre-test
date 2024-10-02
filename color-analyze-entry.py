from color_extract import extract_color_data
from stats_calculation import get_color_stats
from database import save_to_db
from collections import Counter

def main():
    # Extract color data
    all_colors = extract_color_data()

    # Calculate statistics
    mean_color, median_color, variance, prob_red = get_color_stats(all_colors)
    print(f"Mean Color: {mean_color}")
    print(f"Median Color: {median_color}")
    print(f"Variance: {variance}")
    print(f"Probability of Red: {prob_red}")

    # Save to PostgreSQL
    color_counter = Counter(all_colors)
    save_to_db(color_counter)

if __name__ == "__main__":
    main()

