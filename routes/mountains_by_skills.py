from flask import render_template

def mountains_by_skill_route(db, request):
    results = None
    skill_levels = ['Beginner', 'Intermediate', 'Advanced']

    if request.method == 'POST':
        selected_skill = request.form.get('skillLevel')

        cursor = db.cursor(dictionary=True)
        query = """
        SELECT M.name, M.height, SL.description AS skill_level
        FROM Mountain M
        JOIN SkillLevel SL ON M.skillId = SL.id
        WHERE SL.description = %s
        """
        cursor.execute(query, (selected_skill,))
        results = cursor.fetchall()
        cursor.close()

    return render_template("mountains_by_skills.html", results=results, skill_levels=skill_levels)
