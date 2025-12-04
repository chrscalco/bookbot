def get_word_number(contents):
    words = len(contents.split())
    return words

def get_ch_number(contents):
    contents = contents.lower()
    ch_dict = {}
    for ch in contents:
        if ch in ch_dict:
            ch_dict[ch] += 1
        else:
            ch_dict[ch] = 1
    return ch_dict

def sort_on(ch_dic):
    return ch_dic["num"]

def sort_dic(ch_dic):
    ch_dic_list = []
    for ch in ch_dic:
        ch_dic_list.append({"char": ch, "num": ch_dic[ch]})
    ch_dic_list.sort(reverse=True, key=sort_on)   
    return ch_dic_list