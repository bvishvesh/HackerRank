def migratoryBirds(arr):
    a = arr.count(1)
    b = arr.count(2)
    c = arr.count(3)
    d = arr.count(4)
    e = arr.count(5)
    bird_cnt=[a,b,c,d,e]
    return 1+bird_cnt.index(max(bird_cnt))
    
arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = migratoryBirds(arr)
print(result)
