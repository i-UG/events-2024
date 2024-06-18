<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ToDo</title>
  <link rel="stylesheet" type="text/css" href="views/style.css">
  <link rel="icon" type="image/x-icon" href="views/favicon.ico">
</head>

<body>
  <h1>| TODO Application</h1>
  <h2>Create new TODO item:</h2>

  <form action="/new" method="GET">
    <input type="text" size="100" maxlength="100" name="task">
    <br><br>
    <input type="submit" name="save" value="Save">
  </form>

</body>

</html>