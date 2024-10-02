from collections import Counter
import numpy as np

def get_color_stats(all_colors):
    color_counter = Counter(all_colors)

    # Mean (most common color)
    mean_color = color_counter.most_common(1)[0][0]

    # Median color
    sorted_colors = sorted(all_colors)
    median_color = sorted_colors[len(sorted_colors) // 2]

    # Variance of color occurrences
    color_counts = list(color_counter.values())
    variance = np.var(color_counts)

    # Probability of red
    prob_red = color_counter['RED'] / len(all_colors)

    return mean_color, median_color, variance, prob_red

# For debugging or running separately
if __name__ == "__main__":
    from color_data_extractor import extract_color_data

    all_colors = extract_color_data()
    mean_color, median_color, variance, prob_red = get_color_stats(all_colors)
    
    print("Mean Color:", mean_color)
    print("Median Color:", median_color)
    print("Variance:", variance)
    print("Probability of Red:", prob_red)

