# Transform Python value into multiline string suitable for 
# testing differences with HTMLDiff
# Would have preferred to use json.dumps, but doesn't handle tuples and sets.

# Author: Lyn Turbak
# Created: 2017/11/04

'''
# import json
import simplejson as json
''' 

# import util

seqIndent = 2
dictIndent = 2

def printNice(s): 
    print(stringify(s))

def stringify(val): 
    def valToStrings(val, indent, width):
        '''Returns a list of indented strings that represent val onto strings. 
           * indent is the current indentation level;
           * width is the target width (if value is bigger than that, oh well)
           Heuristically tries to fit compound values on a single line if it can.'''
        strings = []
        if hasDictType(val):
            dictWidth = width-dictIndent
            keyValPairs = sorted(val.items())
            # Simplifying assumption: keys will fit on one line.
            # keyValStringsList is a list of pairs of (1) key and (2) list of strings
            keyValStringsList = [(k, valToStrings(v, 0, dictWidth)) for k,v in keyValPairs]
            compressedDict = compressDict(keyValStringsList)
            if compressedDict and len(compressedDict) <= dictWidth: # use width, not dictWidth
                # Can fit entire dictionary on one line
                strings.append(spaces(indent) + compressedDict)
            else:
                dictStrings = []
                dictStrings.append('{')
                lastKeyValIndex = len(keyValStringsList) - 1
                for (keyValIndex, (key, valStrings)) in enumerate(keyValStringsList):
                    compressedKeyValBinding = compressKeyValBinding(key, valStrings)
                    finalString1 = ',' if keyValIndex != lastKeyValIndex else ''
                    # print "In valToString at compressedKeyValBinding => {}, len = {}, dictWidth = {}".format(
                    #    compressedKeyValBinding, len(compressedKeyValBinding), dictWidth)
                    if compressedKeyValBinding and len(compressedKeyValBinding) <= dictWidth: 
                        # print "Taking then branch"
                        dictStrings.append(spaces(dictIndent) + compressedKeyValBinding + finalString1)
                    elif len(valStrings) == 1:
                        candidateBindingString = (myValToString(key) + ': '+ valStrings[0] + finalString1)
                        if candidateBindingString <= dictWidth: # Binding fits on one line
                            dictStrings.append(spaces(dictIndent) + candidateBindingString)
                        else: # Binding doesn't fit on one line; split key and value into two lines
                            dictStrings.append(spaces(dictIndent) + myValToString(key) + ':')
                            dictStrings.append(spaces(dictIndent*2) + valStrings[0] + finalString1)
                    else: # len(valStrings) => 
                        # print "Taking else branch with valStrings => {}".format(valStrings)
                        lastValIndex = len(valStrings) - 1
                        for (valIndex, valString) in enumerate(valStrings):
                            finalString2 = ',' if keyValIndex != lastKeyValIndex and valIndex == lastValIndex else ''
                            if valIndex == 0:
                                dictStrings.append(spaces(dictIndent) + myValToString(key) + ': ' + valString)
                                  # valString must be startString for compound value. 
                                  # Put it on same line with key. 
                            else:
                                dictStrings.append(spaces(dictIndent*2) # Double nesting: Inside dict + inside binding
                                                   + valString + finalString2)
                dictStrings.append('}')
                strings.extend([spaces(indent) + s for s in dictStrings])                
        elif hasSequenceType(val):
            seqWidth = width-seqIndent
            eltList = sorted(val) if hasSetType(val) else list(val)
            # eltStringss is a list of list of strings
            eltStringss = [valToStrings(elt, 0, seqWidth) for elt in eltList]
            compressedSeq = compressSequence(val, eltStringss) # Returns None if not compressible
            if compressedSeq and len(compressedSeq) <= width: # use width, not seqWidth
                # Can fit entire sequence on one line
                strings.append(spaces(indent) + compressedSeq)
            else: # Add individual lines for elements
                seqStrings = [] # unindented strings
                seqStrings.append(seqStart(val))
                lastOuterIndex = len(eltStringss) - 1
                for (outerIndex, eltStrings) in enumerate(eltStringss):
                    lastInnerIndex = len(eltStrings) - 1
                    for (innerIndex, eltString) in enumerate(eltStrings):
                        outString = (spaces(seqIndent) + eltString
                                     + (',' if outerIndex != lastOuterIndex and innerIndex == lastInnerIndex else ''))
                        seqStrings.append(outString)
                seqStrings.append(seqStop(val))
                strings.extend([spaces(indent) + s for s in seqStrings])
        elif hasStringType(val): 
            strings.append(' '*indent + "'{}'".format(val))
        else: 
            strings.append(str(val))
        return strings
    return '\n'.join(valToStrings(val, 0, 80))

