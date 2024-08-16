def solution(elements):
    num=len(elements)
    elements=elements*2
    elementsset=set()
    for i in range(1,num+1):
        for j in range(num):
            elementsset.add(sum(elements[j:j+i]))
    return len(elementsset)