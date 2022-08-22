class Term:
    def __init__(self, init_dict):
        self.full_dict = init_dict
        self.index = list(self.full_dict.keys())[0]
        self.value = self.full_dict[self.index]

    def to_known(self):
        self.value["known"] = True

    def to_unknown(self):
        self.value["known"] = False


# init_dict_1 = {
#     1:
#     {
#         "French": "word_french",
#         "English": "word_english",
#         "known": None
#     }
# }
#
# term_1 = Term(init_dict_1)
# print(term_1.value["known"])
# term_1.to_unknown()
# print(term_1.full_dict)

