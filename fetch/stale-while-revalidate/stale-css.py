def main(request, response):

    content = "body { background: rgb(0, 128, 0); }"
    for cookie in request.cookies.get_list('a'):
      content = "body { background: rgb(255, 0, 0); }"
    for cookie in request.cookies.get_list('a'):
      content = "body { background: rgb(255, 0, 0); }"

    headers = [("Content-Type", "text/css"),
               ("Set-Cookie", "a=b"),
               ("Cache-Control", "private, max-age=0, stale-while-revalidate=10")]
    return 200, headers, content
