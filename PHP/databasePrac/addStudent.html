<?php
function studentAddQuery($query) {
	//Set up a connection to the given DB
	$connection=mysqli_init();
	//Test that the connection was actually instantiated.
	if( !$connection)
		die("MySQLi Initialization failed.");
	if (!mysqli_real_connect($connect,"localhost:25000","root","")
		die("Connect Error: " . mysqli_connect_error());

	$db = mysql_select_db ('ProjectsDB') or die ('Could not select database'); 	
	$result = $result = mysql_query($query) or die ('Query failed: '.mysql_error());
	echo $result;
	return $result;
}
function addStudent($_name,$_sid,$_iid,$_major, $_career, $_degreeHeld){
	$query = "INSERT INTO students (SID, name, IID, major, degreeHeld, career)
    	VALUES('$_sid', '$_name', '$_iid', '$_major', '$_degreeHeld', '$_career')"
    studentAddQuery($query);	
}
function getAnElt($choice){
	if( $choice == 1){
		$query = "	SELECT IID, COUNT(DISTINCT SID)
	FROM students
	GROUP BY IID
	LIMIT 1;
	" 
	} else if ($choice == 2){
		$query = "SELECT SID
	FROM students
	ORDER BY SID DESC
	LIMIT 1;
	"
	}
	$result = studentAddQuery($query);
	if ($choice == 2)
		$result++;
	return $result
}
?>

<!--
Adds a student to the given Database. Base Format
Takes in the students basic Information, the SID is internally
generated.
-->
<!--First Try at this HTML PHP Thing. Lets see. -->
<html>
	<head>
		<title>Add A Student</title>
	</head>
	<body>
		<h1>Add Student</h1>
		<p>Adds a Student into the Given Database. Please add in specified fields.</p>
		<!--Just signals which PHP Point to call when submit is hit -->
		<form action="./queries/addStudent.php" method="post">
			<!--
			Dictates a table object. Explicitly defines its body, as well as the inputs for its fields.
			-->
			<table border="10">
				<tbody>
					<tr>
						<td>Name</td>
						<td align="left">
							<input type="text" name="_name" size="20" maxlength="20"/>
						</td>
					</tr>
					<tr>
						<td>Student ID#</td>
						<td align="left">
							<input type="text" name="_sid" size="20" maxlength="20" 
							value="<?php getAnElt(2); ?>" />
						</td>
					</tr>
					<tr>
						<td>Advisor</td>
						<td>
							<input type="text" name="_iid" size="5" maxlength="5"
							value="<?php getAnElt(1); ?>" />
						</td>
					</tr>
					<tr>
						<td>Major</td>
						<td>
							<input type="text" name="_major" size="5" maxlength="5"/>
						</td>
					</tr>
					<tr>
						<td>Degree Held</td>
						<td>
							<input type="text" name="_degreeHeld" size="20" maxlength="20"/>
						</td>
					</tr>
					<tr>
						<td>Scholastic Career</td>
						<td>
							<input type="text" name="_career" size="20" maxlength="20"/>
						</td>
					</tr>
					<tr>
						<td colspan="5" align="center">
							<input type="submit" value="Insert Student"/>
						</td>
					</tr>
				</tbody>
			</table>
		</form>
	</body>
</html>