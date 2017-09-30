#!/usr/bin/python
# -*- coding: utf8 -*-

import re
import time
import sys


alphabet = u"ABCÇDEFGHIİJKLMNOÖPRSŞTUÜVYZ"

def writeFile(filename,W):
	f = open(filename, 'w')
	f.write("\n".join(W))
	f.close()

def readFile (filename):
	f = open(filename, 'r')
	list_ = []
	for line in f:
		list_.append(line[:-1])
	return list_	






def parseWord(w):
	if w in roots:
		return "root"
	else :
		return "not root"

def parseSentences(S):
	W = S.split(" ")
	type_ = []
	for w in W:
		type_.append(parseWord(w))
	return [W,type_]

path = readFile('path.txt')[0]
roots = readFile(path+'/roots.txt')
verbs = readFile(path+'/verbs.txt') 
verb_sub = readFile('data/verb_subfices.txt') 

input_ = sys.argv[1]
print (input_)
sentences = input_.split(".")

print(str(len(sentences))+" tümce:")
for s in sentences:
	print("-> "+s)
	print("\t"+ str(parseSentences(s)))


