import json
from datetime import datetime

filename = "study_data.json"

def save(data):
    f = open(filename, "w")
    json.dump(data, f, indent=4)
    f.close()

def load():
    try:
        f = open(filename, "r")
        data = json.load(f)
        f.close()
        return data
    except:
        return {"student": {}, "subjects": [], "sessions": [], "tests": []}

def profile(data):
    print("\nStudent Profile")
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    semester = input("Enter semester: ")
    college = input("Enter college: ")
    data["student"] = {
        "name": name,
        "branch": branch,
        "semester": semester,
        "college": college
    }
    save(data)
    print("Profile saved successfuly")

def show_profile(data):
    if len(data["student"]) == 0:
        print("\nNo profile found.")
    else:
        print("\nName:", data["student"]["name"])
        print("Branch:", data["student"]["branch"])
        print("Semester:", data["student"]["semester"])
        print("College:", data["student"]["college"])

def add_subject(data):
    print("\nAdd Subject")
    name = input("Subject name: ")
    marks = float(input("Current marks: "))
    if marks >= 90:
     print("Very good marks")
    elif marks >= 75:
     print("Good marks")
    else:
     print("More practice needed")
    difficulty = int(input("Difficulty from 1 to 5: "))
    confidence = int(input("Confidence from 1 to 5: "))
    days = int(input("Days left for exam: "))
    syllabus = float(input("Syllabus completed (%): "))
    subject = {
        "name": name,
        "marks": marks,
        "difficulty": difficulty,
        "confidence": confidence,
        "days": days,
        "syllabus": syllabus
    }
    data["subjects"].append(subject)
    save(data)
    print("Subject added.")

def show_subjects(data):
    if len(data["subjects"]) == 0:
        print("\nNo subjects added.")
        return
    print("\nSubjects")
    for s in data["subjects"]:
        print(s["name"], "| Marks:", s["marks"], "% | Difficulty:", s["difficulty"], "| Confidence:", s["confidence"], "| Days:", s["days"])

def find_subject(data, name):
    for s in data["subjects"]:
        if s["name"].lower() == name.lower():
            return s
    return None

def update_subject(data):
    show_subjects(data)
    name = input("\nEnter subject to update: ")
    s = find_subject(data, name)
    if s == None:
        print("Subject not found.")
        return
    s["marks"] = float(input("New marks: "))
    s["difficulty"] = int(input("New difficulty: "))
    s["confidence"] = int(input("New confidence: "))
    s["days"] = int(input("New days left: "))
    s["syllabus"] = float(input("New syllabus %: "))
    save(data)
    print("Subject updated.")

def delete_subject(data):
    show_subjects(data)
    name = input("\nEnter subject to delete: ")
    s = find_subject(data, name)
    if s == None:
        print("Subject not found.")
        return
    data["subjects"].remove(s)
    save(data)
    print("Subject deleted.")

def priority(s):
    weak = 100 - s["marks"]
    difficult = s["difficulty"] * 10
    low_confidence = (6 - s["confidence"]) * 10
    exam_near = 0
    if s["days"] <= 7:
        exam_near = 30
    elif s["days"] <= 15:
        exam_near = 20
    elif s["days"] <= 30:
        exam_near = 10
    syllabus_left = 100 - s["syllabus"]
    score = weak + difficult + low_confidence + exam_near + syllabus_left
    return score

def study_plan(data):
    if len(data["subjects"]) == 0:
        print("\nAdd subjects first.")
        return
    minutes = int(input("\nHow many minutes can you study today? "))
    total = 0
    for s in data["subjects"]:
        total = total + priority(s)
    print("\nStudy Plan")
    for s in data["subjects"]:
        p = priority(s)
        if total == 0:
            time = 0
        else:
            time = int(minutes * p / total)
        print(s["name"], "->", time, "minutes", "| Priority:", p)

