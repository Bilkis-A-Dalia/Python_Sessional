def IntersecOfSets(arr1,aar2,arr3):

    # convert arry to set
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)

    # calculating intersection
    set1 = s1.intersection(s2)
    result_set = set1.intersection(s3)

    # set to list convert
    final_list = list(result_set)
    print(final_list)

if __name__ == '__main__':
    # elements of set
    arr1 = [1,2,3,4,5]
    arr2 = [4,5,6,7,8]
    arr3 = [4,3,7,5,8]

    IntersecOfSets(arr1,arr2,arr3)