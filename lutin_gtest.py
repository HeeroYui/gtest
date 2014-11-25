#!/usr/bin/python
import lutinModule as module
import lutinTools as tools

def get_desc():
	return "gtest : google test interface"

def get_license():
	return "BSD 3 clauses"


def create(target):
	myModule = module.Module(__file__, 'gtest', 'LIBRARY')
	
	myModule.add_src_file([
		'src/gtest-all.cc',
		'src/gtest.cc',
		'src/gtest-death-test.cc',
		'src/gtest-filepath.cc',
		'src/gtest_main.cc',
		'src/gtest-port.cc',
		'src/gtest-printers.cc',
		'src/gtest-test-part.cc',
		'src/gtest-typed-test.cc'
		])
	
	myModule.compile_flags_CC([
		'-DPNG_NO_LIMITS_H'])
	
	myModule.add_path(tools.get_current_path(__file__))
	myModule.add_export_path(tools.get_current_path(__file__)+"/include/")
	
	# add the currrent module at the 
	return myModule









