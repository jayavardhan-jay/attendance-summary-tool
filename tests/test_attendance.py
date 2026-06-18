from src.attendance import summarize_attendance

def test_summarize_attendance():
    result = summarize_attendance([True, True, False, True])
    assert result["total"] == 4
    assert result["present"] == 3
    assert result["attendance_percentage"] == 75
    assert result["eligible"] is True
