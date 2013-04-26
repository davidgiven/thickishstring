# coding=UTF-8
#
# thickishstring server
# Copyright © 2013 David Given
#
# This software is redistributable under the terms of the Simplified BSD
# open source license. Please see the COPYING file in the distribution for
# the full text.

import ts.scriptcompiler as scriptcompiler
from ts.ScriptRuntime import ScriptRuntime
import dis
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def run_test(test):
	(script, desiredresult) = test
	print "-----"
	print script
	module = scriptcompiler.compile(script)
	rt = ScriptRuntime()
	result = module["var_test"](rt)
	if (result != desiredresult):
		print "TEST FAILED: ", result, " != ", desiredresult
		exit(1)
	else:
		print "PASSED"

scripts = [
	('''
		sub test
			return true
		endsub
	''',
	True),

	('''
		sub test
			return false
		endsub
	''',
	False),

	('''
		sub test
			return 1+1
		endsub
	''',
	2),

	('''
		sub test
			x = 1: y = 1
			return x+y
		endsub
	''',
	2),

	('''
		sub test
			return 1+2*3
		endsub
	''',
	7),

	('''
		sub test
			return 1*2+3
		endsub
	''',
	5),

	('''
		sub test
			return 1/2
		endsub
	''',
	0.5),

	('''
		sub test
			if true then
				return 1
			else
				return 0
			endif
		endsub
	''',
	1),

	('''
		sub test
			if false then
				return 1
			else
				return 0
			endif
		endsub
	''',
	0),

	('''
		sub test
			if false then
				return 1
			elseif false then
				return 2
			elseif false then
				return 3
			else
				return 0
			endif
		endsub
	''',
	0),

	('''
		sub test
			if true then
				return 1
			endif
			return 0
		endsub
	''',
	1),

	('''
		sub test
			if false then
				return 1
			endif
			return 0
		endsub
	''',
	0),

	('''
		sub test
			if true then return 1 else return 0
		endsub
	''',
	1),

	('''
		sub test
			if false then return 1 else return 0
		endsub
	''',
	0),

	('''
		sub test
			if true then return 1
			return 0
		endsub
	''',
	1),

	('''
		sub test
			if false then return 1
			return 0
		endsub
	''',
	0),

	('''
		sub test
			if false then if false then if false then return 1 else return 2
			return 0
		endsub
	''',
	0),

	('''
		sub test
			if true then if true then if true then return 1 else return 2
			return 0
		endsub
	''',
	1),

	('''
		sub test
			$x = 1: return $x
		endsub
	''',
	1),

	('''
		sub test
			$x = 1: y = 2
			$x = $x + y
			return $x
		endsub
	''',
	3),

	('''
		sub test
			y = 0
			for x = 1 to 10
				 y = y + x
			next
			return y
		endsub
	''',
	55),

	('''
		sub test
			y = 0
			for x = 10 to 1
				 y = y + x
			next
			return y
		endsub
	''',
	10),

	('''
		sub test
			y = 0
			for x = 1 to 10 step -1
				 y = y + x
			next
			return y
		endsub
	''',
	1),

	('''
		sub test
			y = 0
			for x = 10 to 1 step -1
				 y = y + x
			next
			return y
		endsub
	''',
	55),

	('''
		sub test
			y = 0
			for x = 1 to 10: y = y + x: next
			return y
		endsub
	''',
	55),

	('''
		sub test
			y = 0: x = 0
			while (x < 10)
				y = y + x
				x = x + 1
			endwhile
			return y
		endsub
	''',
	45),

	('''
		sub test
			y = 0: x = 0
			while (x < 10): y=y+x: x=x+1: endwhile
			return y
		endsub
	''',
	45),

	('''
		sub test
			x=1: y=2: return x < y
		endsub
	''',
	True),

	('''
		sub test
			x=1: y=2: return x <= y
		endsub
	''',
	True),

	('''
		sub test
			x=1: y=2: return x > y
		endsub
	''',
	False),

	('''
		sub test
			x=1: y=2: return x >= y
		endsub
	''',
	False),

	('''
		sub test
			x=1: y=2: return x == y
		endsub
	''',
	False),

	('''
		sub test
			x=1: y=2: return x = y
		endsub
	''',
	False),

	('''
		sub test
			x=1: y=2: return x != y
		endsub
	''',
	True),

	('''
		sub test
			x=1: y=2: return x <> y
		endsub
	''',
	True),

	('''
		sub test
			x=1: y=2: return x<y and y==2
		endsub
	''',
	True),

	('''
		sub test
			x=1: y=2: return x>y or y==2
		endsub
	''',
	True),

	('''
		sub test
			return true and true or false
		endsub
	''',
	True),

	('''
		sub test
			return true or true and false
		endsub
	''',
	True),

	('''
		sub zero
		endsub

		sub zerop()
		endsub

		sub one(p1)
			return p1
		endsub

		sub two(p1, p2)
			return p1+p2
		endsub

		sub test
			zero(): zerop()
			return one(1) + two(1, 2)
		endsub
	''',
	4),

#	('''
#		return 1 < false
#	''',
#	True),
]

for test in scripts:
	run_test(test)

