from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    #First will equal the first song in the list
    main = self.__first_song
    #New song will equal a new song object
    new_song = Song(title)

    #If there is no first song, the first song will be the first new song object
    if main == None:
      self.__first_song = new_song
    #If there is no next song, then set the next entry to the next song
    else:
      while main.get_next_song() != None:
        main = main.get_next_song()
      main.set_next_song(new_song)



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    #Set variables for the loop and to update 
    main = self.__first_song
    found = False
    index = 0
    #While there is a song in the list
    while main != None and not found:
      #If the the get title function is equal to a title then return true
      if main.get_title() == title:
        found = True
      #Else, run the loop again
      else:
        main = main.get_next_song()
        index + 1

    return index


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    main = self.__first_song
    found = False
    prev = None

    while not found:
      if main == None:
        print(f'Could not fine song with name {title}')
        return 
      elif main.get_title() == title:
        found = True
      else:
        prev = main
        main = main.get_next_song()

      if prev == None:
        self.__first_song = main.get_next_song()
      else:
        prev.set_next_song(main.get_next_song())




  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    main = self.__first_song
    counter = 0

    if main == None:
      print(f'There are no songs in the playlist')
    else:
      while main.get_next_song() != None:
        counter += 1
        main = main.get_next_song()

    return counter + 1


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    main = self.__first_song
    counter = 1
    if main == None:
        print("There are no songs.")
    else:
        while main != None:
            print(f'#{counter} {main.get_title()}')
            counter += 1
            main = main.get_next_song()

  