from urllib2 import urlopen
from json import load
import json

url = "http://databits.io/static_content/challenges/wordpress-dot-com-social-reciprocity-challenge/wordpress_com_userdata.json"
json_obj = urlopen(url)
data = load(json_obj)

user_list = []
blog_list = []

for i in data:
	i = json.dumps(i['user_id'], indent = 1, separators=(',',': '))
	user_list.append(i)

for i in data:
	i = json.dumps(i['user_blogs'], separators=(',',': '))
	blog_list.append(i)


blog_list = ([s.replace('[','') for s in blog_list])
blog_list = ([s.replace(']','') for s in blog_list])

print blog_list[0]
print "AND"
print user_list[0]

first_blogs = blog_list[0]
num_of_blogs = 1 +(first_blogs.count(','))

print first_blogs.split(",")[0]
print num_of_blogs

# ok, have user ID & number of blogs
# need to write a loop that goes through and associates each blog ID with the correct user ID

# what about a dictionary of blog_id : user_id ? since users have many blogs but blogs
# have only one user - could then query dictionary for blogs / user, etc