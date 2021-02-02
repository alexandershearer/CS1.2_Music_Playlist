class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  def get_title(self):
    return self.__title
  
  
  def set_title(self, title):
    old_title = self.__title
    self.__title = title
    return f"You have renamed {old_title} to {title}"


  def get_next_song(self):
    if self.__next_song != None:
      return self.__next_song
    else:
      return None


  def set_next_song(self, next_title):
    self.__next_song = next_title


  def __str__(self):
    return self.__title


  def __repr__(self):
    return f'{self.__title} -> {self.__next_song}'
