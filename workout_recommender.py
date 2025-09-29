from typing import Dict

def readiness_label(record: Dict) -> str:
    """Simple heuristic for readiness: 'ready', 'caution', 'rest'."""
    hr = record.get('resting_heart_rate', None)
    sleep = record.get('hours_slept', None)
    steps = record.get('steps', 0)

    if sleep is None or hr is None:
        return 'caution'
    if sleep < 5 or hr >= 70:
        return 'rest'
    if sleep < 6 or hr >= 60:
        return 'caution'
    if steps > 10000 and sleep >= 7:
        return 'ready'
    return 'caution'

def recommend_workout(record: Dict) -> Dict:
    """Return a workout recommendation based on readiness and previous activity."""
    label = readiness_label(record)
    workout_history = record.get('workout', {}) or {}
    last_type = workout_history.get('type', 'none')

    if label == 'rest':
        return {
            'label': label,
            'recommendation': 'Rest or active recovery (easy walk, mobility).',
            'plan': ['20-30 min easy walk', '10 min mobility/stretching']
        }
    elif label == 'caution':
        if last_type in ['strength', 'run'] and workout_history.get('duration_min',0) >= 45:
            return {
                'label': label,
                'recommendation': 'Light recovery session.',
                'plan': ['20 min cycling or brisk walking', '10 min foam rolling']
            }
        else:
            return {
                'label': label,
                'recommendation': 'Moderate session focusing on technique and tempo.',
                'plan': ['30 min mixed cardio', '15 min mobility']
            }
    else:  # ready
        return {
            'label': label,
            'recommendation': 'Full training session: strength or interval cardio.',
            'plan': ['Warm-up 10 min', '30-40 min strength or intervals', 'Cooldown 10 min']
        }
