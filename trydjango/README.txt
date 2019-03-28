###Django project###
#It's my first project I made
#it start with building admin site & it will make bloger
#i trying django with this project and I love it
#for any question please contact me amdsleem@yahoo.com
#the way to make invironment :
###1# pip install virtualenv
###2# pip install virtualenv --upgrade
###3# cd /path/
###4# virtualenv .

#to start a project use this code:
## django-admin.py startproject 'projectName'

#to run server use:
## python manage.py runserver

#for admin site configuration go to:
## https://docs.djangoproject.com/en/2.1/ref/contrib/admin/

#for more information about CRUD see:
## https://en.wikipedia.org/wiki/Create,_read,_update_and_delete


#at this point I add draft & publish to models.Post
#after that I makemigrations 'if it failed you can add timezone.now()'
#in form.py we add "Draft" & "Publish"
#at post_list.html:
##we change {{obj.timestamp}} to {{obj.publish}} in line 25
##also change {{ instance.timestamp }} to {{ instance.publish }} in line 15

#in class PostManager I make active() function instead of all()
#because all() will give 404 error to any 1 want to see the draft page
#but active() will allow only the admin to see it

#at models.post_detail() I add 'if instance.publish' block code to
#sure future post no one another admin can see it before publish time

#for any question please contact me amdsleem@yahoo.com
