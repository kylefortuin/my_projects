import unittest 
from word_processor import convert_to_word_list,words_longer_than,most_used_character,words_lengths_map,letters_count_map

class Third_test(unittest.TestCase):
    #convert_to_word_list
    def test_convert_punctuation_spaces_caps(self):
        self.assertEqual(convert_to_word_list("So.What,          have we here?"),['so','what','have','we','here'])
    def test_convert_digit(self):
        self.assertEqual(convert_to_word_list(1234),-1)
    def test_convert_empty(self):
        self.assertEqual(convert_to_word_list(""),[])
    
    #words_longer_than
    def test_words_longer_than(self):
        self.assertEqual(words_longer_than(5,"nickelback -Here And Now"),['nickelback'])
    def test_words_longer_than_digit(self):
        self.assertEqual(words_longer_than("","nickelback -Here And Now"),-1)
    def test_words_longer_than_str(self):
        self.assertEqual(words_longer_than(4,123),-1)
    def test_words_longer_than_digit(self):
        self.assertEqual(words_longer_than(12,""),[])

        
    #words_lengths_map
    def test_words_lengths_map(self):
        self.assertEqual(words_lengths_map("this is this long"),{2: 1,4: 3})
    def test_words_lengths_map_empty(self):
        self.assertEqual(words_lengths_map(""),{})
    def test_words_lengths_map_digit(self):
        self.assertEqual(words_lengths_map(123),-1)
        
    # letters_count_map

    def test_letters_count_map(self):
        self.assertEqual( letters_count_map("this is the test text"),{"a":0,"b":0,"c":0,"d":0,"e":3,"f":0,"g":0,"h":2,"i":2,"j":0,"k":0,"l":0,"m":0,
                     "n":0,"o":0,"p":0,"q":0,"r":0,"s":3,"t":6,"u":0,"v":0,"w":0,"x":1,"y":0,"z":0})
    def test_letters_count_map_empty(self):
        self.assertEqual( letters_count_map(""),{"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,
                     "n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0})
    def test_letters_count_map_digit(self):
        self.assertEqual( letters_count_map(123),-1)
        
    #most_used_characters

    def test_most_used_character(self):
        self.assertEqual(most_used_character("Long but longer"),"l")
    def test_most_used_character_digit(self):
        self.assertEqual(most_used_character(123),-1)
    def test_most_used_character_empty(self):
        self.assertEqual(most_used_character(""),None)
    