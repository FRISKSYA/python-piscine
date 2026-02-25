ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}
# your code here

ft_list[1] = "World!"


ft_list_tuple = list(ft_tuple)
ft_list_tuple[1] = "France!"
ft_tuple = tuple(ft_list_tuple)

# ft_tuple = (ft_tuple[0], "France!")
# is better.

ft_set.discard("tutu!")
ft_set.add("Paris!")

ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
