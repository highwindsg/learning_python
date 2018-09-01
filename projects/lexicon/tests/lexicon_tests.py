from nose.tools import *
import lexicon

def test_directions():
    assert_equal(lexicon[('direction', 'north')], [('direction', 'south')], [('direction', 'east')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])


