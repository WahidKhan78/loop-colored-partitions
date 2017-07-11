def get_profiles(num_colors, size):
    if num_colors == 1:
        return [[size]]
    profiles = []
    for i in xrange(size+1):
        for prof in get_profiles(num_colors-1, size-i):
            profiles.append(prof + [i])
    return profiles

def is_necklace(comp):
    representative = int(''.join(map(str,list(comp))))
    for i in xrange(len(comp)):
        if (representative > int(''.join(map(str,list(comp)[i:]+list(comp)[:i])))):
            return False
    return True

def is_bracelet(profile):
    representative = int(''.join(map(str,list(profile))))
    for i in xrange(len(profile)):
        if (representative > int(''.join(map(str,list(profile)[i:]+list(profile)[:i])))):
            return False
    reverse = profile[::-1]
    for i in xrange(len(profile)):
        if (representative > int(''.join(map(str,list(reverse)[i:]+list(reverse)[:i])))):
            return False
    return True

def get_necklaces(num_colors,size):
    return [x for x in get_profiles(num_colors,size) if is_necklace(x)]

def get_bracelets(num_colors, size):
    return [x for x in get_profiles(num_colors,size) if is_bracelet(x)]
