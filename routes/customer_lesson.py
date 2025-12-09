from flask import render_template

def customer_lesson_route(db, request):
    results = None

    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        date = request.form.get('date')

        cursor = db.cursor(dictionary=True)
        query = """
        SELECT 
            M.name AS mountain_name,
            L.date
        FROM Lesson L
        JOIN GroupCustomer GC ON L.groupId = GC.groupId
        JOIN Customer CU ON GC.customerId = CU.id
        JOIN Mountain M ON L.mountainId = M.id
        WHERE CU.firstName = %s AND CU.lastName = %s
        """
        params = [first_name, last_name]

        if date:
            query += " AND L.date = %s"
            params.append(date)

        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()

    return render_template("customer_lesson.html", results=results)
