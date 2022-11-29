# ------------------------------------------------------------------------
# This module is implementing hash table class, including its related
# properties and functions.
#
# Author: Shuting Chen
# Date Created: 10/28/2022
# Date Last Modified: 11/8/2022
# ------------------------------------------------------------------------

from tablenode import TableNode
import random
import math


class HashTable:
    def __init__(self, table_size, bucket_size, collision_scheme, modulo_scheme):
        """
            Class constructor for HashTable object
                table_size: size of the hash table
                bucket_size: number of buckets
                collision_scheme: linear/quadratic/chaining
                modulo_scheme: div/mul (division or multiplication)

            Return:
                none
        """
        # initialize attributes
        self.table_size = table_size
        self.bucket_size = bucket_size
        self.rows = int(table_size / bucket_size)
        self.hash_table = self.declare_table_slots()
        self.pri_collision = 0
        self.sec_collision = 0
        self.c1 = 0.5
        self.c2 = 0.5
        self.occupation_ct = 0
        self.modulo_scheme = modulo_scheme
        self.failed_values = []
        self.collision_scheme = self.collision_scheme_translation(collision_scheme)
        if self.collision_scheme == 3:
            self.space = self.declare_free_space()

    def declare_free_space(self):
        """
            Declare stack for recording a free space

            Return:
                none
        """
        random_indices = list(range(1, self.rows))
        random.shuffle(random_indices)
        return random_indices

    def declare_table_slots(self):
        """
            Declare slots for the hash table

            Return:
                none
        """
        hashtable = []
        # initiate slot(s) per row
        for i in range(0, self.rows):
            if self.bucket_size == 1:
                hashtable.append(TableNode(-1, -1, -1))
            else:
                slot = []
                for j in range(0, self.bucket_size):
                    slot.append(TableNode(-1, -1, -1))
                hashtable.append(slot)
        return hashtable

    def collision_scheme_translation(self, collision_scheme):
        """
            Declare slots for the hash table
                collision_scheme: linear/quadratic/chaining
            Return:
                return integer 1/2/3 to represent linear/quadratic/chaining
                or return -1 as an error flag
        """
        # save collision_scheme into integer representation, case insensitive
        if collision_scheme.lower() == "linear" or collision_scheme.lower() == "linear probing":
            return 1
        elif collision_scheme.lower() == "quadratic" or collision_scheme.lower() == "quadratic probing":
            return 2
        elif collision_scheme.lower() == "chaining":
            return 3
        else:
            return -1  # error flag for collision_scheme

    def collision_scheme_trans_back(self):
        """
            Reverse integer of collision_scheme back to string formate
                collision_scheme: linear/quadratic/chaining
            Return:
                return integer 1/2/3 to represent linear/quadratic/chaining
                or return -1 as an error flag
        """
        # save collision_scheme into integer representation, case insensitive
        if self.collision_scheme == 1:
            return "linear"
        elif self.collision_scheme == 2:
            return "quadratic"
        elif self.collision_scheme == 3:
            return "chaining"

    def bucket_is_full(self, key):
        """
            Check if a bucket at a given key is full

            Return:
                return True if that bucket is full, otherwise False
        """
        flag = True
        for i in self.hash_table[key]:
            if i.value == -1:
                flag = False
                break
        return flag

    def bucket_insert(self, key, value):
        """
            Insert a value into a bucket at a given key
                value: the value to be inserted into a bucket
                key: the key of the bucket

            Return:
                none
        """
        if self.bucket_size == 1:
            self.hash_table[key].key = key
            self.hash_table[key].value = value
        else:
            for i in self.hash_table[key]:
                if i.value == -1:
                    i.key = key
                    i.value = value
                    break

    def insert(self, value, modulo, c1, c2):
        """
            Insert a value into hash table by a given modulo
                value: the value to be inserted into a hashtable
                modulo: the modulo value
                c1: c1 is only for quadratic probing, default: 0.5
                c2: c2 is only for quadratic probing, default: 0.5

            Return:
                none
        """
        # save constants for quadratic probing
        self.c1 = c1
        self.c2 = c2
        if self.collision_scheme == 1 or self.collision_scheme == 2:
            self.probe_insert(value, modulo)
        elif self.collision_scheme == 3:
            self.chaining_insert(value, modulo)

    def probing(self, value, i, modulo):
        """
            calculate the next key for probing
                value: the value to be probed
                i: how far the value is going to probe
                modulo: the modulo value

            Return:
                the new key after probing
        """
        # calculate new key
        if self.collision_scheme == 1:
            temp_key = self.hash_function(value + i, modulo)
        elif self.collision_scheme == 2:
            temp_key = self.hash_function(value + self.c1 * i + self.c2 * i * i, modulo)

        # manually assign key 40 to key 0
        if self.bucket_size != 1:
            if temp_key == self.rows:
                temp_key = 0

        return math.floor(temp_key)

    def probe_insert(self, value, modulo):
        """
            Probing approach for both linear and quadratic probing
                value: the value to be probed
                modulo: the modulo value

            Return:
                none
        """
        # calculate key index
        key = self.hash_function(value, modulo)

        if self.bucket_size == 1:
            # check availability
            if self.hash_table[key].value == -1:
                # key is available
                self.hash_table[key].key = key
                self.hash_table[key].value = value
                self.hash_table[key].primary_insertion = True
                self.occupation_ct += 1
            else:
                # key is occupied
                i = 0
                fail_insertion = False
                # probe to next available slot
                new_key = self.probing(value, i, modulo)
                while self.hash_table[new_key].value != -1:
                    # check i is less than m
                    if i == self.rows:
                        self.failed_values.append(value)
                        fail_insertion = True
                        break
                    # record collision
                    if self.hash_table[new_key].primary_insertion:
                        self.pri_collision += 1
                    else:
                        self.sec_collision += 1
                    # update the next probe location
                    i += 1
                    new_key = self.probing(value, i, modulo)
                # insert into new slot
                if not fail_insertion:
                    self.bucket_insert(new_key, value)
        else:
            # manually assign key 40 to key 0
            if key == self.rows:
                key = 0
            # when bucket size greater than 1, insert value into bucket
            if not self.bucket_is_full(key):
                self.bucket_insert(key, value)
            else:
                # key is occupied
                i = 1
                fail_insertion = False
                self.pri_collision += 1
                # probe to next available slot
                new_key = self.probing(value, i, modulo)
                while self.bucket_is_full(new_key):
                    # check i is less than m
                    if i == self.rows:
                        self.failed_values.append(value)
                        fail_insertion = True
                        break
                    # record collision
                    self.sec_collision += 1
                    # update the next probe location
                    i += 1
                    new_key = self.probing(value, i, modulo)
                # insert into new slot
                if not fail_insertion:
                    self.bucket_insert(new_key, value)

    def chaining_insert(self, value, modulo):
        """
            Insert a value into the hash table by chaining approach
                value: the value to be probed
                modulo: the modulo value

            Return:
                none
        """
        # calculate key index
        key = self.hash_function(value, modulo)
        if self.bucket_size == 1:
            if self.hash_table[key].value == -1:
                # fill an available slot
                self.hash_table[key].key = key
                self.hash_table[key].value = value
                self.hash_table[key].primary_insertion = True
                self.occupation_ct += 1
            else:
                # slot at key is occupied
                # check collide situation
                if self.hash_table[key].primary_insertion:
                    self.pri_collision += 1
                else:
                    self.sec_collision += 1

                if len(self.space) != 0:
                    new_key = self.space[0]
                    self.space.pop(0)
                    temp = self.hash_table[key].next
                    self.hash_table[key].next = self.hash_table[new_key]
                    self.hash_table[new_key].value = value
                    self.hash_table[new_key].key = new_key
                    self.hash_table[new_key].next = temp
                else:
                    self.occupation_ct += 1
        else:
            print("Only consider chaining when bucket size is 1. ")

    def hash_function(self, value, modulo):
        """
            Calculate the key to save the value on the hash table
                key: the value to be probed
                modulo: the modulo value

            Return:
                the key to save the value
        """
        if self.modulo_scheme == "div":
            return value % modulo
        elif self.modulo_scheme == "mul":
            # m(kA mod1):
            return math.floor(120 * ((0.618 * value) % 1))

    def load_factor(self):
        """
            Calculate the load factor for the hash table

            Return:
                the load factor
        """
        return self.occupation_ct / self.table_size

    def print_table_info(self, n_ct, modulo):
        """
            Output the hash table and its information

            Return:
                text about the hash table
        """
        # get the properties of the table
        if self.modulo_scheme == "div":
            output = "Method: division " + "mod" + str(modulo) + "\n"
        elif self.modulo_scheme == "mul":
            output = "Method: multiplication m(kA mod1)\n"
            output += "\tm = " + str(self.rows) + "; A = 0.618\n"
        output += "Hash Table size: " + str(self.table_size) + "\n"
        output += "\tbucket size: " + str(self.bucket_size) + "\n"

        # get the collision statistics
        output += "Collision handling scheme: " + self.collision_scheme_trans_back() + "\n"
        if self.collision_scheme == 2:
            output += "\tc1 = " + str(self.c1) + "; c2 = " + str(self.c2) + "\n"
        output += "\tprimary collisions: " + str(self.pri_collision) + "\n"
        output += "\tsecondary collisions: " + str(self.sec_collision) + "\n"
        output += "\ttotal collisions: " + str(self.pri_collision + self.sec_collision) + "\n"
        output += "Keys not inserted: " + str(self.failed_values) + "\n"
        output += "Load factor: " + str((n_ct - len(self.failed_values)) / self.table_size) + "\n"

        # print the table
        output += "Hash table: \n"
        if self.bucket_size == 1:
            line = []
            int_ct = 0
            for i in self.hash_table:
                if i.value != -1:
                    line.append(str(i.value))
                else:
                    line.append("----")
                int_ct += 1
                if int_ct == 5:
                    output += '    '.join(line) + "\n"
                    line = []
                    int_ct = 0
            output += '    '.join(line) + "\n"
        else:
            line_index = 0
            for i in self.hash_table:
                line = []
                line_index += 1
                line.append(str(line_index))
                for j in i:
                    if j.value != -1:
                        line.append(str(j.value))
                    else:
                        line.append("----")
                output += '    '.join(line) + "\n"
        return output
