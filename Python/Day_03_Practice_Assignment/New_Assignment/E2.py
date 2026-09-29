"""`
You are organizing a movie marathon. You start with a playlist:
 ["Inception", "The Matrix", "Interstellar"]. Prompt the user to 
 enter the name of a movie they want to add.

If the movie is already in the list, print "Already added!"
 and do not insert it.
If it is not in the list, append it to the end of the list. 
Finally, sort the movie list alphabetically and print the updated playlist.
Sample Input: "Interstellar"
Sample Output:
Already added!
Alphabetical Playlist: ['Inception', 'Interstellar', 'The Matrix']




"""



# movie = ["Inception", "The Matrix", "Interstellar"]

# new_movie = input("Enter a new movie: ")

# if new_movie in movie:
#     print("Already added!")
# else:
#     movie.append(new_movie)

# movie.sort(key=str.lower)

# print("Alphabetical Playlist:", movie)


movie=["Inception", "The Matrix", "Interstellar"]
new_movie=input("enter a new movie :")

if new_movie in movie:
    print(f"{new_movie} already added.")
else:
    movie.append(new_movie)

movie.sort()        
print("updated list:", movie)