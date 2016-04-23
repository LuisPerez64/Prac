'''
Basic Database Acces Points for the Students. SQL Queries first hand, transferring to PHP 
when the time falls forward. Attempting PHP Syntax integration from now, but not too sure
if these things will work in the format provided.
'''

#Base Query for attaining the Grades for the Students, and the Courses that they have taken
#So Far.
INSERT INTO students 
(SID, name, IID, major, degreeHeld, career)
VALUES
('$_sid', '$_name', '$_iid', '$_major', '$_degreeHeld', '$_career')

#Update All in one function, for student
(UPDATE students
 SET degreeheld='$_newInput'  
 WHERE SID = '$_sid')
(UPDATE students
 SET iid='$_newInput'  
 WHERE SID = '$_sid')
(UPDATE students
 SET career='$_newInput'  
 WHERE SID = '$_sid')
(UPDATE students
 SET name='$_newInput'  
 WHERE SID = '$_sid')
(UPDATE students
 SET major='$_newInput'  
 WHERE SID = '$_sid')

# Enrollment insert, can only enroll if they meet a specific set of requirements.
#Check if Course being Added has Prereqs
(SELECT CID
 FROM (SELECT prerequisite.PCID AS pRID
 FROM courses, prerequisite
 WHERE prerequisite.CID = courses.CID AND
courses.CID = '$_CID') AS SQ1, courses
 WHERE courses.CID = pRID)
#logFRom ^^^^ is $_pRID
#If Does have Prereq
#Check if the PreReq is met if it does exist.
(SELECT grade
FROM enrollment, students
WHERE enrollment.SID = students.SID AND 
enrollment.CID = '$pRID')
#returns $_grade
#If $_grade < threshold then deny enrollment. Done on the PHP side

#If these points are not met directly, ie any of them fail, then deny enrollment
INSERT INTO enrollment
(CID, grade, SecID, semesterID, SID, yearID)
VALUES
('$_CID', '$_grade', '$_secID', '$_semID', '$_SID', '$_yearID')

#Update the grade mainly, if the student retakes. Get Year ID From Date Function 
UPDATE enrollment
SET grade='$_newGrade', yearID = '$_yearTaking', secID='$_secID', semID='$_semID' 
WHERE SID = '$_SID' AND CID = '$_CID'

'''
SUPPLEMENTARY FUNCTIONS, Mainly to facilitate User Interaction.
'''
 #Get the SID to feed to Insert 
SELECT SID
FROM students
ORDER BY SID DESC
LIMIT 1;

 #IID To keep it fair, do the same thing
SELECT IID, COUNT(DISTINCT SID)
FROM students
GROUP BY IID
LIMIT 1;

# Get the grades that have been attained by a specific student. Used in GPA validation
(SELECT grade 
FROM students, enrollment
WHERE students.SID = enrollment.SID AND students.SID = '$_sid'
GROUP BY grade, CID)

# Also to test if theres any grades below a B. Another Requirement, returns count for a given
# student.
(SELECT COUNT(*)
 FROM 
 (SELECT name, grade   
  FROM students, enrollment
  WHERE students.SID = enrollment.SID AND 
  students.SID = '$_sid' AND 
 (grade <> 'A' AND grade <> 'A-' AND grade <> 'B+'
    AND grade <> 'B')
GROUP BY name, grade, CID) AS output)


'''
Begin DB Graduation Query
'''

#Attain the total courses that a given student has taken, to discern if they
# have at least taken the courses needed to push foward on the course grouping.

(SELECT students.name, enrollment.grade, courses.groupID
 FROM students, enrollment, courses
  WHERE students.SID = enrollment.SID AND courses.CID = enrollment.CID
  GROUP BY students.name, courses.groupID)

#SUBQUERIES:
#Condition One: Have at least 30 totalCredits
 (SELECT students.name, SUM(courses.credits) as totalCredits
  FROM students, enrollment, courses
    WHERE students.SID = enrollment.SID AND courses.CID = enrollment.CID
      GROUP BY students.name)

      
#Conditon Two: Earn 12 Credits from core courses
#Produces the SID of all the students who ha ve taken the four core courses,
 (SELECT SQ1.SID 
 FROM 
 (SELECT students.SID as SID, COUNT(DISTINCT courses.groupID) as coreTaken
    FROM students, enrollment, courses
    WHERE courses.CID = enrollment.CID AND enrollment.SID = students.SID AND
    (courses.groupID <> 0 AND courses.groupID <> 1)
    GROUP BY students.SID) AS SQ1, 
 (SELECT students.name as name, students.SID as SID
    FROM students, courses, enrollment
    WHERE students.SID = enrollment.SID AND courses.CID = enrollment.CID AND
    courses.name = 'Algorithms') AS SQ2
  WHERE SQ1.SID = SQ2.SID AND SQ1.coreTaken = 3
) 
#^^^^ Send this in, and 	  
# ------------------------------------------------------------------------------
 # Core Courses(91.503 explicit, One from Group 2,3,4)  
 #  Subquery: Find Students who have taken Algorithms
   (SELECT *
    FROM students, courses, enrollment
    WHERE students.SID = enrollment.SID AND courses.CID = enrollment.CID AND
    courses.name = 'Algorithms')

  # Subquery: Find total number of core courses taken not in Group 1 ie (2,3,4)
   (SELECT students.SID, COUNT(DISTINCT courses.groupID)
    FROM students, enrollment, courses
     WHERE courses.CID = enrollment.CID AND enrollment.SID = students.SID AND
      (courses.groupID <> 0 AND courses.groupID <> 1)
      GROUP BY students.SID)

 #Condition Three: Earn 18 credits from elective courses
  #Satisfied if Condition One and Two are satisfied.


'''
TODO:
 Move the letter grades into their Numerical counterparts, may be able to do
  this in the PHP side instead of polluting the DB with uneeded subqueries, and
  this may also be a lot faster to manage.
 Make a subquery to make sure that all of the needed requirements are met, and
  that each one of them filters the list, may again do this in PHP so as not to
  clutter up the database or the queries that need to be run on it.
 May do all the data management in JS, the only real requirement is that the
  database access be done in PHP, attain the data filter through it with JS...
  This is not what they want -_-.
'''
