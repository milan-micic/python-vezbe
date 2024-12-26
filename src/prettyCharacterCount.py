import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
heroes = {
  'id': 564564676,
  'name': 'Sandman',
  'nickname': [
    'Morpheus',
    'Dream',
    'Murphy'
  ]
}

count = {}
for character in message:
  count.setdefault(character, 0)
  count[character] = count[character] + 1
pprint.pprint(count)

print()

heroes = pprint.pformat(heroes)
chars_to_remove = ["{", "}", "'","[","]"]
for char in chars_to_remove:
  heroes = heroes.replace(char, "")
print(heroes)
print()