# AB
Requared data:
- Address.
- Threads.
- № of requests
- Time limit
- Timeout
- Cookie
- Basic auth
- Content-type
- Arbitary header

ADRESS
Address should have format: http(s)://www.<domain.name>/

THREATS
Number of multiple requests to make at a time

№ OF REQUESTES
Number of requests to perform

TIME LIMIT
Seconds to max. to spend on benchmarking. This implies -n 50000

TIMEOUT
Seconds to max. wait for each response. Default is 30 seconds

COOKIE
Add cookie, eg. 'Apache=1234'. (repeatable)


BASIC AUTHENTIFICATION
Add Basic WWW Authentication, the attributes are a colon separated username and password.
                    
CONTENT-TYPE
Content-type header to use for POST/PUT data, eg. 'application/x-www-form-urlencoded'

ARBITARY HEADER
Add Arbitrary header line, eg. 'Accept-Encoding: gzip' Inserted after all normal header lines. (repeatable)
