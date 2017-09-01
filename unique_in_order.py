def unique_in_order(iterable):
    final = []
    iterable += ' '
    for i in range(len(iterable)-1):
        if iterable[i] != iterable[i+1]:
            final.append(iterable[i])
            continue
    return final
