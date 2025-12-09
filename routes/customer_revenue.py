from flask import render_template

def customer_revenue_route(db, request):
    result = None
    first_name = None
    last_name = None

    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')

        cursor = db.cursor(dictionary=True)
        query = """
        SELECT SUM(L.pricePerPerson) AS total_revenue
        FROM Lesson L
        JOIN GroupCustomer GC ON L.groupId = GC.groupId
        JOIN Customer C ON GC.customerId = C.id
        WHERE C.firstName = %s AND C.lastName = %s;
        """
        cursor.execute(query, (first_name, last_name))
        result = cursor.fetchone()
        cursor.close()

    return render_template("customer_revenue.html", result=result, first_name=first_name, last_name=last_name)