def spaces(n):
    return ' '*n

def seqStart(seq):
    if hasListType(seq):
        return '['
    elif hasTupleType(seq):
        return '('
    elif hasSetType(seq):
        return 'set(['
    else: 
        "***UNKNOWN SEQUENCE TYPE***"

def seqStop(seq):
    if hasListType(seq):
        return ']'
    elif hasTupleType(seq):
        return ')'
    elif hasSetType(seq):
        return '])'
    else: 
        "***UNKNOWN SEQUENCE TYPE***"

def compressSequence(seq, eltsStringss):
    if all([len(eltStrings) == 1 for eltStrings in eltsStringss]):
        return seqStart(seq) + ', '.join([eltStrings[0] for eltStrings in eltsStringss]) + seqStop(seq)
    else:
        return None

def compressDict(keyValStringsList):
    if all([len(valStrings) == 1 for (key, valStrings) in keyValStringsList]):
        result = ('{'
                  +  ', '.join([myValToString(key) + ': ' + valStrings[0]
                                for (key, valStrings) in keyValStringsList])
                  + '}')
        # print 'compressDict => {}, {}'.format(result, len(result))
        return result
    else:
        return None

def compressKeyValBinding(key, valStrings):
    if len(valStrings) == 1: 
        result = myValToString(key) + ': ' + valStrings[0]
    else: 
        result = (myValToString(key) + ': ' 
                + valStrings[0] # start symbol
                + ', '.join(valStrings[1:-1]) # elemenents
                + valStrings[-1] # stop symbol
                )
    # print 'compressKeyValBinding => {}, {}'.format(result, len(result))
    return result

