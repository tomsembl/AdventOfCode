a="""2558912-2663749,1-19,72-85,82984-100358,86-113,193276-237687,51-69,779543-880789,13004-15184,2768-3285,4002-4783,7702278-7841488,7025-8936,5858546565-5858614010,5117615-5149981,4919-5802,411-466,126397-148071,726807-764287,7454079517-7454227234,48548-61680,67606500-67729214,9096-10574,9999972289-10000034826,431250-455032,907442-983179,528410-680303,99990245-100008960,266408-302255,146086945-146212652,9231222-9271517,32295166-32343823,32138-36484,4747426142-4747537765,525-652,333117-414840,13413537-13521859,1626-1972,49829276-50002273,69302-80371,8764571787-8764598967,5552410836-5552545325,660-782,859-1056"""
test="""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
#a=test
b=[[int(y) for y in x.split("-")] for x in  a.split(",")]
invalids = 0
for start,end in b:
    for x in range(start,end+1):
        str_x=str(x)
        l = len(str_x)
        if l % 2 != 0: continue
        half_1, half_2 = str_x[:l//2], str_x[l//2:]
        if half_1==half_2:
            invalids+=x
print(invalids) #p1

def all_equal(segments):
    segments[0]
    for x in segments[1:]:
        if x != segments[0]:
            return False
    return True

def is_invalid(x):
    str_x=str(x)
    l = len(str_x)
    for y in range(2,l+1):
        if l % y != 0: continue
        segments = [str_x[z*l//y:(z+1)*l//y] for z in range(y)]
        if all_equal(segments):
             return True
    return False
                 

invalids = 0
for start,end in b:
    for x in range(start,end+1):
        if is_invalid(x):
            invalids+=x
print(invalids) #p2
