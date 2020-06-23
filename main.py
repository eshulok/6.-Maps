#Maps are used to store multiple items, just like lists and tuples, but they are not ordered and do not allow duplicate entries
#Maps are useful when you want to store information about something
#They are also called dictionaries because like a dictionary entry, you have a key (the unique item you look up, which is a word in a dictionary), and a value for that key (the definition of the word in a dictionary)
#To create a map, we use curley braces to contain the information, and a colon between each key/value pairs, which are separated by commas 

#Here is a map to store my (made up) movie ratings for some movies
movie_ratings = {"Toy Story" : 5, "Monsters, Inc." : 4, "Inside Out" : 5, "A Bug's Life" : 2, "Coco" : 5, "Finding Nemo" : 5, "Finding Dora" : 3}

#The Key in this example is the movie title, the Value is my rating
print(movie_ratings) #Prints the whole list

#To access the value of an item in the map, we use the key, which is the movie name in this case 
#The syntax is similar to lists and tuples, but we use the key in place of an index
print("My rating for Toy Story is %s/5 stars" % movie_ratings['Toy Story'])

#Map items can be updated
movie_ratings['Monsters, Inc'] = 5
print("My rating for Monsters, Inc is %s/5 stars" % movie_ratings['Monsters, Inc'])

#To add a new movie rating is similar to updating an existing one
#If the Key is not found in the map, it is added as a new entry
movie_ratings['Cars'] = 4
print("My rating for Cars is %s/5 stars" % movie_ratings['Cars'])

#Be careful about misspelling a key when you update it, because instead of updating it, it will add a new entry
movie_ratings['Monsters Inc'] = 3 #Movie name doesn't match

#I expect the following to show my updated rating of 3/5 stars, but it still shows the original value because the line above added a new item in my map
print("My rating for Monsters, Inc is %s/5 stars" % movie_ratings['Monsters, Inc'])

#Keys do not need to be strings
#The following map uses student ids as the key and the value is the student name
student_ids = {111: 'Avery', 321 : 'Sam', 327 : 'Marianna', 528 : 'Jax'}

print("student with id %s is %s" % (327, student_ids[327]))

#If you try to get the value for a key that isn't in the map, you will get a KeyError
#print("student with id %s is %s" % (333, student_ids[333]))

