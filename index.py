
import cgi

form_inputs = cgi.FieldStorage()

print "Content-type: text/html\n"


print    "<!doctype html>"
print    "<html lang="en">"
print    "<head>"
print       " <!-- Required meta tags -->"
print        "<meta charset="utf-8">"
# print        "<meta name="viewport" content="width=device-width, initial-scale=1">"

        # <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

print       " <title>Hello, world!</title>"
print    "</head>"
print    "<body>"
print        "<h1>Hello, world!</h1>"


# print      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

print       "<form name="test" action="." method="post">"
print           " <label> Name <label>"
print  " <input type="text" name="name">"
print        "<input type="submit" value="submit">"
print   "</body>"
print   "</html>"