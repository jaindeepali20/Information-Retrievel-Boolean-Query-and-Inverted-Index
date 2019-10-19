# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 02:28:21 2019

@author: Deepali
"""

import sys
import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument("input_corpus_file")
#parser.add_argument("output")
#parser.add_argument("input")
#
#args = parser.parse_args()
#
#input_corpus_file = args.input_corpus_file
#output = args.output
#input_1 = args.input

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing
       
    def print_all_vals(self):
        node = self # start from the head node
        while node != None:
            print (node.val, end =" ") # access the node value
            node = node.next # move on to the next node
           
    def compare(self,other):
        if self.val > other.val:
            return 1
        if self.val == other.val:
            return 0
        if self.val < other.val:
            return -1

def insert_new_node(head_node,new_val):
    node = head_node
    prev_node = node
    while node != None:
        if node.val == new_val:
            break
        elif node.val > new_val:
            old_next_node = node
            prev_node.next = Node(new_val)
            prev_node = node
            prev_node.next = old_next_node
        elif node.next == None:
            node.next = Node(new_val)
        else:
            prev_node = node
            node = node.next

            
            
def get_postings(index,term_list):
    global count_terms_in_a_sentence
    count_terms_in_a_sentence = 0
    ls_get_postings = []
    
    node = index.get(term_list)
    while node != None:
        count_terms_in_a_sentence=count_terms_in_a_sentence+1
        ls_get_postings.append(node.val+"")
        node = node.next

    return ls_get_postings
    f.close() 
      
def daat_and(index,term_list):
    ls_daat_and = []
    postings_lists = []
    output = []
    exit_while = False
    max_updated = False
    number_of_comparisons = 0
    curr_max_doc_id = ''
    for i in range(len(term_list)):
        postings_lists.append(index.get(term_list[i]))
        #ls_daat_and.append(term_list[i]+" ")
    for i in range(len(postings_lists)):
        if postings_lists[i].val > curr_max_doc_id:
            number_of_comparisons += 1
            curr_max_doc_id = postings_lists[i].val
    while not exit_while:
        max_updated = False
        for i in range(len(postings_lists)):
            if postings_lists[i].val in output:    # condition reached when a doc_id has just been added to the output
                postings_lists[i] = postings_lists[i].next
                if postings_lists[i] == None:
                    exit_while = True
                elif postings_lists[i].val > curr_max_doc_id:
                    number_of_comparisons += 1
                    curr_max_doc_id = postings_lists[i].val
                    max_updated = True
            elif postings_lists[i].val < curr_max_doc_id:    # condition reached when the posting list's current doc_id is below max
                while postings_lists[i] != None and postings_lists[i].val < curr_max_doc_id:    # increment the pointer until node.val is = or > than current max doc id
                    number_of_comparisons += 1
                    postings_lists[i] = postings_lists[i].next
                if postings_lists[i] == None:
                    exit_while = True
                elif postings_lists[i].val > curr_max_doc_id:
                    number_of_comparisons += 1
                    curr_max_doc_id = postings_lists[i].val
                    max_updated = True
        if ((not exit_while) and (not max_updated)):
            output.append(postings_lists[0].val)

    if len(output) > 0:
        for i in range(len(output)):
            ls_daat_and.append(output[i]+"")
    else:
        ls_daat_and.append("empty\n")
    
    global l_o_o
    l_o_o = len(output)
    global n_o_c
    n_o_c = number_of_comparisons
    
    return ls_daat_and
    

def daat_or(index,term_list):
    ls_daat_or = []
    postings_lists = []
    number_of_comparisons = 0
    output_set = set()
    output = []
    for i in range(len(term_list)):
        postings_lists.append(index.get(term_list[i]))
        #ls_daat_or.append(term_list[i]+" ")
    for i in range(len(postings_lists)):
        node = postings_lists[i]
        while node != None:
            if node.val not in output_set:
                output.append(node.val)
            output_set.add(node.val)
            node = node.next
            number_of_comparisons += 1
    if len(output) > 0:
        for i in range(len(output)):
            ls_daat_or.append(output[i]+"")
    else:
        ls_daat_or.append("empty\n")
    global l_o_o1
    global n_o_c1
    l_o_o1 = len(output)
    n_o_c1 = number_of_comparisons
    ls_daat_or=sorted(ls_daat_or)
    return ls_daat_or
    

def TF_IDF(index,term_list):
    
     print('TF-IDF')
#     f.write("TF-IDF")
#     #l = get_postings(index, ['bending'])
#     print(l_o_o)
#     print(doc1_length)
#     TF = l_o_o/doc1_length
#     print(TF)
    
#     print(line)
#     print(count_terms_in_a_sentence)
#     IDF = line/count_terms_in_a_sentence
#     print(TF)
#     TF_IDF = TF * IDF
     
     
    

    

#splitting terms on the basis of tab delimiter

with open("input_corpus.txt", "r") as input_corpus:
    tokenized_list = []
    global no_of_sentences 
    no_of_sentences = 0
    global no_of_terms
    no_of_terms = []
    
    for line in input_corpus:
        doc = line.split("\t")
        no_of_sentences=no_of_sentences+1
        tokenized_list.append([doc[0], doc[1].split()])
        no_of_terms.append(len(doc[1]))
    
    global tokenized_list_length 
    tokenized_list_length = len(tokenized_list)
        
index = {}
count = 0
for i in range(len(tokenized_list)):
    doc_id = tokenized_list[i][0]
    for j in range(len(tokenized_list[i][1])):
        term = tokenized_list[i][1][j]
        
        (term, doc_id) in map
             map[(term, doc_id)] = map[(term, doc_id)]+1 

            
        if(term in index):
            insert_new_node(index.get(term),doc_id)
        else:
            index[term] = Node(doc_id)
            
        tf = map[(term, doc_id)]/no_of_terms[i]

def write_list(lst):
    str = ""
    for i in lst:
        str = str + i + " "
    return str.strip()
    

with open("Project2_Sample_input.txt", "r") as ip:
    f = open("outputfile.txt", "w+")
    for i in ip:
        query = i.split()
        
        for j in query:
            f.write("GetPostings\n")
            f.write(j+"\n")
            f.write("Postings list: ")
            ps = get_postings(index, j)
            s = write_list(ps)
            f.write(s)
            f.write("\n")
        
        f.write("DaatAnd\n")
        f.write(write_list(query))
        f.write("\n")
        f.write("Results: ")
        da = daat_and(index, query)
        d1 = write_list(da)
        f.write(d1+"\n")
        f.write("Number of documents in results: "+str(l_o_o)+"\n")  
        f.write("Number of comparisons: "+str(n_o_c)+"\n") 
        
        #TF_IDF(index, query)
        f.write("TF-IDF\n") 
        f.write("Results: ")
        f.write("\n")
        
        f.write("DaatOr\n")
        f.write(write_list(query))
        f.write("\n")
        f.write("Results: ")
        do = daat_or(index, query)
        d2 = write_list(do)
        f.write(d2+"\n")
        f.write("Number of documents in results: "+str(l_o_o1)+"\n")  
        f.write("Number of comparisons: "+str(n_o_c1)+"\n") 
        
        #TF_IDF(index, query)
        f.write("TF-IDF\n")
        f.write("Results: ")
        f.write("\n")
        
        f.write("\n")
        
    f.close()   
    
        
