def getKeywords(j):
    size = len(j['summarizedInsights']['keywords'])
    timestampdict = {}
    graphtimes = {}
    for i in range(0, size):
        keyword = j['summarizedInsights']['keywords'][i]
        timestampdict[keyword['name']] = keyword['appearances']
    for key in timestampdict:
        graphtimes[key] = []
        for dict in timestampdict[key]:
            graphtimes[key].append([dict['startSeconds'], dict['endSeconds']])
    # print(timestampdict)
    # print(graphtimes)

    return graphtimes