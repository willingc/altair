from altair.api import *
import altair.datasets as ds

data = pd.DataFrame([
      {"a": "A","b": 28}, {"a": "B","b": 55}, {"a": "C","b": 43},
      {"a": "D","b": 91}, {"a": "E","b": 81}, {"a": "F","b": 53},
      {"a": "G","b": 19}, {"a": "H","b": 87}, {"a": "I","b": 52}
    ])

v = Viz().encode(
    x=X('a:O'),
    y=Y('b:Q')
).bar()

expected_output = {'encoding': {'x': {'field': 'a', 'type': 'ordinal'},
                                'y': {'field': 'b', 'type': 'quantity'}},
                   'mark': 'bar'}