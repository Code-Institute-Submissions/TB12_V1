
# TB12 Fitness

Description:
----------------------------------------------------------------------------------------------------------------------------

A Tribute to Tom Brady

This is a website to build a fitness commiunity providing exercise plans, Nutrition plans , Nutrition and exercise products.

User will be able to purchase idividual payments model for products.

User are able to create profiles to track order history and save address details for next orders. 





Features Implemented:
----------------------------------------------------------------------------------------------------------------------------

Account creation/register
LogOut and Log in Feauture
View profile with historty of current and previous orders.
Search through database of products. 
admin can create new products and edit existing ones
Abilty to create new profile and verify user via email.

Features left to implement:
-------------------------------------------------------------------------------------------------------------------------------

Subscription payement model. 

More products to be added to database for assignment for special offers.




Technologies Used:
--------------------------------------------------------------------------------------------------------------------------------

Django
Django-allauth
heroku 
Python
Json
Javascript
HTML
Stripe


Enviorment Variables:

-------------------------------------------------------------------------------------------------------------------------------------



Debugging: 

-------
Bootstrap cdn not working correctly for dropdown list. 
-------
could not get products to load.  error :Traceback (most recent call last):
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/options.py", line 575, in get_field
    return self.fields_map[field_name]
KeyError: 'catergory'    -- resolve

-------

Images not loading from django admin in products. ERROR:

Page not found (404)
Request Method:	GET
Request URL:	http://localhost:8000/media/nutrition.jpeg
Raised by:	django.views.static.serve     -- fixed .(typo in urls.py file) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
-------
Opening product_details page getting error : NoReverseMatch at /products/ 
Seems to be an issue with URL not being picked up.   / / fixed (another typo but urls.py for products, name attri was not correct )
-------

product.html file htr horizontal rule floating to the left of screen , not centered. 
-------
Sorting on rating instead of a "=desc" or "=asc" a minus symbol replaces the equals which is inccorrect so the page does not sort. 
Fixed- it was a typo in href for main_nav.html

-------

toasts close symbol not showing in the correct location. Needs to be floated to the right .

-------

Stipe - local variables not loading so unable to test payment Functionatily :// temp fixed manually loading 

-------

Django database not updating values - missing import in apps.py - fixed

-------





TESTING 

-----------------------------------------------------------------------------------------------------------------------------------------

Created webhooks handler and webhooks.py. Stripe website not recieving responces yet. 
Port 8000 was showing as private. Made public resolved the issue.

Checked all links to pages and work succefully.

Tested navigation and links and all work fine. 

Can Create products and stored correctly with format in database.

The infomation stored on database can be retrieved a dispalyed onscreen correctly to be purchased.

Tested editing a product as admin as well deleting. (message promt when deleting works.)

Tested all buttons and input fields. All displaying correctly at all resolutions. 

Log in and out feautes are working and Store password securely.

While testing notice nutriction items were not showing. _Fixed

Stripe payments are working correctly. 

Tested new account with confimr email works fine. 




DEPLOYMENT:

---------------------------------------------------------------------------------------------------------------------------------------

Deplayed to heroku with static and media files hosted on AWS.

https://sk-tb12.herokuapp.com/





RESOURCES/CREDITS:
----------------------------------------------------------------------------------------------------------------------------------------- 

SLACK CKz870 - Provided Json fixture creation python file so can create on json fixtures. To build custom files for use. 