# Chapter:04 -----> data structures in python
# -------------------------------------------
# 01. mutable and immutable objects
# 02. string data structure
# 03. list data structure
# 04. tuple data structure
# 05. set data structure
# 06. dict data structure
# 07. sample programs









                                            # 01. mutable and immutable objects
                                            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~







# mutable objects:
# ----------------
# once if an object is created, if we are trying to perform modifications on the existing object,
#  those modifications will be reflected on the same object, then such type of objects are called as mutable objects.

# Ex: list, set and dict




# immutable objects:
# ------------------
# once if an object is created, if we are trying to perform modifications on the existing object,
#  with those modifications a new object will be created modifications wn't be reflected on the same object,
#  then such type of objects are called as immutable objects.

# Ex: tuple, string and fundamental data types

# Define a dictionary with duplicate keys (the last value will be kept)
dict = {1: 'one', 2: 'two', 1: 'thousand'}  # The value 'one' is overwritten by 'thousand'

# Overwrite the value for key 1
dict[1] = 'zero'  # The value 'thousand' is overwritten by 'zero'

# Print the dictionary
print(dict)





# 02. string data structure
# -------------------------
# introduction:
# -------------
# ==> collection or sequence or group of characters is called as string.
# ==> <class 'str'>
# ==> we can represent string objects in the following ways

#     1. single quotes
#     2. double quotes
#     3. triple single quotes
#     4. triple dounle quotes

# Ex:
# ---
# s1 = "Hai"
# s2 = 'Hi'
# s3 = """Bye"""
# s4 = '''Bi'''


# index concept:
# --------------
# we can use index and subscript combination to extract individual characters from a string.




# accessing string objects:
# -------------------------
# The following are the various method to access string objects

# 1) directly we can print
# 2) index concept
# 3) slice operator
# 4) while loop
# 5) for each loop


# Ex:
# ---
# s = "prakash"

# #1) directly we can print
# print(s) #prakash

# #2) index concept
# print(s[0]) #p
# print(s[1]) #r
# print(s[2]) #a
# print(s[3]) #k


# slice operator:
# ---------------
# we can use slice operator to extract(sub-string) or slice the given string.

# syntax:
# 	s[s:s:s]

# 	s ----> start value
# 	s ----> stop value
# 	s ----> step value

# Note: slice operator never generates error.


# operators on string objects
# ---------------------------
# +	string concatenation
# *	string repeatation
# in	membership checking
# not in	membership checking
# <	comparing
# <=	comparing
# >	comparing
# >=	comparing
# ==	comparing
# !=	comparing



                                                # string
# common functions
# ----------------
# len(s)			length of string
# max(s)			max char based on ascii value
# min(s)			min char based on ascii value
# sorted(s)		sorted list will all char in asc order
# sorted(s,reverse=True)	sorted list will all char in desc order
# ord(ch)			returns ascii value of char
# chr(ascii)		returns char value for given ascii



# string specific methods:
# ------------------------
# upper():
# --------
# it converts the given str into upper case

# lower():
# --------
# it converts the given str into lower case

# swapcase():
# -----------
# it converts lower case into upper case and upper case into lower case

# title():
# --------
# each word's first char will be converted into upper case

# capitalize():
# -------------
# sentence first char will be converted into upper case

# startswith():
# -------------
# it returns true if the given string starts with another string else false

# endswith():
# -----------
# it returns true if the given string ends with another string else false

# index(substring):
# -----------------
# it returns index of sub-string in the main string, else it raises error

# find(substring):
# ----------------
# it returns index of sub-string in the main string, else it returns -1

# split(delimiter)
# ----------------
# it splits the given string based on delimiter.

# seperator.join(list)
# --------------------
# it takes seperator and join each element in list with given seperator.

# isalnum():
# ---------- 
# returns True if the given string contains only alpha numeric values else False

# isalpha():
# ----------
# returns True if the given string contains only alphabets else False

# isdigit():
# ----------
# returns True if the given string contains only digits else False

# islower():
# ----------
# returns True if the given string/char is in lower case else False

# isupper():
# ----------
# returns True if the given string/char is in upper case else False

# isspace():
# ----------
# returns True if the given string/char contains only space else False

# list data structure:
# ~~~~~~~~~~~~~~~~~~~~

# introduction:
# -------------
# ==> it is a group of objects of different types.
# ==> it is represented by using []
# ==> it is growable (add/remove/update)
# ==> mutable object
# ==> it is index based data structure
# ==> slicing is allowed
# ==> insertion order is preserved
# ==> duplicates are allowed.


