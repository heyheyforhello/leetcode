def solution(s):
    s = "{" + s + "}"
    stack = []
    N = len(s)
    i = 0

    def compress(cell):
        pass

    elements = ''
    while i < N:
        c = s[i]
        
        if c == '{':
            if elements:
                stack.extend(elements.strip(',').split(','))
                elements = ""
            stack.append(c)
        elif c == "}":
            # Find last {
            index = len(stack) - 1 - stack[::-1].index("{")
            cell = stack[index+1:] + elements.strip(',').split(',')
            # cell = compress(cell)
            stack[index] = cell
            stack = stack[:index+1]
            elements = ""
        elif c != " ":
            elements += c
    

        i += 1

        
    print(stack[0])




solution("a,{c,{a,b}, d},a,e,f")