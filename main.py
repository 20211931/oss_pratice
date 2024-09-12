import collections

class Mycollection:
  def __getitem__(self, key):
    return f"Value for {key}"

collection = Mycollection()
print(collection.__getitem__(3))
print(collection[3])

