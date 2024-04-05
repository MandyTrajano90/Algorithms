def student_entry(entry) -> bool:
    return (
        isinstance(entry, tuple)
        and len(entry) == 2
        and all(isinstance(i, int) for i in entry)
    )


def study_schedule(permanence_period, target_time):
    if any(
        not student_entry(entry) for entry in permanence_period
            ) or not isinstance(target_time, int):
        return None
    present_students = 0
    for student_time in permanence_period:
        if target_time in range(student_time[0], student_time[1] + 1):
            present_students += 1
    return present_students
