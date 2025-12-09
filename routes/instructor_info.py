from flask import render_template

def instructor_info_route(db, request):
    result = None

    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')

        cursor = db.cursor(dictionary=True)
        query = """
        SELECT 
            firstName,
            lastName,
            salary,
            yearsExperience
        FROM Instructors
        WHERE firstName = %s AND lastName = %s;
        """

        cursor.execute(query, (first_name, last_name))
        result = cursor.fetchall()
        cursor.close()

    return render_template("instructor_info.html", result=result)
