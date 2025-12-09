from flask import render_template

def group_size_route(db, request):
    results = None

    if request.method == 'POST':
        skill_level = request.form.get('skillLevel')
        date = request.form.get('date')

        cursor = db.cursor(dictionary=True)
        query = """
        SELECT COUNT(GC.customerId) AS group_size
        FROM Lesson L
        JOIN SkillLevel SL ON L.skillId = SL.id
        JOIN GroupCustomer GC ON L.groupId = GC.groupId
        WHERE SL.description = %s
          AND L.date = %s
        """
        cursor.execute(query, (skill_level, date))
        results = cursor.fetchall()
        cursor.close()

    return render_template("group_size.html", results=results)
