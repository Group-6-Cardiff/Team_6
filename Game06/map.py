from items import *

room_student_union = {
    "name": "The Student Union",

    "description":
    """The SU""",

    "exits": {"south": "Accomadation", "east": "Pub", "west": "Police Station"},

    "items": [],

    "travel": {"south": 0.3, "east": 0.2, "west": 0.4},
   
    "locational_items":[],

    "open":True,

    "useable":[item_id,]
}

room_pub = {
    "name": "The Pub",

    "description":
    """The local Pub.""",

    "exits":  {"north": "Student Union", "south":"Comp Sci", "west":"Accomadation"},

    "items": [],

    "travel": {"north": 0.2, "south":0.4, "west":0.1},

    "locational_items":[],

    "open":True,

    "useable":[]
}

room_accomadation = {
    "name": "Your Accomadation",

    "description":
    """Your Accomadation""",

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
    """Your Bedroom""",

    "exits" :{"out":"Accomadation"},

    "items": [item_bike_key],

     "travel": {"out":0.05},

    "locational_items":[],

    "open":False,

    "useable":[]
}

room_police_station = {
    "name": "The Police Station",

    "description":
    """The Police Station""",

    "exits": {"north":"Student Union", "east": "Accomadation", "south": "Club" , "west":"Castle"},

    "items": [],

    "travel": {"north":0.4, "east": 0.2, "south": 0.4 , "west":0.3},
    
    "locational_items":[],

    "open":True,

    "useable":[item_evidence]

}

room_comp_sci = {
    "name":"The Comp Sci Buildings",

    "description":
    """Comp Sci.""",

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
    "The Bar",

    "exits":{"north":"Accomadation", "east":"Comp Sci", "south":"Club", "west":"Castle"},

    "items": [],

    "travel": {"north":0.4, "east":0.2, "south":0.1, "west":0.3},
    
    "locational_items":[],

    "open":True,

    "useable":[]
    
}

room_castle = {
    "name": "The Castle",

    "description":
    "The Castle",

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
    "The Club",

    "exits":{"north":"Police Station", "west":"Castle", "east":"Bar"},

    "items": [],

    "travel": {"north":0.4, "west":0.2, "east":0.2},

    "locational_items":[],

    "open":True,

    "useable":[]

}

rooms = {
    "Student Union": room_student_union,
    "Pub": room_pub,
    "Accomadation": room_accomadation,
    "Police Station": room_police_station,
    "Bedroom": room_bedroom,
    "Comp Sci":room_comp_sci,
    "Bar":room_bar,
    "Castle":room_castle,
    "Club":room_club,
}
