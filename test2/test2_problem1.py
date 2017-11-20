import random

airports = ['LGA','SFO','SEA','DTW','SFO','EWR','ATL','ORD',
            'LAX','JFK','BOS','DCA']

sample_routes = {'LAX': ['SFO', 'ATL'],
                 'BOS': ['SFO', 'SEA'],
                 'SFO': ['JFK', 'BOS', 'BOS'],
                 'LGA': ['ATL', 'BOS'], 
                 'JFK': ['DCA', 'SFO'],
                 'ATL': ['SFO', 'SFO', 'DCA'],
                 'ORD': ['LAX', 'SFO'],
                 'DTW': ['BOS', 'LAX', 'JFK'], 
                 'DCA': ['SEA', 'SFO', 'LGA'], 
                 'SEA': ['DTW', 'SFO', 'LAX'], 
                 'EWR': ['SFO', 'ATL', 'SFO']}

def create_routes(airp):
  routes = {}
  for i in airports:
      n = random.randrange(2,6)
      d = []
      for j in range(n):
        newa = airports[random.randrange(len(airp))]
        while newa in d or newa == i: newa = airports[random.randrange(len(airp))]
        d.append(newa)
      routes.setdefault(i,d)
  return routes

routes = create_routes(airports)

def two_hops(routes,start,end):
  if end in routes[start]: return True
  for i in routes[start]:
      if end in routes[i]: return True
  return False
      
print(create_routes(airports))