def solution(s):
    answer = len(s)
    for step in range(1, int(len(s))):
        count = 1
        sentence = ""
        comparison = s[0:step]
        # print(f'comparison : {comparison}')
        for idx in range(step, len(s), step):
            # print(f'now : {s[idx:idx+step]}')
            if comparison == s[idx:idx + step]:
                count += 1
            else:
                sentence += str(count) + comparison if count >= 2 else comparison
                count = 1
                comparison = s[idx:idx + step]
                # print(f'comparison : {comparison}')

        sentence += str(count) + comparison if count >= 2 else comparison
        # print(f'sentence : {sentence}')
        answer = len(sentence) if answer > len(sentence) or answer == 0 else answer
    return answer

sinput = input()
answer = solution(sinput)
print(answer)

'''
xababcdcdababcdcd
'''