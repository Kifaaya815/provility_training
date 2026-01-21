#list
marks_list=[75, 80, 90, 80, 75, 85]
print("Marks:",marks_list)
print("Total no. of marks:",len(marks_list))

#tuple
marks_tuple=tuple(marks_list)
print("Marks tuple:",marks_tuple)
print("Highest mark:",max(marks_tuple))

#set
marks_set=set(marks_list)
print("Marks set:",marks_set)
print("Number of unique marks:",len(marks_set))

#dictionary
marks_dict={"Alice":75,
            "Bob":80,
            "Charlie":90,
            "David":80,
            "Eva":75,
            "Frank":85}
print("Marks Dictionary:",marks_dict)
print("Charlie's mark:",marks_dict["Charlie"])
marks_dict["Bob"]=88
print("Updated Dictionary:",marks_dict)