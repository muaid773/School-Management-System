def rafing(array : list):
    """
    دالة تقوم باخذ مصفوفه ةتزيل العناصر المكررة
    """
    newarray = []
    for value in array:
        if not value in newarray:
            newarray.append(value)
    return newarray


def stariting(main_array : list, array : list, emptyvalue: str):
    """
    تقوم هذه التالد ب عمل تقويم لقاىمة استنادا على القاىمة الي تتم المقارنة بها
    حيث كل عنصر في القاىمة الثانية سيتم جعل رقم الفهرس مساويا لرقم الفهرس في
    القاىمة الاولى ويستم تعويض الفراغات بقيمه افتراضيه تحدد وتمرر لدالة\n
    مثال:
        **main_array = [1, 2, 3, 4, 5, 6]** 
            <p>.القاىمة الاول التي سيم المقارنه بها\n
        **array = [1,3,6]**
            <p>هذه القاىمة هي التي سيتم سد فراغاتها بقيمه افتراضية</p>\n
        **resualt = [1, -, 3, -, -, 6]** . هذه هي النتيجه\n
            حيث ان الشرطه ستكون القيمه الافتراضية التي تسد بها الغراغات\n
        وبهذا كل عنصر في القالىمة الثانية مقابل لكل عنصر في القاىمة الأولى\n
    """
    for grade in array:
        try:
            if grade.month.name in main_array:
                index = main_array.index(grade.month.name)
                index2 = array.index(grade)

                if index > index2:
                    fullindex = index - index2
                    for _ in range(fullindex):
                        array.insert(index2, emptyvalue)
        except:
            pass
    return array
