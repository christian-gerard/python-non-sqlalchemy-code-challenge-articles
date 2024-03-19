#!/usr/bin/env python3


# from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")
magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("Skate", "Skate")
magazine_3 = Magazine("Thrasher", "Skate")
# article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
# article_2 = Article(author_1, magazine_1, "Dating life in NYC")
# article_3 = Article(author_2, magazine_2, "How to be TEST")
# article_4 = Article(author_2, magazine_2, "TEST TEST TEST TES")
# article_5 = Article(author_2, magazine_2, "TESTS SSS TEST")
# article_6 = Article(author_2, magazine_2, "1234")
# article_7 = Article(author_2, magazine_2, "56")





print(Magazine.top_publisher())


    # don't remove this line, it's for debugging!

