# from flask import Flask, render_template, request, redirect
# import pandas as pd
# import os

# app = Flask(__name__)

# # Storage for attendance (in-memory)
# attendance_list = []

# @app.route("/", methods=["GET", "POST"])
# def attendance():
#     global attendance_list
#     if request.method == "POST":
#         roll = request.form["roll"]
#         name = request.form["name"]
#         year = request.form["year"]
#         dept = request.form["DEPERTMENT"]

#         # Save the data
#         attendance_list.append({"Roll": roll, "Name": name, "Year": year, "Department": dept})

#         # Sort by Roll Number
#         attendance_list = sorted(attendance_list, key=lambda x: x["Roll"])
#         # Save to Excel
#         df = pd.DataFrame(attendance_list)
#         df.index += 1   # Serial Numbers
#         df.to_excel("attendance.xlsx", index_label="Serial No.")

#         return redirect("/")  # Refresh page

#     return render_template("index.html")  # Your HTML file (form.html)


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0")

from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__)

# Storage for attendance (in-memory)
attendance_list = []

@app.route("/", methods=["GET", "POST"])
def attendance():
    global attendance_list
    if request.method == "POST":
        roll = request.form["roll"]
        name = request.form["name"]
        year = request.form["year"]
        dept = request.form["DEPERTMENT"]

        # Save the data
        attendance_list.append({"Roll": roll, "Name": name, "Year": year, "Department": dept})

        # Sort by Roll Number
        attendance_list = sorted(attendance_list, key=lambda x: x["Roll"])

        # Save to Excel
        df = pd.DataFrame(attendance_list)
        df.index += 1   # Serial Numbers
        df.to_excel("attendance.xlsx", index_label="Serial No.")

        return redirect("/")  # Refresh page

    return render_template("index.html")  # Your HTML file (form.html)


if __name__ == "__main__":
    app.run(debug=True)