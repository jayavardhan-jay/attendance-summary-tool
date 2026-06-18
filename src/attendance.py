def summarize_attendance(records):
    present_count = sum(records)
    total_count = len(records)

    attendance_percentage = (present_count / total_count) * 100

    return {
        "total": total_count,
        "present": present_count,
        "attendance_percentage": attendance_percentage,
        "eligible": attendance_percentage >= 75
    }
