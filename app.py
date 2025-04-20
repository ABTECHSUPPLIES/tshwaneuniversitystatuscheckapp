from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database for student records
STUDENT_RECORDS = {
    "0402080285081": {
        "student_number": "319874256",
        "id_number": "0402080285081",
        "name": "MISS PULENG SEBOKA",
        "birth_date": "08-JAN-2005",
        "courses": [
            {"year": "2025", "qualification": "DNUR20: Diploma in Nursing", "faculty": "HEALTH SCIENCES", "status": "FA: A: UNCONDITIONAL ACCEPTANCE", "choice": "1", "letter_date": "18-JAN-2025"},
            {"year": "2025", "qualification": "DBCE20: Diploma in Civil Engineering", "faculty": "ENGINEERING & BUILT ENVIRONMENT", "status": "FA: P: PROVISIONAL ACCEPTANCE", "choice": "2", "letter_date": "22-JAN-2025"},
            {"year": "2025", "qualification": "DECE20: Diploma in Early Childhood Education", "faculty": "HUMANITIES", "status": "FA: R: WAITLISTED", "choice": "3", "letter_date": "28-JAN-2025"}
        ]
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_id = request.form.get("x_idno", "").strip()
        surname = request.form.get("x_surn", "").strip()
        full_name = request.form.get("x_names", "").strip()
        birth_date = request.form.get("x_birdat", "").strip()

        student_data = STUDENT_RECORDS.get(user_id)

        if student_data:
            return redirect(url_for("status", id_number=user_id))
        elif surname and full_name and birth_date:
            return redirect(url_for("status", id_number="N/A", surname=surname, full_name=full_name, birth_date=birth_date))
        else:
            return render_template("index.html", error="Invalid details. Please try again.")

    return render_template("index.html", error=None)

@app.route("/status")
def status():
    id_number = request.args.get("id_number", "N/A")

    student_data = STUDENT_RECORDS.get(id_number, {
        "student_number": "N/A",
        "id_number": id_number,
        "name": request.args.get("full_name", "N/A"),
        "birth_date": request.args.get("birth_date", "N/A"),
        "courses": []
    })

    return render_template("status.html", student=student_data)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        action = request.form.get("action")

        if action == "add_student":
            student_number = request.form["student_number"]
            id_number = request.form["id_number"]
            name = request.form["name"]
            birth_date = request.form["birth_date"]
            STUDENT_RECORDS[id_number] = {
                "student_number": student_number,
                "id_number": id_number,
                "name": name,
                "birth_date": birth_date,
                "courses": []
            }

        elif action == "edit_student":
            id_number = request.form["id_number"]
            if id_number in STUDENT_RECORDS:
                STUDENT_RECORDS[id_number]["name"] = request.form["name"]
                STUDENT_RECORDS[id_number]["birth_date"] = request.form["birth_date"]

        elif action == "delete_student":
            id_number = request.form["id_number"]
            STUDENT_RECORDS.pop(id_number, None)

        elif action == "add_course":
            id_number = request.form["id_number"]
            if id_number in STUDENT_RECORDS:
                STUDENT_RECORDS[id_number]["courses"].append({
                    "year": request.form["year"],
                    "qualification": request.form["qualification"],
                    "faculty": request.form["faculty"],
                    "status": request.form["status"],
                    "choice": request.form["choice"],
                    "letter_date": request.form["letter_date"]
                })

        elif action == "delete_course":
            id_number = request.form["id_number"]
            course_index = int(request.form["course_index"])
            if id_number in STUDENT_RECORDS and 0 <= course_index < len(STUDENT_RECORDS[id_number]["courses"]):
                del STUDENT_RECORDS[id_number]["courses"][course_index]

    return render_template("admin.html", students=STUDENT_RECORDS)

if __name__ == "__main__":
    app.run(debug=True)
