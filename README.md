Fibonacci Fast Api - using python

GET: /api/health -> A HEALTH CHECK

POST: /api/fibonacci -> Accepts a json (

    {
        "lista" : 7
    }

) retuns a fibonacci sequence.

To run this api using vunicor: uvicorn main:app --reload

To run this API in a Docker container:

docker build -t fibonacci-api .
docker run -d --name fibonacci -p 8000:80 fibonacci-api
