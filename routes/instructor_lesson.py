from flask import render_template

def instructor_lesson_route(db, request):
    results = None

    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        date = request.form.get('date')

        cursor = db.cursor(dictionary=True)
        query = """
        SELECT 
            SL.description AS skill_level,
            M.name AS mountain_name,
            L.date
        FROM Lesson L
        JOIN SkillLevel SL ON L.skillId = SL.id
        JOIN Mountain M ON L.mountainId = M.id
        JOIN Instructors I ON L.instructorId = I.id
        WHERE I.firstName = %s AND I.lastName = %s
        """
        params = [first_name, last_name]

        if date:
            query += " AND L.date = %s"
            params.append(date)

        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()

    return render_template("instructor_lesson.html", results=results)
