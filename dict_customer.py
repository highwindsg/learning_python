#!/usr/bin/env python3

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("birthdate"))    # If the key is not in the dict then will
                                    # output as None, rather then error message.
print(customer.get("birthdate", "Jan 1 1980"))  # Or if birthdate is None, then
                                                # will take the second param as
                                                # the default value.
customer["name"] = "Jack Smith"     # Changing value of name var to 'Jack Smith'
                                    # is a permanent change.
print(customer.get("name"))
print(customer)     # Printing out the whole dict will show the new name as well.

