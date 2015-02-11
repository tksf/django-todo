from unittest import skip
from .base import FunctionalTest



class ItemValidationTest(FunctionalTest):

	def get_error_element(self):
		return self.browser.find_element_by_css_selector('.has-error')

	# @skip
	def test_can_not_add_empty_list_items(self):

		# Edith tries to submit an empty list item
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('\n')

		# she gets an error message
		error = self.get_error_element()
		self.assertEqual(error.text, "You can't have an empty list item")

		#tries again with txt
		self.get_item_input_box().send_keys('Buy milk\n')
		self.check_for_row_in_list_table('1: Buy milk')

		# another blank item
		self.get_item_input_box().send_keys('\n')		

		# warning again
		self.check_for_row_in_list_table('1: Buy milk')
		error = self.get_error_element()
		self.assertEqual(error.text, "You can't have an empty list item")

		# with tex again, slow learner
		self.get_item_input_box().send_keys('Make tea\n')
		self.check_for_row_in_list_table('1: Buy milk')
		self.check_for_row_in_list_table('2: Make tea')

	def test_cannot_add_duplicate_items(self):

		# Edith starts a new lsit
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('Buy wellies\n')
		self.check_for_row_in_list_table('1: Buy wellies')

		# tries to enter duplicate item
		self.get_item_input_box().send_keys('Buy wellies\n')

		# gets an error message
		self.check_for_row_in_list_table('1: Buy wellies')
		error = self.get_error_element()
		self.assertEqual(error.text, "You've already got this in your list")

	def test_error_messages_are_cleared_on_input(self):
		# Edith starts a new list - causes validation error
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('\n')	
		error = self.get_error_element()
		self.assertTrue(error.is_displayed())

		# she starts typing to clear the error
		self.get_item_input_box().send_keys('a')
		error = self.get_error_element()
		self.assertFalse(error.is_displayed())	









