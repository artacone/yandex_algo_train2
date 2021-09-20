if __name__ == '__main__':
    total_msgs = int(input())
    replies = [0] * total_msgs
    topics = [''] * total_msgs
    for i in range(total_msgs):
        n = int(input())
        if n == 0:
            replies[i] = i
            topics[i] = input()
        else:
            replies[i] = replies[n - 1]
        input()
    replies_counter = {}
    for topic_n in replies:
        replies_counter[topic_n] = replies_counter.get(topic_n, 0) + 1
    ans = []
    for topic_n in replies_counter:
        ans.append((-replies_counter[topic_n], topic_n))
    print(topics[min(ans)[1]])
 