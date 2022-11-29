# ------------------------------------------------------------------------
# This module is implementing hash table node object.
#
# Author: Shuting Chen
# Date Created: 10/28/2022
# Date Last Modified: 11/8/2022
# ------------------------------------------------------------------------

class TableNode:
    def __init__(self, key, value, next):
        # initialize attributes
        self.key = key
        self.value = value
        self.next = next
        self.primary_insertion = False

