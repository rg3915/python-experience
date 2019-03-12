from typing import Dict


def weekday(day: int) -> Dict[str, str]:
    if day == 1:
        return {'day': 'sunday'}
    else:
        return {}
