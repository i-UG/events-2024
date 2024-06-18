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
  <h1>TODO Application: All Items</h1>

  <table class="styled-table">
    <thead>
      <tr>
        <th>ID</th>
        <th>Text</th>
        <th>Status</th>
      </tr>
    </thead>
    %for i in rows:
        <tr>
                <td>{{ i[0] }}</td>
                <td>{{ i[1] }}</td>
                <td>{{ i[2] }}</td>
        </tr>
    %end
  </table>
</body>

</html>