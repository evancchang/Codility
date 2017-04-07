def solution(S):
    n = len(S)
    if n < 0 or n > 1000000:
        return 0

    if len(S.strip()) == 0: # S is empty
        return 1

    match_bracket = {')':'('}
    to_push_bracket = ['(']

    bracket_stack = []
    for bracket in S:
        if bracket not in ['(', ')']:
            return 0

        if bracket in to_push_bracket:
            bracket_stack.append(bracket)
        else:
            if len(bracket_stack) == 0:
                return 0
            if match_bracket[bracket] != bracket_stack.pop():
                return 0

    if len(bracket_stack) == 0:
        return 1
    else:
        return 0

print solution("(()(())())")
