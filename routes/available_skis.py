from flask import render_template

def available_skis_route(db, request):
    result = None

    if request.method == 'POST':
        date = request.form.get('date')

        cursor = db.cursor(dictionary=True)
        query = """
        SELECT COUNT(*) AS available_skis
        FROM Ski S
        JOIN Equipment E ON S.id = E.id
        WHERE NOT EXISTS (
            SELECT 1
            FROM RentalItem RI
            JOIN Rent R ON RI.rentId = R.id
            WHERE RI.equipmentId = E.id
              AND R.date = %s
        );
        """
        cursor.execute(query, (date,))
        result = cursor.fetchone()
        cursor.close()

    return render_template("available_ski.html", result=result)