# creation of list objects:
# -------------------------
# 1) []
# 2) [obj1, obj2, obj3, obj4,....]
# 3) list()
# 4) split()
# 5) input() with list()
# 6) eval()


# accessing list objects:
# -----------------------
# 1) directly 
# 2) index concept
# 3) slice operator
# 4) while loop
# 5) for each loop

# nested list objects:
# --------------------
# a list object within another list object is called as nested list.

# list aliasing:
# --------------
# assigning a new reference variable for an existing list object is called as list aliasing. 

# list cloning:
# -------------
# it is used to create a duplicate copy of existing list object. it is possible by using copy() method.

# shallow copy and deep copy
# --------------------------
# once if copy of list object got created, if it contains any nested list objects, then if we perform any modifications on nested list object, those modifications will be reflected for both list pbjects i.e. nested list objects are shared. this type of copy operation is called as shallow copy or normal copy.

# Ex:
# ---
# L1 = [11, 22, 33, [111, 222, 333], 44, 55]
# L2 = L1.copy() #shallow copy


# list comprehension:
# -------------------
# easiest way to create list objects.

# Ex1: increment each element present in a list
# ---------------------------------------------
# OL = [1, 2, 3, 4, 5]
# NL = [i+1 for i in OL]

# Ex2: find factorial of each element present in a list
# -----------------------------------------------------
# import math
# OL = [1, 2, 3, 4, 5]
# NL = [math.factorial(i) for i in OL]

# Ex3: convert every name present in list into upper case
# -------------------------------------------------------
# OL = ["prakash","raju","ram","somu"]
# NL = [i.upper() for i in OL]

# Ex4: extract even numbers from a list
# -------------------------------------
# OL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# NL = [i for i in OL if i%2==0]



                                                            # LIST






# common functions on list
# ------------------------
# len(L) 				length of list
# max(L) 				max element in list
# min(L) 				min element in list
# sorted(L)			sorted list with all elements in asc order
# sorted(L,reverse=True) 	sorted list with all elements in desc order
# sum(L) 				sum of all the elements in list

# list specific methods:
# ----------------------
# append(object)
# --------------
# it is used to add an object into list at the ending.

# insert(index,object)
# --------------------
# it is used to add an object into list at the given index value

# remove(object)
# --------------
# it will remove the given object from the list

# pop()
# -----
# it will remove the element located at last location
# Ex:
# ---
# L = [10, 20, 30, 40]
# print(L) #[10, 20, 30, 40]
# L.pop()
# print(L) #[10, 20, 30]

# pop(index)
# ----------
# it will remove the element located at given location

# Ex:
# ---
# L = [10, 20, 30, 40]
# print(L) #[10, 20, 30, 40]
# L.pop(0)
# print(L) #[20, 30, 40]

# clear()
# -------
# it will remove all the elements from a list


# index(object)
# -------------
# it returns location of the given object

# count(object)
# -------------
# it returns number of occurrences of the given object

# reverse()
# ---------
# it reverse the given list object

# sort()
# ------
# it sorts the given list in asc order
# Ex:
# ---
# L = [10, 30, 20, 50, 40]
# print(L) #[10, 30, 20, 50, 40]
# L.sort()
# print(L) #[10, 20, 30, 40, 50]

# sort(reverse=True)
# ------------------
# it sorts the given list in desc order

# Ex:
# ---
# L = [10, 30, 20, 50, 40]
# print(L) #[10, 30, 20, 50, 40]
# L.sort(reverse=True)
# print(L) #[50, 40, 30, 20, 10]





                                        # 04. tuple data structure
                                        # ------------------------



# introduction:
# -------------
# ==> it is a group of objects of different types.
# ==> it is represented by using ()
# ==> it is not growable 
# ==> immutable object
# ==> it is index based data structure
# ==> slicing is allowed
# ==> insertion order is preserved
# ==> duplicates are allowed.


# creation of tuple objects:
# -------------------------
# 1) ()
# 2) (obj1, obj2, obj3, obj4,....)
# 3) (obj,)
# 4) tuple()
# 5) input() with tuple()
# 6) eval()

# accessing tuple objects:
# -----------------------
# 1) directly 
# 2) index concept
# 3) slice operator
# 4) while loop
# 5) for each loop

# nested tuple objects:
# --------------------
# a tuple object within another tuple object is called as nested tuple.

# tuple aliasing:
# --------------
# assigning a new reference variable for an existing tuple object is called as tuple aliasing. 

# tuple comprehension:
# -------------------
# easiest way to create list objects.

# syntax1: tuple(expr for i in sequence)
# syntax2: tuple(expr for i in sequence if condition)

