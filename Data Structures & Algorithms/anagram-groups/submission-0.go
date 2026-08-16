func groupAnagrams(strs []string) [][]string {
    v := make(map[[26]int][]string)
    for _, s := range strs {
        var count [26]int
        for _, c := range s {
            count[c-'a']++
        }

        v[count] = append(v[count], s)
    } 

    var res [][]string
    for _, group := range v {
        res = append(res, group)
    }

    return res
}
