def rafing(array : list):
    """
    دالة تقوم باخذ مصفوفه ةتزيل العناصر المكررة
    """
    newarray = []
    for value in array:
        if not value in newarray:
            newarray.append(value)
    return newarray


def stariting(main_array: list, array: list, emptyvalue: str = "-"):
    """
    تقوم هذه الدالة بمحاذاة قائمة استنادًا إلى قائمة مرجعية.
    بحيث يتم ترتيب عناصر القائمة الثانية بنفس ترتيب القائمة الأولى،
    وسدّ الفجوات بقيمة افتراضية.

    مثال:
        main_array = [1, 2, 3, 4, 5, 6]
        array = [1, 3, 6]
        الناتج => [1, -, 3, -, -, 6]
    """
    # أول عنصر عادة الطالب نفسه
    student = array[0]
    grades = array[1:]

    aligned_row = [student]

    # ترتيب القيم حسب main_array
    for item in main_array:
        found = None
        for grade in grades:
            if hasattr(grade, 'month') and grade.month.name == item:
                found = grade
                break
        aligned_row.append(found if found else emptyvalue)

    return aligned_row