# Ex
# T1 = (1, 2, 3, 4)
# T2 = tuple(i+1 for i in T1)
# print(T1)
# print(T2)

# common functions on tuple
# ------------------------
# len(L) 				length of tuple
# max(L) 				max element in tuple
# min(L) 				min element in tuple
# sorted(L)			sorted list with all elements in asc order
# sorted(L,reverse=True) 	sorted list with all elements in desc order
# sum(L) 				sum of all the elements in tuple

# tuple specific methods:
# ----------------------
# index(object)
# -------------
# it returns location of the given object

# count(object)
# -------------
# it returns number of occurrences of the given object

# tuple packing and tuple unpacking
# ---------------------------------
# converting individual objects into tuple is called as tuple packing
# converting tuple into individual objects is called as tuple unpacking





                                                # 05. set data structure
                                                # ----------------------


# introduction:
# -------------
# ==> it is a group of objects of different types. (immutable)
# ==> it is represented by using {}
# ==> it is growable (add/remove) 
# ==> mutable object
# ==> it is not index based data structure
# ==> slicing is not allowed
# ==> insertion order is  not preserved
# ==> duplicates are not allowed.

# creation of set objects:
# -------------------------
# 1) set()
# 2) {obj1, obj2, obj3, obj4,....}
# 3) input() with set()
# 4) eval()

# accessing set objects:
# -----------------------
# 1) directly 
# 2) for each loop


# common functions on set
# ------------------------
# len(L) 				length of set
# max(L) 				max element in set
# min(L) 				min element in set
# sorted(L)			sorted list with all elements in asc order
# sorted(L,reverse=True) 	sorted list with all elements in desc order
# sum(L) 				sum of all the elements in set



# set specific methods:
# ----------------------
# add(object)
# ------------
# it adds the given object into set

# Python frozenset()
# ------------------
# returns immutable frozenset object

# Python Set add()
# ----------------
# adds element to a set

# Python Set clear()
# ------------------
# remove all elements from a set

# Python Set copy()
# -----------------
# Returns Shallow Copy of a Set

# Python Set difference()
# -----------------------
# Returns Difference of Two Sets

# Python Set difference_update()
# ------------------------------
# Updates Calling Set With Intersection of Sets

# Python Set discard()
# --------------------
# Removes an Element from The Set

# Python Set intersection()
# -------------------------
# Returns Intersection of Two or More Sets

# Python Set intersection_update()
# --------------------------------
# Updates Calling Set With Intersection of Sets

# Python Set isdisjoint()
# -----------------------
# Checks Disjoint Sets

# Python Set issubset()
# ---------------------
# Checks if a Set is Subset of Another Set

# Python Set issuperset()
# -----------------------
# Checks if a Set is Superset of Another Set

# Python Set pop()
# ----------------
# Removes an Arbitrary Element

# Python Set remove()
# -------------------
# removes the specified element from the set

# Python Set symmetric_difference()
# ---------------------------------
# Returns the symmetric difference of sets

# Python Set symmetric_difference_update()
# ----------------------------------------
# Updates the Set with symmetric difference

# Python Set union()
# ------------------
# Returns the union of sets

# Python Set update()
# -------------------
# Add elements to the set



                                    # dictionary data structure or dict data structure:
                                    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ==> collection of individual objects ---> str, list, tuple, set
# ==> collection of key and value pairs are called as dictionary or dict
# ==> it is represented by using {}
# ==> <class 'dict'>

# Ex:
# ---
# d = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five"}
# print(d) 
# print(type(d))#<class 'dict'>



# ==> index concept is not allowed but keys are acting as index.
# ==> duplicate keys are not allowed but values can be duplicated.

# ==> both keys and values must be objects.
# ==> modifications are allowed.

# key ---> object
# value -> object

# dict methods:
# -------------
# d[key] = value

# it adds key and value pair into the existing dict.


# del d[key]

# it deletes key and value pair from the existing dict



# clear()
# -------
# it clear all the key value pairs from dict


# keys()
# ------
# it returns a list of all keys existed in dict

# values()
# --------
# it returns a list of all values existed in dict

# items()
# -------
# it returns a list of all key and value pairs in the form of tuple

# get(key)
# --------
# it returns a value associated with given key


# get(key,default)
# ----------------
# it returns a value associated with given key if not, it returns default value


# dictionary comprehension:
# -------------------------
# easiest way to create dict is nothing dict comprehension.

# {key_expr:val_expr for i in seq}
# {key_expr:val_expr for i in seq if cond}

# Ex:
# ---
# d = {i:i*i for i in range(1,11)}
# print(d)


