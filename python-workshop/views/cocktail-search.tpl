<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Cocktails</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
  <link rel="stylesheet" type="text/css" href="./static/style.css">
  <link rel="icon" type="image/x-icon" href="./static/favicon.ico">
  <script src="https://kit.fontawesome.com/7e02145d4d.js" crossorigin="anonymous"></script>
</head>

<body>

  <div class="container">

    <h1 class="text-center text-primary">Cocktail Application</h1>
    <h2 class="text-center text-danger">Cocktail Search</h2>

    <div class="container">
      <div class="row g-3 align-items-center mt-5">

        <form class="example" action="/" method="get">

          <div class="input-group">
            <input class="text-start" type="text" placeholder="Search ..." name="search" id="search">
            <button class="btn btn-block btn-info"><i class="fas fa-search"></i></button>
          </div>

        </form>

      </div>
    </div>

  </div>

  <footer>

    % import datetime
    <div class="container mt-5">
      <hr class="mt-5">
      <p class="text-center small">&copy; FormaServe Systems Ltd {{ datetime.datetime.now().year}}</p>
    </div>

  </footer>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous">
    </script>
</body>

</html>