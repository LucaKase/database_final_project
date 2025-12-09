from flask import render_template

def update_salary_route(db, request):
    message = None

    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        new_salary = request.form.get('salary')

        cursor = db.cursor()
        query = """
        UPDATE Instructors
        SET salary = %s
        WHERE firstName = %s AND lastName = %s
        """
        cursor.execute(query, (new_salary, first_name, last_name))
        db.commit()
        cursor.close()

    return render_template("update_salary.html", message=message)
