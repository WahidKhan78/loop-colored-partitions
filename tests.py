from Profiles import *
from LoopColoredPartition import *
profs = [prof for i in xrange(10) for prof in get_bracelets(2,i)]

for prof in profs:
    print [prof,
           len(partitions_from_profile(prof)),
           len(partitions_from_profile(prof, unique_parts = True)),
           len(partitions_from_profile(prof, unique_sizes = True)),
           len(partitions_from_profile(prof, length_list = [1,3,5,7,9,11])),
           len(partitions_from_profile(prof, length_list = [1,3,5,7,9,11], unique_parts = True)),
           len(partitions_from_profile(prof, length_list = [2,4,6,8,10,12])),
           len(partitions_from_profile(prof, num_parts_list = [1,3,5,7,9,11]))]
