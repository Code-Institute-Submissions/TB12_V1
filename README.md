
# TB12 Fitness

Description:
----------------------------------------------------------------------------------------------------------------------------

This is a website to build a fitness commiunity providing exercise plans, Nutrition plans , Nutrition and exercise products.

User will be able to purchase subscripton based payment model and indivdual payments models.




Features Implemented:
----------------------------------------------------------------------------------------------------------------------------


Features left to implement:
-------------------------------------------------------------------------------------------------------------------------------

Functionatily on members on their successes / accomplishments

User profiles containing infomation that map to Nutrition and excercise plans

product reviews 

Subscription based payment model

Indivdual item purchase capabilties

Authenication and authorisation mechanisms for subscribers and adminstrators


Technologies Used:
--------------------------------------------------------------------------------------------------------------------------------

Django
Django-allauth

Python
Json
Javascript
HTML
Stripe


Enviorment Variables:

-------------------------------------------------------------------------------------------------------------------------------------



Debugging: 

FIXED
-------------------------------------------------------------------------------------------------------------------------------------


ISSUE 
----------------------------------------------------------------------------------------------------------------------------------------

BUGS
----------------------------------------------------------------------------------------------------------------------------------------

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

Stipe - local variables not loading so unable to test payment Functionatily

-------





TESTING 

-----------------------------------------------------------------------------------------------------------------------------------------





DEPLOYMENT:

---------------------------------------------------------------------------------------------------------------------------------------



RESOURCES/CREDITS:
----------------------------------------------------------------------------------------------------------------------------------------- 

SLACK CKz870 - Provided Json fixture creation python file so can create on json fixtures. To build custom files for use. 