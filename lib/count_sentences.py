#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value=''):
    self._value = value
  
  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    self._value = value if isinstance(value, str) else print('The value must be a string.')

  def is_sentence(self):
    return True if self._value[len(self._value) - 1] == '.' else False

  def is_question(self):
    return True if self._value[len(self._value) - 1] == '?' else False

  def is_exclamation(self):
    return True if self._value[len(self._value) - 1] == '!' else False

  def count_sentences(self):
    sentences = self._value.replace('?', '.').replace('!', '.').split('.')
    sentence_list = []
    for sentence in sentences:
      if len(sentence) > 0:
        sentence_list.append(sentence)
    
    return len(sentence_list)



    