if __name__ == "__main__":
    
    declaration = '''When in the Course of human events it becomes necessary for one people to dissolve the political bands which have connected them with another and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation.'''

    declaration2 = [
        "When in the Course of human events".split(),  
        "it becomes necessary for one people to dissolve the political bands".split(),
        "which have connected them with another".split(),
        " and to assume among the powers of the earth,".split(),
        "the separate and equal station to which the Laws of Nature".split(),
        "and of Nature's God entitle them,".split(),
        "a decent respect to the opinions of mankind".split(),
        "requires that they should declare the causes which impel them to the separation.".split()
        ]

    declaration3 = [
        ["When in the Course of human events".split(),  
         "it becomes necessary for one people to dissolve the political bands".split(),
         "which have connected them with another".split()],
        [" and to assume among the powers of the earth,".split(),
        "the separate and equal station to which the Laws of Nature".split(),
        "and of Nature's God entitle them,".split()], 
        ["a decent respect to the opinions of mankind".split(),
         "requires that they should declare the causes which impel them to the separation.".split()]
        ]

 
    stringList1 = ["foo", "bar", "baz"]
    stringList2 = ["John", "Paul", "George", "Ringo"]
    declaration1 = declaration.split()

    dictWithLists = {
        "cat" : ["foo", "bar", "baz"],
        "dog" : ["John", "Paul", "George", "Ringo"], 
        "bunny" :["father", "son", "holy ghost"]
    }

    dictWithTuples = {
        "cat" : ("foo", "bar", "baz"),
        "dog" : ("John", "Paul", "George", "Ringo"), 
        "bunny" : ("father", "son", "holy ghost")
    }

    dictWithSets = {
        "cat" : set(["foo", "bar", "baz"]), 
        "dog" : set(["John", "Paul", "George", "Ringo"]),
        "bunny" : set(["father", "son", "holy ghost"])
    }

    dictWithIntegerKeys = {
        17: ["foo", "bar", "baz"],
        251: ["John", "Paul", "George", "Ringo"], 
        7812372627: ["father", "son", "holy ghost"]
    }

    dictWithTupleKeysAndValues = {
        ("mister", "cat") : ("foo", "bar", "baz"),
        ("mrs", "dog") : ("John", "Paul", "George", "Ringo"), 
        ("little", "baby", "bunny") : ("father", "son", "holy ghost")
    }
 
    declarationsDict = {
        "declaration0": declaration,
        "declaration1": declaration1,
        "declaration2": declaration2, 
        "declaration3": declaration3
    }

    survivalDict = {'1st Class': {'survivalRate': 0.62, 'survivors': 201, 'victims': 123}, 
                   '2nd Class': {'survivalRate': 0.418, 'survivors': 119, 'victims': 166}, 
                   '3rd Class': {'survivalRate': 0.254, 'survivors': 180, 'victims': 528}, 
                   'A la Carte': {'survivalRate': 0.043, 'survivors': 3, 'victims': 66}, 
                   'Deck': {'survivalRate': 0.652, 'survivors': 43, 'victims': 23}, 
                   'Foo2': {'survivalRate': 0.123456789, 'survivors': 2345678901, 'victims': 3456789012}, 
                   'Foobarville': {'survivalRate': 0.123456789111, 'survivors': 2345678901222, 'victims': 3456789012333}, 
                   'Foobarville2': {'survivalRate': 0.12345678, 'survivors': 234567890, 'victims': 345678901}, 
                   'Engine': {'survivalRate': 0.222, 'survivors': 72, 'victims': 253}, 
                   'Victualling': {'survivalRate': 0.218, 'survivors': 94, 'victims': 337}}

    allDicts = {
        'dictWithLists': dictWithLists,
        'dictWithTuples': dictWithTuples, 
        'dictWithSets': dictWithSets, 
        'dictWithIntegerKeys': dictWithIntegerKeys, 
        'dictWithTupleKeysAndValues': dictWithTupleKeysAndValues, 
        'declarationsDict': declarationsDict, 
        'survivalDict': survivalDict
        }

    def testLists():
        for lst in [stringList1, 
                    [stringList1, tuple(stringList1), set(stringList1)],
                    stringList2, 
                    [stringList2, tuple(stringList2), set(stringList2)],
                    declaration1, 
                    declaration2, 
                    declaration3,
                    ]:
            print(stringify(lst))

    def testTuples():
        for lst in [stringList1, stringList2, [tuple(line) for line in declaration2]]:
            print(stringify(tuple(lst)))

    def testSets():
        for lst in [stringList1, stringList2, [tuple(line) for line in declaration2]]: 
            print(stringify(set(lst)))

    def testDicts():
        for dct in [
            # dictWithLists, 
            # dictWithTuples, 
            # dictWithSets, 
            # dictWithIntegerKeys, 
            # dictWithTupleKeysAndValues, 
            # declarationsDict,
            survivalDict
            # allDicts
            ]:
            # print(json.dumps(dct, sort_keys=True, indent=4, separators=(',', ': ')))
            print(stringify(dct))

    # testLists()
    # testTuples()
    # testSets()
    testDicts()

def hasIntegerType(x):
    return isinstance(x, int) or isinstance(x, long)

def hasSequenceType(x): 
    return hasListType(x) or hasTupleType(x) or hasSetType(x)

def hasListType(x):
    return isinstance(x, list) 

def hasTupleType(x):
    return isinstance(x, tuple) 

def hasSetType(x):
    return isinstance(x, set) 

def hasDictType(x):
    return isinstance(x, dict) 

def hasStringType(x): 
    return isinstance(x, str) or isinstance(x, unicode)

def myValToString(v):
    if hasStringType(v):
        return "'{}'".format(v)
    else:
        return str(v)
