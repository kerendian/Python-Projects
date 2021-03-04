def read_string(file_name):
    f = open(file_name,"r") 
    text = f.readlines()
    f.close()
    return "\n".join(text)


def remove_punctuation(my_str, puncts):
    str_no_puncts = ""
    for i in my_str:
        if i not in puncts:
            str_no_puncts += i
    return str_no_puncts



def remove_stopwords(my_str, stopwords):
     str_no_stopwords = ""
     my_str_list = my_str.split(" ") 
     for i in my_str_list: #go over the string not by index like in range but by each object in the string
         if i not in stopwords:
             str_no_stopwords = str_no_stopwords + i + " " 
            
     str_no_stopwords=str_no_stopwords[:-1]    
     return str_no_stopwords


def remove_prefix(my_str, prefix_to_remove):    
    prefix_to_remove = tuple(prefix_to_remove) #must be a tuple to use .startswith
    my_str = my_str.split(" ")
    for i in  range(0,len(my_str)): #go over the string by index 
        if my_str[i].startswith(prefix_to_remove):                 
            my_str[i] = ""
    
    return " ".join(my_str)   



def remove_oov(my_str, min_count, oov):
    str_oov = ""
    my_str_list = my_str.split(" ")
    for i in my_str_list:
        if my_str_list.count(i) < min_count:
            str_oov = str_oov + oov + " " 
        else:
            str_oov = str_oov + i + " "          
    str_oov = str_oov[:-1]  
    return str_oov


def remove_spaces(my_str):
    str_no_spaces = ""
    my_str_list = my_str.split(" ")
    for i in my_str_list: #go over the string not by index like in range but by each object in the string
        if i != "":
            str_no_spaces = str_no_spaces + i + " "  
    str_no_spaces = str_no_spaces[:-1] 
    return str_no_spaces



def clean_text(my_str, puncts_to_remove, stop_words, min_count, oov, prefix_to_remove):
    my_str = my_str.lower()
    my_str = remove_punctuation(my_str, puncts_to_remove)
    my_str = remove_stopwords(my_str, stop_words)
    my_str = remove_prefix(my_str, prefix_to_remove)
    my_str = remove_oov(my_str, min_count, oov)
    my_str = remove_spaces(my_str)
    return my_str



def get_word2count(my_str):
    my_dict = {}
    my_str_list = my_str.split(" ")
    for i in my_str_list :
        val = my_str_list.count(i) 
        my_dict[i] = val
    return my_dict
my_str = clean_text(read_string("baseball2.txt"), ["\n","\t",'?',"+","<",">",'!',"=",'"',")","(","`",".",',',"#","%","//","'",":","$","-","_","@","~",";"], ['i','am','he','she','it','on','is','are','does','do','you','me','we','in','when','why','how','what'], 2, '[PAD]' , ['http://','https://'])


def get_count2words(my_str):
    my_dict = {} # does it need to be a diffrent dict name than the function above?
    my_str_list = my_str.split(" ")
    for i in my_str_list :
        my_dict.setdefault(my_str_list.count(i), [])      
        if i not in my_dict[my_str_list.count(i)] : 
            my_dict[my_str_list.count(i)].append(i)    
    return my_dict



def top_n_words(n, count2words_dict):
    lst_n_words = []
    list_keys = sorted(count2words_dict.keys(), reverse=True) #list of the keys
    for key in list_keys:
        for val in count2words_dict.get(key) :
            invalid_lst = ['',[],None]
            if val not in invalid_lst :
                lst_n_words.append(val)     
    return lst_n_words[:n]
    
#print(top_n_words(4,get_count2words(read_string("baseball2.txt"))))


def compare_texts(n, text_path1, text_path2):
    
    my_str1 = read_string(text_path1)
    my_str1 = clean_text(my_str1, ["\n","\t",'?',"+","<",">",'!',"=",'"',")","(","`",".",',',"#","%","//","'",":","$","-","_","@","~",";"], ['i','am','he','she','it','on','is','are','does','do','you','me','we','in','when','why','how','what'], 2, '[PAD]' , ['http://','https://'])
    my_dict1 = get_count2words(my_str1)
    n_word_list1 = top_n_words(n, my_dict1)
    
    my_str2 = read_string(text_path2)
    my_str2 = clean_text(my_str2, ["\n","\t",'?',"+","<",">",'!',"=",'"',")","(","`",".",',',"#","%","//","'",":","$","-","_","@","~",";"], ['i','am','he','she','it','on','is','are','does','do','you','me','we','in','when','why','how','what'], 2, '[PAD]' , ['http://','https://'])
    my_dict2 = get_count2words(my_str2)
    n_word_list2 = top_n_words(n, my_dict2)
    
    x = n_word_list2
    y = n_word_list1
    count = 0
    for i in x:
        if i in y:
            count += 1
    return count







