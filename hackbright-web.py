from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    page = hackbright.get_grades_by_github(github)

    return page


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add-confirm", methods=['POST'])
def add_student():
    """Add student to database and confirmation message for user."""

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')

    hackbright.make_new_student(first, last, github)

    return render_template("student_add_confirm.html",
                            github=github)


@app.route("/student-add")
def add_student_form():
    """Show form for adding a new student."""

    return render_template("student_add.html")


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
