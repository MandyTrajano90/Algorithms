def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    if not permanence_period or any(
        not isinstance(start, int) or not isinstance(end, int) or end < start
        for start, end in permanence_period
    ):
        return None

    present_students = sum(
        1 for start, end in permanence_period if start <= target_time <= end
    )
    return present_students
