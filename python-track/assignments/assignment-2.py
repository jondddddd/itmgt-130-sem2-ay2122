'''Assignment 2

This assignment covers your proficiency with Python's data structures.
It engages your ability to manipulate and evaluate data stored in lists and dictionaries.
'''

def relationship_status(from_member, to_member, social_graph):
    '''
    Item 1.
    Relationship Status. 10 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-2-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Write your code below this line
    followertype_list = ["follower", "followed by", "friends", "no relationship"]
    subjectmember_following = social_graph[from_member]["following"]
    objectmember_following = social_graph[to_member]["following"]
    if to_member in subjectmember_following and from_member in objectmember_following:
        follower_type = "friends"
    elif to_member in subjectmember_following:
        follower_type = "follower"
    elif from_member in objectmember_following:
        follower_type = "followed by"
    else:
        follower_type = "no relationship"

    #Output
    return(str(follower_type))


def tic_tac_toe(board):
    '''
    Item 2.
    Tic Tac Toe. 10 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-2-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Write your code below this line
    points = 0
    lastelement = "blank"
    for row in board:
        points = 0
        lastelement = "blank"
        for element in row:
            if lastelement == element:
                points = points + 1
            lastelement = element
        if points == 2:
            return(str(element))

    #Verticals
    column = -1
    row = -1
    vert_board = [[],[],[]]
    while column < 2:
        column = column + 1
        while row < 2:
            row = row + 1
            element = board[row][column]
            list.append(vert_board[column],element)
        else:
            row = -1
    for row in vert_board:
        points = 0
        lastelement = "blank"
        for element in row:
            if lastelement == element:
                points = points + 1
            lastelement = element
        if points == 2:
            return(str(element))

    #Diagonals
    column = -1
    row = -1
    points = 0
    lastelement = "blank"
    diag_board = [[],[]]
    while column < 2:
        
        column = column + 1
        row = row + 1
        element = board[row][column]
        if lastelement == element:
            points = points + 1
        list.append(diag_board[0],element)
        if points == 2:
            return(str(element))
        lastelement = element

    column = -1
    row = 3
    points = 0
    lastelement = "blank"
    while column < 2:
        
        column = column + 1
        row = row - 1
        element = board[row][column]
        if lastelement == element:
            points = points + 1
        list.append(diag_board[1],element)
        if points == 2:
            return(str(element))
        lastelement = element

    #No defined winner
    return(str("No winner"))


def eta(first_stop, second_stop, route_map):
    '''
    Item 3.
    ETA. 10 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "assignment-2-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Write your code below this line
    for tuple_stop in route_map:
        if tuple_stop[0] == first_stop:
            start_stop = first_stop
            time = route_map[tuple_stop]["travel_time_mins"]
            first_tuple_stop = tuple_stop

    #Switch between different tuples
    while found_end_stop == False:
        if first_tuple_stop[1] == second_stop:
            break
        else:
            stop_check = first_tuple_stop[1]
            for tuple_stop in route_map:
                if stop_check == tuple_stop[0]:
                    first_tuple_stop = tuple_stop
                    time = time + route_map[first_tuple_stop]["travel_time_mins"]
                    
    #Output
    return(int(time))