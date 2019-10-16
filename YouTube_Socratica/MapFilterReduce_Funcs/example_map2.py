#!/usr/bin/env python3

temps = [
    ("Berlin", 29),
    ("Cairo", 36),
    ("Buenos Aires", 19),
    ("Los Angles", 26),
    ("Tokyo", 27),
    ("New York", 28),
    ("London", 22),
    ("Beijing", 32)
]

# Converting celsius to fahrenheit.
c_to_f = lambda data: (data[0], (9 / 5) * data[1] + 32)

print(
    (list
     (map(c_to_f, temps)
      )
     )
)
