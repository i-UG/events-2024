<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ToDo</title>
  <link rel="stylesheet" type="text/css" href="./static/style.css">
  <link rel="icon" type="image/x-icon" href="./static/favicon.ico">
</head>

<body>
  <h1>| TODO Application</h1>
  <h2>All TODO items are as follows:</h2>
  <table>
    <tr>
      <th>ID</th>
      <th>Text</th>
      <th>Status</th>
    </tr>
    %for row in rows:
    <tr>
      %for col in row:
      <td>{{col}}</td>
      %end
    </tr>
    %end
  </table>
</body>

</html>