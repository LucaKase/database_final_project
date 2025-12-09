from flask import render_template

def lesson_conditions_route(db, request):
    results = None

    if request.method == 'POST':
        date = request.form.get('date')

        cursor = db.cursor(dictionary=True)
        query = """
        SELECT DISTINCT C.weatherCondition, C.snowCondition
        FROM Lesson L
        JOIN Conditions C ON L.conditionId = C.id
        WHERE L.date = %s
        """
        cursor.execute(query, (date,))
        results = cursor.fetchall()
        cursor.close()

    return render_template("lessons_conditions.html", results=results)
