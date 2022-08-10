ticket_list=["Paris-Skopje","Zurich-Amsterdam","Prague-Zurich","Barcelona-Berlin","Kiev-Prague","Skopje-Kiev","Amsterdam-Barcelona","Berlin-Paris",
]
source="Kiev"
route=[]

ticket_map = {}

for ticket in ticket_list:
    src, dest = ticket.split('-')
    ticket_map[src] = dest

#for k,v in ticket_map.items():
#    print(k, " = ", v)

route.append(source)

for i in range(len(ticket_list)):
    dest = ticket_map[source]
    route.append(dest)
    source = dest

print(str(route))


