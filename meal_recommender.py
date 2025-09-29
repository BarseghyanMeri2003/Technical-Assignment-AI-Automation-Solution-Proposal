from typing import Dict

def estimate_calorie_adjustment(record: Dict, user_goal: str = 'maintain') -> Dict:
    burned = record.get('calories_burned', 0)
    if user_goal == 'loss':
        if burned > 600:
            delta = -100
        elif burned > 350:
            delta = 0
        else:
            delta = -250
    elif user_goal == 'gain':
        if burned > 600:
            delta = +400
        elif burned > 350:
            delta = +200
        else:
            delta = +300
    else:  # maintain
        if burned > 600:
            delta = +200
        elif burned > 350:
            delta = +100
        else:
            delta = 0
    return {'target_delta_kcal': delta}

def recommend_meal(record: Dict, user_profile: Dict = None) -> Dict:
    user_profile = user_profile or {}
    goal = user_profile.get('goal', 'maintain')
    adjustment = estimate_calorie_adjustment(record, user_goal=goal)
    protein_g_per_kg = user_profile.get('protein_g_per_kg', 1.6)
    weight_kg = user_profile.get('weight_kg', 70)
    protein_total = round(protein_g_per_kg * weight_kg)
    return {
        'calorie_delta': adjustment['target_delta_kcal'],
        'macros': {
            'protein_g': protein_total,
            'carbs_g': 40,
            'fat_g': 25
        },
        'sample_meal': 'Grilled chicken, quinoa, mixed vegetables'
    }
