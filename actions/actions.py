# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List, Union

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction

# class VaccineSuggestion(FormAction):

# 	def name(self):
# 		return "vaccine_suggestion_form"

# 	async def required_slots(
# 		self,
#         slots_mapped_in_domain: List[Text],
#         dispatcher: "CollectingDispatcher",
#         tracker: "Tracker",
#         domain: "DomainDict",
#     ) -> Optional[List[Text]]:
#         return slots_mapped_in_domain

# 	@staticmethod
# 	def required_slots(tracker):

# 		if tracker.get_slots("female_between_18_49") == True:
# 			dispatcher.utter_message(text="CDC do not recommend one vaccine over the other. But CDD advices precausion to female between 18 and 49 before getting Janssen vaccine due to posible blood clots. Pfizer and Moderna vaccine are available alternatives.")
# 			return ["female_between_18_49"]
# 	 	else:
# 	 		if tracker.get_slots("under_12") == True:
# 	 			dispatcher.utter_message(text="CDC do not recommend one vaccine over the other. Currently, the available vaccines did not include clinical trials on people under the age of 12. Please contact your primary healthcare provider for more consults."
# 	 		return []
# 	 		if tracker.get_slots("between_12_and_18") == True:
# 	 			dispatcher.utter_message(text="CDC do not recommend one vaccine over the other. Currently, Pfizer vaccine is the only available vaccine had people over 12 years old in its clinical trial with 95 percent effective."
# 			return ["between_12_and_18"]
# 			else:
# 				if tracker.get_slots("two_dose_commitment") == False:
# 	 			dispatcher.utter_message(text="CDC do not recommend one vaccine over the other. For 1 dose only, Janssen has the highest effective rate among 3 major vaccines with 66 percent."
# 	 			return
# 	 				else:
# 		 					dispatcher.utter_message(text="CDC do not recommend one vaccine over the other. You can get any availabe vaccines: Pfizer, Moderna, and Janssen."		 	
# 		 					return

# 	def submit(
# 		self,
# 		dispatcher: CollectingDispatcher,
# 		tracker: Tracker,
# 		domain: Dict[Text, Any]
# 	) -> List[Dict]:
# 		return []

# 	def slot_mapping(self) -> Dict[Text, Union[Dict, List[Dict]]]:
# 		return {
# 			"female_between_18_49": [
# 				self.from_intent(intent="affirm", value=True),
# 				self.from_intent(intent="deny", value=False),
# 			],
# 			"under_12": [
# 				self.from_intent(intent="affirm", value=True),
# 				self.from_intent(intent="deny", value=False),
# 			],
# 			"between_12_and_18": [
# 				self.from_intent(intent="affirm", value=True),
# 				self.from_intent(intent="deny", value=False),
# 			],
# 			"two_dose_commitment": [
# 				self.from_intent(intent="affirm", value=True),
# 				self.from_intent(intent="deny", value=False),
# 			]
# 		}

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
