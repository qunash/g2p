from unittest import main, TestCase
import os
from g2p.cors import Correspondence
from g2p.transducer import Transducer

class TransducerTest(TestCase):
    ''' Basic Transducer Test
    '''

    def setUp(self):
        self.test_cor = Correspondence([{'from': 'a', "to": 'b'}])
        self.test_cor_rev = Correspondence([{"from": 'a', "to": 'b'}], True)
        self.test_cor_moh = Correspondence(language={"lang": "moh", "table": "orth"})
        self.test_cor_ordered = Correspondence([{"from": "a", "to": "b"}, {"from": "b", "to": "c"}])
        self.test_trans = Transducer(self.test_cor)
        self.test_trans_ordered = Transducer(self.test_cor_ordered)
        self.test_trans_rev = Transducer(self.test_cor_rev)
        self.test_trans_moh = Transducer(self.test_cor_moh, True)

    def test_ordered(self):
        transducer = self.test_trans_ordered('a', True)
        self.assertEqual(transducer[0], 'c')
        self.assertEqual(transducer[1], [((0, "a"), (0, "c"))])

    def test_forward(self):
        self.assertEqual(self.test_trans('a'), "b")
        self.assertEqual(self.test_trans('b'), "b")

    def test_backward(self):
        self.assertEqual(self.test_trans_rev("b"), 'a')
        self.assertEqual(self.test_trans_rev("a"), 'a')
    
    def test_lang_import(self):
        self.assertEqual(self.test_trans_moh('kawennón:nis'), 'kawẽnonnis')

if __name__ == "__main__":
    main()
    