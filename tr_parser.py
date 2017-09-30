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




def checkVowelHarmony(w):
	vovels = list(map(w.lower().count, "aıoueiöü"))
	return sum(vovels[:4])*sum(vovels[4:])==0

def parseWord(w):
	status = ""
	w = w.lower()
	
	noun_canditate = []
	verb_canditate = []
	
	# Seperate roots and compound words
	if w in roots or w in verbs:
		status += "kök"
		if w in roots :
			noun_canditate.append(w)
		if w in verbs :
			verb_canditate.append(w)
	else :
		status += "kök değil"
		
		i = 1 
		while i < len(w):	
			if w[:i] in roots:
				noun_canditate.append(w[:i])
			i += 1
		i = 1 
		while i < len(w):	
			if w[:i] in verbs:
				verb_canditate.append(w[:i])
			i += 1

	if len(noun_canditate) == 1 and len(verb_canditate)==0:
		status += "/"+noun_canditate[0] +"-"+w[len(noun_canditate[0]):]
	elif len(noun_canditate) == 0 and len(verb_canditate)==1:
		status += "/"+verb_canditate[0] +"-"+w[len(verb_canditate[0]):]
	elif len(noun_canditate) == 1 and len(verb_canditate)==1:
		status += "/-nesne yada eylem" 
	else:
		for N in noun_canditate:
			pass
	#status +="-nesne:"+str(noun_canditate)+"-eylem:"+str(verb_canditate)

	"""
	if checkVowelHarmony(w):
		status += "/TR"
	else:
		status += "/TR değil"
	"""
	return status, 

def parseSentences(S):
	W = S.split(" ")
	type_ = []
	for w in W:
		type_.append(parseWord(w))
	return type_


def parseParagraf():
	arg = sys.argv[1]
	F = True
	check = arg.split(".")
	for s in check[1:]:
		if s[0]!=" ":
			print("noktadan sonra boşluk koyun !!")
			F = False
	sentences = arg.split(". ")
	return sentences,F

path = readFile('path.txt')[0]
roots = readFile(path+'/roots.txt')
verbs = readFile(path+'/verbs.txt') 
verb_sub = readFile('data/verb_subfices.txt') 


sentences,flag = parseParagraf()
if flag : 
	print(str(len(sentences))+" tümce:")
	for s in sentences:
		print("-> "+s)
		print("\t"+ str(parseSentences(s)))


