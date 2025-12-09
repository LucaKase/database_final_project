from flask import render_template

def customers_by_nationality_route(db):
    cursor = db.cursor(dictionary=True)
    query = """
        SELECT nationality, COUNT(*) AS number_of_customers
        FROM Customer
        GROUP BY nationality
        ORDER BY number_of_customers DESC;
    """

    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()

    return render_template("customer_by_nationality.html", results=results)
