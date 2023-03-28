def vote(votes):
    dict_vote = dict()
    for vote in votes:
        if vote in dict_vote:
            dict_vote[vote] += 1
        else:
            dict_vote[vote] = 1
    return max(dict_vote, key=dict_vote.get)


if __name__ == '__main__':
    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))
