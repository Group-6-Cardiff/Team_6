from items import *

room_student_union = {
    "name": "The Student Union",

    "description":
    """You are in the main entance of Cardiff University students union
at the ground floor. The Students' Union is a very large building which has many stores at the ground level.
You can choose to go up via the lift or stairs. In the second level, you can see a reception which involves
everything regarding club nights at Y PLAS. It seems the receptionist is a bit sleepy.
At your left you can see the Y PLAS entrance, there are 2 possible exits.
You can exit the same way you entered the SU,
or you can go down the stairs outside floor 2.""",

    "exits": {"south": "Accommodation", "east": "Pub", "west": "Police Station"},

    "items": [],

    "travel": {"south": 0.3, "east": 0.2, "west": 0.4},
   
    "locational_items":[],

    "open":True,

    "useable":[item_id,]
}

room_pub = {
    "name": "The Pub",

    "description":
    """You are at the entrance of the Pub "Pryzm". At the entrance, you can see that there is a small
reception with a nervous receptionist. It seems she will ignore you until she calms down.
Inside, there are various paths you can take, however the biggest corridor
leads to the main bar in which the barman is serving cocktails
to two people who are wearing trench coats and sun glasses. The room is quite ample, however,
you can see that if you take the next path, you will reach an even bigger room which looks
like the main disco area. The only exit of the pub is the main entrance.""",

    "exits":  {"north": "Student Union", "south":"Comp Sci", "west":"Accommodation"},

    "items": [],

    "travel": {"north": 0.2, "south":0.4, "west":0.1},

    "locational_items":[],

    "open":True,

    "useable":[]
}

room_accommodation = {
    "name": "Your Accommodation",

    "description":
    """You are in a new student accomodation with a modern but familiar design.
At the entrance, there is a common area with a receptionist named J.P
looking at the CCTV cameras, you also notice a pool table 
which is surrounded by 3 students chatting about what happened last night.
Next to you there is a door leading to different corridors with rooms.
Your room is in the left side of the first corridor.""",

    "exits": {"north":"Student Union", "east":"Pub", "south":"Bar", "west": "Police Station", "in":"Bedroom"},

    "items": [item_bike],

    "travel": {"north":0.3, "east":0.1, "south":0.4, "west": 0.2, "in":0.05},

    "locational_items":[],

    "open":True,

    "useable":[item_bike_key,item_room_keys]
}
room_bedroom = {
    "name": "Your Bedroom",

    "description":
    """You are in your room. It's a small room but it feels really familiar and comfortable.
There is a big window with views to the bar in the south.
In your room, you have a single bed, a quite wide messy desk with your desktop computer and some items.
You also have a closet full of clothes.
There is only one entry to the room.""",

    "exits" :{"out":"Accommodation"},

    "items": [item_bike_key],

     "travel": {"out":0.05},

    "locational_items":[],

    "open":False,

    "useable":[]
}

room_police_station = {
    "name": "The Police Station",

    "description":
    """You are now in the police station. It's a large, grey and cold building.
Inside, you can feel the pressure of authority, and you are worried for your friend Kirill,
as you can hear him cry for help in the distance as he is still being detained in a cell.
In the main entrance, there is a receptionist waiting with an angry face,
and in the waiting area you can see a homeless man with a familiar face,
however, you cannot remember him just yet.
There are several corridors inside the station,
some leading to offices and others leading to the cells.
Kirill is in the very last cell in the last corridor""",

    "exits": {"north":"Student Union", "east": "Accommodation", "south": "Club" , "west":"Castle","in":"Staff room"},

    "items": [],

    "travel": {"north":0.4, "east": 0.2, "south": 0.4 , "west":0.3,"in":0.05},
    
    "locational_items":[],

    "open":True,

    "useable":[item_evidence, item_id]

}

room_comp_sci = {
    "name":"The Comp Sci Buildings",

    "description":
    """You are now in the Comp Sci department here is where you'll be studying for
     the next 3 years..... if you manage to clear your name""",

    "exits": {"north": "Pub", "west":"Bar"},

    "items": [],

    "travel": {"north": 0.4, "west":0.2},

    "locational_items":[],

    "open":True,

    "useable":[]

}

room_bar ={
    "name":"The Bar",

    "description":
    """You are now in the entrance of the bar called "Central Bar". You can see that
there are several tables and a wide bar in which there is a barman waiting to serve customers.
To your right, you can see that there are stairs to reach the first floor of the bar.
In the first floor, there are more tables and another barman. If you look closely,
you can see a small box next to the till. It seems it can be opened without a key. The only exit
is the main entrance of the bar.""",

    "exits":{"north":"Accommodation", "east":"Comp Sci", "south":"Club", "west":"Castle"},

    "items": [],

    "travel": {"north":0.4, "east":0.2, "south":0.1, "west":0.3},
    
    "locational_items":[],

    "open":True,

    "useable":[]
    
}

room_castle = {
    "name": "The Castle",

    "description":
    """You are at the entrance of Cardiff Castle. At the entrance, you can see a reception in which
you can pay for your entrance ticket, or alternatively, show your castle card. You have a sudden realisation
that there is only two paths. The left path will guide you to the top of the castle, 
and the right path will lead you to the inners of the castle. 
Around you, there are people walking around, as well as people having a rest on the grass
at the entrance of the castle. The only exit of the castle is the main entrance.""",

    "exits":{"north":"Police Station", "east":"Bar", "south":"Club"},

    "items": [],

    "travel": {"north":0.3, "east":0.5, "south":0.2},

    "locational_items":[],

    "open":True,

    "useable":[]

}

room_club = {
    "name": "The Club",

    "description":
    """You are now in the entrance of a club called Revs. At the entrance, you notice that there is a security guard
 who is glaring at you; as if he recognises you. Inside, you can see that there are big tables 
 and a worried barman next to the till. 
 The club is not very crowded for now, but it's likely to get busier in the next few minutes.
You can see different paths to take, however the club is not very big, which means that everything you
can see at the moment is probably what you will find in the club. The only exit of the club is the
main entrance.""",

    "exits":{"north":"Police Station", "west":"Castle", "east":"Bar"},

    "items": [],

    "travel": {"north":0.4, "west":0.2, "east":0.2},

    "locational_items":[],

    "open":True,

    "useable":[]

}

room_staff_room = {
    "name": "Staff room",

    "description":
    """You are now in police staff room, it's a bit odd because besides lockers there is a safe and old phone box. You see another pair of doors that can lead to prison cells but they
are locked. You spot than on the safe there is a short note "Code is 10011010010" """,

    "exits": {"out": "Police Station", "in": "Secret room"},

    "items": [],

    "travel": {"out":0.05,  "in": 0.05},
    
    "locational_items":[item_safe, item_phone_box],

    "open":False,

    "useable":[item_coins, item_safe,item_phone_box]

}
room_secret_room = {
    "name": "Secret room",

    "description":
    """Well it's secret. You can hear Kirill on the other side of locked doors """,

    "exits": {"out": "Staff room"},

    "items": [item_beer, item_book],

    "travel": {"out":0.05},
    
    "locational_items":[item_fridge, item_bookshelf],

    "open":False,

    "useable":[item_fridge, item_bookshelf]
}

rooms = {
    "Student Union": room_student_union,
    "Pub": room_pub,
    "Accommodation": room_accommodation,
    "Police Station": room_police_station,
    "Bedroom": room_bedroom,
    "Comp Sci":room_comp_sci,
    "Bar":room_bar,
    "Castle":room_castle,
    "Club":room_club,
    "Staff room": room_staff_room,
    "Secret room": room_secret_room,
}
