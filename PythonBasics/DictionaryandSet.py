from numpy.ma.core import size

print("--------------------------------------------- DICT ------------------------------------------------------------")
# A dictionary is mutable and unordered , and it don't allow duplicate keys
info={
    "name" : "TAFFIKUDDIN KHAN", # Note : a key can not be a list or tuple in dictionary
    "subjects" : ["python","java","sql"],  #a dictionary can contain list and tuple also
    "age" : 20,
    "marks" :89.6,
    "is_adult" : True
}
print(info)
info["name"] = "LORD INOSUKE" #update the name . while updating the old value will be overwritten by new value , python don't allocate extra memory for this
print(info["name"],info["subjects"],info["is_adult"]) #There is no index concept in dict so we have to access the value by only accessing the key
info["is_good"] = True  #through this can add new key : value pairs in the dictionary
print(info)

student = {  # A nested dictionary , student dictionary

    "Name" : "TANJIRO KAMADO",

    "subjects":{  # subject dictionary

        "math":{  # individual subject dictionary with pass and fail  , so the flow is student -> subjects -> math{pass,98} , science{fail,15} , english{pass,67}
            "pass" : 98
        },
        "science":{
          "fail" : 15
        },
        "English":{
            "pass":67
        }

    }
}
print(student)

#                           =========================== METHODS =================================

print(student["subjects"]["math"]["pass"]) # Access individual record
print(student.keys()) #return all the keys from student dictionary
print(student.values()) #return all the values from student dictionary
print(student.items()) #return all the key and value pairs as tuple
pairlist = list(student.items()) #type casting to list type , list can contain dictionary and vice versa is also possible
print(pairlist[0]) #after converting into list access element base on the index
print(type(pairlist)) #checking the type of pairlist
print(student["subjects"]["math"].get("pass")) # get the value of the math key
student["subjects"]["math"].update({"fail":45}) #added a new record in math dictionary
print(student)

student["subjects"]["math"] = {"fail":15} #update the existing record in math dictionary
print(student)

print("---------------------------------------------------- SETS -----------------------------------------------------")
nums={1,2,2,3,3,3,3,4,5,6,7,8} #et is the collection of unordered items ,if any element repeats then it will keep that element once
print(nums)
# we can't store list and dictionary in a set , bcz the elements of set is immutable and list,dictionaries are mutable
collection = set()  #empty set declaration
print(type(collection))

#                   ================================ METHODS ======================================

collection.add(1)#add value in an empty set
collection.add(2)
collection.add(3)
collection.add(4) #remove element from the set by passing that exact value
collection.remove(1)
print(len(collection))
collection.pop() #remove any random value from the set
collection.clear() #empty the set
print(len(collection))
print(collection)

print(collection.union(nums))  # union both collection and nums set , it don't affect the original sets at all
print(collection.intersection(nums))


#practice questions -------------------------------
#store the following word meaning in a python dictionary
words={
    "table" : ["a piece of furniture","list of facts and figures"],
    "cat" : "a small animal"
}
print(words)

#you are given a list of subjects for students, assume one classroom is required for 1 subject . how many classrooms are needed by all students
classrooms = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print("There are",len(classrooms),"classrooms need for each subject")

#wap to store 9 and 9.0 in a set and print
values={ #method 1  in a tuple assign the value with the expected data type
    ("float",9.0),
    ("int",9)
}
values1 = {9,"9.0"} #method 1 , treat one of the values as string
print(values1)
print(values)