COURSE_FEES = {
    "AI202": 18000,
    "CS101": 15000,
    "IT205": 16500,
    "DS301": 20000
}


def get_course_fee(course_code: str) -> str:
    """Return the fee for a course code."""

    course_code = course_code.upper()

    if course_code in COURSE_FEES:
        return f"The fee for {course_code} is ₹{COURSE_FEES[course_code]:,}."

    return f"No fee information was found for course {course_code}."