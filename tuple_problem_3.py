def swap_elements(list_of_tuple):
    list2 = []

    for element in list_of_tuple:
        f_element = element[0]
        s_element = element[-1]
        m_elements = element[1:-1]
        new_element = (s_element,)+m_elements+(f_element,)
        list2.append(new_element)
    return list2
        

list_of_tuple1 = [(1,2,3,4),(4,5,6,7),(7,8,9,10)] 

print(swap_elements(list_of_tuple1))

    