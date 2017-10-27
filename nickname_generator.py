def nickname_generator(name):
    return 'Error: Name too short' if len(name) < 4 else name[:4] if name[2] in ('a', 'e', 'i', 'o', 'u') else name[:3] 
