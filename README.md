# AI-Based Study Time Recommendation System

A Python-based study management and recommendation system that helps students decide how much time to spend on each subject based on marks, difficulty, confidence level, syllabus completion, and days remaining for an exam.

## Project Overview

The AI-Based Study Time Recommendation System is a menu-driven Python application designed to help students organize and manage their study time.

The system collects information about subjects and calculates a priority score for each subject. Based on these priority scores and the total study time available, it recommends how many minutes should be spent on each subject.

The application also allows students to record study sessions, test results, and track their overall progress.

## Features

### Student Profile
- Store student name
- Store branch
- Store semester
- Store college

### Subject Management
- Add new subjects
- View all subjects
- Update subject information
- Delete subjects
- Store current marks
- Store difficulty level
- Store confidence level
- Store days remaining for the exam
- Store syllabus completion percentage

### Study Priority
The system calculates a priority score using:
- Current marks
- Subject difficulty
- Student confidence
- Days remaining for the exam
- Remaining syllabus

Subjects with higher priority scores require more attention.

### Study Plan
The student enters the amount of time available for studying.

The system distributes the available study time among subjects according to their priority scores.

### Study Session Tracking
Students can record:
- Subject studied
- Study duration
- Topic studied
- Date of study session

### Study History
The system displays previous study sessions and calculates total study time.

### Test Results
Students can record:
- Subject
- Test name
- Marks obtained
- Date

### Performance Tracking
The system displays:
- Current subject marks
- Average test marks
- Test performance for each subject

### Progress Tracking
The system displays:
- Number of subjects
- Number of study sessions
- Number of tests
- Total study time
- Average study session duration

## Recommendation Logic

The study priority is calculated using a rule-based scoring system.

The score considers:

- Weakness in the subject
- Subject difficulty
- Low confidence
- Exam proximity
- Remaining syllabus

The higher the priority score, the more study time the subject receives in the recommended study plan.

## Technologies Used

- Python
- JSON
- `datetime` module
- Functions
- Conditional statements
- Loops
- Lists and dictionaries
- File handling
- User input and output

## Data Storage

The application stores student information, subjects, study sessions, and test results in:

`study_data.json`

This allows the data to remain available when the program is opened again.

## How to Run

### Requirements

- Python 3.x
- VS Code or any Python-supported IDE

### Steps

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Make sure Python is installed.
4. Run:
5. Follow the menu displayed in the terminal.

## Main Menu

The program provides the following options:

1. Student Profile
2. Add New Subject
3. Show Subjects
4. Update Subject
5. Delete Subject
6. Study Priority
7. Study Plan
8. Add Study Session
9. Study History
10. Add Test
11. View Tests
12. Performance
13. Progress
0. Exit

## Future Improvements

- Add a graphical user interface (GUI)
- Add charts and visual progress reports
- Add login functionality
- Add weekly and monthly study schedules
- Store more detailed study statistics
- Add machine learning-based recommendations using historical study data
- Add reminders for upcoming exams and study sessions

## Author

Hardik

## Project Type

First Semester Python Project
