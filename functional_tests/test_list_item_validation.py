from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

	# @skip
	def test_can_not_add_empty_list_items(self):

		# Edith tries to submit an empty list item
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('\n')

		# she gets an error message
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		#tries again with txt
		self.get_item_input_box().send_keys('Buy milk\n')
		self.check_for_row_in_list_table('1: Buy milk')

		# another blank item
		self.get_item_input_box().send_keys('\n')		

		# warning again
		self.check_for_row_in_list_table('1: Buy milk')
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		# with tex again, slow learner
		self.get_item_input_box().send_keys('Make tea\n')
		self.check_for_row_in_list_table('1: Buy milk')
		self.check_for_row_in_list_table('2: Make tea')

		# self.fail('write me!')

# if __name__ == '__main__':
# 	unittest.main(warnings='ignore')
















