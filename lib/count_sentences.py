#!/usr/bin/env python3

class MyString:
    '''A string with additional methods.'''
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        '''The string value.'''
        return self._value
    
    @value.setter
    def value(self, value):
        if type(value) is not str:
            print("The value must be a string.")
            return
        self._value = value

    def is_sentence(self):
        '''Returns True if value ends with a period and False otherwise.'''
        return self.value.endswith('.')

    def is_question(self):
        '''Returns True if value ends with a question mark and False otherwise.'''
        return self.value.endswith('?')

    def is_exclamation(self):
        '''Returns True if value ends with an exclamation mark and False otherwise.'''
        return self.value.endswith('!')

    def count_sentences(self):
        '''Returns the number of sentences in the value.'''
        self.value = self.value.replace('!', '.')
        self.value = self.value.replace('?', '.')
        return len([sentence for sentence in self.value.split('.') if sentence])
