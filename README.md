# wp_test

WP_TEST

I. CODE:
https://github.com/wtrela/wp_test


II. DEMO:


Short instruction
1. Retrieve token

curl -X POST -d "grant_type=password&username=admin&password=admin" -

u"g1SEXoQ3PFFHSpqJg0fSkctTPHtr3YCY3FAt1j09:AHVALB6tYvtEB6VXFodzssuLsTDj9wQUbvSmOdjbZD2mMzPEFtDnEj2OSxkfzByf63nUPoPyI6IgCE4ToRseAPU

HtWp5wd3XGd67mZxK8zOLhSZyfBMnE6kg66iGvDss" http://ec2-52-56-124-112.eu-west-2.compute.amazonaws.com/api/v0/o/token/

2. Save your token

3. Testing Endpoint API

curl -H "Authorization: Bearer <token>" http://ec2-52-56-124-112.eu-west-2.compute.amazonaws.com/api/v0/websites/




Full authorization instruction

1. Login to admin page (login: admin password: admin)
2. Browse to http://ec2-52-56-124-112.eu-west-2.compute.amazonaws.com/api/v0/o/applications/
3. Register your application which will test endpoint API
4. Fill in data
- Name: your_name
- Client type: Confidential.
- Authorization Grant Type: Resource owner password-based
5. Retrieve token

curl -X POST -d "grant_type=password&username=<name>&password=<password>" -u"<client_id>:<client_secret>" http://ec2-52-56-124-

112.eu-west-2.compute.amazonaws.com/api/v0/o/o/token/

example:

curl -X POST -d "grant_type=password&username=admin&password=admin" -

u"g1SEXoQ3PFFHSpqJg0fSkctTPHtr3YCY3FAt1j09:AHVALB6tYvtEB6VXFodzssuLsTDj9wQUbvSmOdjbZD2mMzPEFtDnEj2OSxkfzByf63nUPoPyI6IgCE4ToRseAPU

HtWp5wd3XGd67mZxK8zOLhSZyfBMnE6kg66iGvDss" http://ec2-52-56-124-112.eu-west-2.compute.amazonaws.com/api/v0/o/token/


response:

{
    "access_token": "N2vYbv43nYQDZ5Dq19Mim8cwSkJ9E1",
    "token_type": "Bearer",
    "expires_in": 36000,
    "refresh_token": "LCzg16cbhARAhktPPb9PjK5ebyye9L",
    "scope": "read write groups"
}



6. Save your token
7. Testing Endpoint API

example:

curl -H "Authorization: Bearer N2vYbv43nYQDZ5Dq19Mim8cwSkJ9E1" http://ec2-52-56-124-112.eu-west-

2.compute.amazonaws.com/api/v0/websites/


III. Own deployment

You need to have installed docker and fabric.


1. fab bootstrap

2. (in case problems with docker networks) 
	- fab net
	- fab bootstrap

