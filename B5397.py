t = int(input())

for _ in range(t):
    pw_log = input()

    stack1 = []
    stack2 = []
    for tmp in pw_log:
        if tmp == '-':
            if len(stack1) > 0:
                stack1.pop(-1)

        elif tmp == '<':
            if len(stack1) > 0:
                stack2.append(stack1.pop(-1))
        
        elif tmp == '>':
            if len(stack2) > 0:
                stack1.append(stack2.pop(-1))

        else :
            stack1.append(tmp)

    print("".join(stack1) + "".join(stack2[::-1]))