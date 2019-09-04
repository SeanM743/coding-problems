
def football_scoring(points, ways_to_score = {2,3,7}):

    def scoring(p, score):
        if p == 0:
            results.append(score[:])
        
        elif p > 0:
            for s in ways_to_score:
                score.append(s)
                scoring(p-s, score)
                score.pop()
        
    results = []
    scoring(12, [])
    return results
    

#print(football_scoring(12))

def score_game(points, ways_to_score):
    if points:
        for score in ways_to_score:
            if points - score >= 0:
                for way_to_score in score_game(points-score, ways_to_score):
                    yield [score, *way_to_score]
    else:
        yield []

#print(list(score_game(12,{2,3,7})))

def find_scoring(points, ways_to_score=[2, 3, 7]):
    def score_finder(points, scores, result):
        if points == 0:
            result.append(scores[:])
        elif points > 0:
            for val in ways_to_score:
                scores.append(val)
                score_finder(points - val, scores, result)
                scores.pop()

        return result

    return score_finder(points, [], [])

#print(find_scoring(12))

def find_scoring2(points, ways_to_score=[2, 3, 7]):
    def score_finder(points, scores, result = []):
        if points == 0:
            result.append(scores[:])
        elif points > 0:
            for val in ways_to_score:
                scores.append(val)
                score_finder(points - val, scores)
                scores.pop()
        return result
    return score_finder(points, [])

def find_scoring3(points, ways_to_score=[2, 3, 7]):
    def score_finder(points, scores, result = []):
        if points == 0:
            result.append(scores[:])
        elif points > 0:
            for val in ways_to_score:
                #scores.append(val)
                score_finder(points - val, scores + [val])
                #scores.pop()

        return result

    return score_finder(points, [])

print(find_scoring3(12))