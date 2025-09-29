import argparse
from data_ingestion import load_activity_log
from workout_recommender import recommend_workout
from meal_recommender import recommend_meal

def pretty_print_suggestion(date, workout, meal):
    print(f"\n=== Suggestions for {date} ===")
    print(f"Workout readiness: {workout['label']}")
    print(f"Recommendation: {workout['recommendation']}")
    print("Plan:")
    for step in workout['plan']:
        print(f" - {step}")
    print("\nNutrition suggestion:")
    print(f" - Calorie delta (kcal): {meal['calorie_delta']}")
    print(f" - Protein (g): {meal['macros']['protein_g']}")
    print(f" - Sample meal: {meal['sample_meal']}")
    print("==============================\n")

def run_demo(input_path):
    records = load_activity_log(input_path)
    user_profile = {'goal': 'maintain', 'weight_kg': 78, 'protein_g_per_kg': 1.8}
    for rec in records:
        workout = recommend_workout(rec)
        meal = recommend_meal(rec, user_profile=user_profile)
        pretty_print_suggestion(rec.get('date','unknown'), workout, meal)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AI Fitness Coach Demo')
    parser.add_argument('--input', type=str, default='sample_data.json', help='path to input json')
    args = parser.parse_args()
    run_demo(args.input)