def show_priority(data):
    show_subjects(data)
    name = input("\nEnter subject: ")
    s = find_subject(data, name)
    if s == None:
        print("Subject not found.")
        return
    p = priority(s)
    print("\nSubject:", s["name"])
    print("Priority score:", p)
    if p >= 200:
        print("Priority: Very High")
    elif p >= 150:
        print("Priority: High")
    elif p >= 100:
        print("Priority: Medium")
    else:
        print("Priority: Low")

def add_session(data):
    show_subjects(data)
    name = input("\nSubject studied: ")
    s = find_subject(data, name)
    if s == None:
        print("Subject not found.")
        return
    minutes = int(input("Minutes studied: "))
    topic = input("Topic studied: ")
    session = {
        "date": datetime.now().strftime("%d-%m-%Y"),
        "subject": s["name"],
        "minutes": minutes,
        "topic": topic
    }
    data["sessions"].append(session)
    save(data)
    print("Study session saved.")

def study_history(data):
    if len(data["sessions"]) == 0:
        print("\nNo study sessions yet.")
        return
    print("\nStudy History")
    total = 0
    for s in data["sessions"]:
        print(s["date"], "|", s["subject"], "|", s["minutes"], "minutes |", s["topic"])
        total = total + s["minutes"]
    print("Total study time:", total, "minutes")

def add_test(data):
    show_subjects(data)
    name = input("\nSubject: ")
    s = find_subject(data, name)
    if s == None:
        print("Subject not found.")
        return
    test = input("Test name: ")
    marks = float(input("Marks obtained: "))
    result = {
        "date": datetime.now().strftime("%d-%m-%Y"),
        "subject": s["name"],
        "test": test,
        "marks": marks
    }
    data["tests"].append(result)
    save(data)
    print("Test result saved.")

def show_tests(data):
    if len(data["tests"]) == 0:
        print("\nNo test results.")
        return
    print("\nTest Results")
    for t in data["tests"]:
        print(t["date"], "|", t["subject"], "|", t["test"], "|", t["marks"], "%")

def performance(data):
    if len(data["subjects"]) == 0:
        print("\nNo subjects.")
        return
    print("\nPerformance")
    for s in data["subjects"]:
        total = 0
        count = 0
        for t in data["tests"]:
            if t["subject"].lower() == s["name"].lower():
                total = total + t["marks"]
                count = count + 1
        print("\n", s["name"])
        print("Current marks:", s["marks"], "%")
        if count > 0:
            print("Test average:", round(total / count, 2), "%")
        else:
            print("No tests recorded.")

def progress(data):
    print("\nMy Progress")
    print("Subjects:", len(data["subjects"]))
    print("Study sessions:", len(data["sessions"]))
    print("Tests:", len(data["tests"]))
    total = 0
    for s in data["sessions"]:
        total = total + s["minutes"]
    print("Total study time:", total, "minutes")
    if len(data["sessions"]) > 0:
        print("Average session:", round(total / len(data["sessions"]), 2), "minutes")

def menu():
    print("\nSMART STUDY TIME RECOMMENDATION SYSTEM")
    print("1. student Profile")
    print("2. Add New Subject")
    print("3. Show Subjects")
    print("4. Update Subject")
    print("5. Delete Subject")
    print("6. Study Priority")
    print("7. Study Plan")
    print("8. Add Study Session")
    print("9. Study History")
    print("10. Add Test")
    print("11. View Tests")
    print("12. Performance")
    print("13. Progress")
    print("0. Exit")

data = load()

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        profile(data)
        show_profile(data)
    elif choice == "2":
        add_subject(data)
    elif choice == "3":
        show_subjects(data)
    elif choice == "4":
        update_subject(data)
    elif choice == "5":
        delete_subject(data)
    elif choice == "6":
        show_priority(data)
    elif choice == "7":
        study_plan(data)
    elif choice == "8":
        add_session(data)
    elif choice == "9":
        study_history(data)
    elif choice == "10":
        add_test(data)
    elif choice == "11":
        show_tests(data)
    elif choice == "12":
        performance(data)
    elif choice == "13":
        progress(data)
    elif choice == "0":
        save(data)
        print("Program closed.")
        break
    else:
        print("Wrong choice.")