def convert_to_flat_dict(kv_list):
    flat_dict = dict(kv_list)
    return flat_dict

# Example usage:
kv_list = [('name', 'Hanzala'), ('age', 24), ('city', 'Thane')]
flat_dict = convert_to_flat_dict(kv_list)
print("Flat Dictionary:", flat_dict)
