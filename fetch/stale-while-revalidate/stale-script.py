import random, string, datetime

def token():
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(20))

def main(request, response):
    revalidation = request.headers.get("If-Modified-Since", None) != None
    age = 0;
    if revalidation:
      age = 100;

    unique_id = token()
    headers = [("Content-Type", "text/javascript"),
               ("Cache-Control", "private, max-age={}, stale-while-revalidate=10".format(age)),
               ("Last-Modified", datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")),
               ("Token", unique_id)]
    content = "report('{}', '{}')".format(unique_id, revalidation)
    return 200, headers, content
