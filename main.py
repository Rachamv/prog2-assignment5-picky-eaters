from collections import Counter

def create_meal_frequencies(preferences):
    meal_frequencies = Counter()

    for meals in preferences.values():
        meal_frequencies.update(meals)

    return meal_frequencies

def create_user_scores(preferences, meal_frequencies):
    user_scores = {person: sum(meal_frequencies[meal] for meal in meals) for person, meals in preferences.items()}

    return user_scores

def find_users_with_lowest_score(user_scores):
    min_score = min(user_scores.values())
    lowest_score_users = [user for user, score in user_scores.items() if score == min_score]

    return lowest_score_users

if __name__ == '__main__':
    preferences = {
        'a': {'pizza', 'goat meat', 'shortbread'},
        'b': {'pizza', 'shrimp', 'tea'},
        'c': {'pizza', 'nutella', 'dumplings'},
    }

    meal_score = create_meal_frequencies(preferences)
    print(f'{meal_score}')
    user_score = create_user_scores(preferences, meal_score)
    print(f'{user_score}')

    print(find_users_with_lowest_score(user_score))