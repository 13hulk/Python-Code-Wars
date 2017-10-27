def user_contacts(data): #data is a list of lists wit conatct name and zip code
    return { i[0] : ( None if len(i) == 1 else i[1] ) for i in data }
