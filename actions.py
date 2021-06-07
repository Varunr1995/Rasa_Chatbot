from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction, FormAction

class Action_Painting_Form(FormValidationAction):
    def name(self) -> Text:
        return "validate_painting_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ List of required slots that the form has to fill (inputs from the user) """
        print("required_slots(tracker: Tracker")
        return["name", "entity_2", "entity_3", "entity_4", "entity_5", "entity_6"] # The list how we provide here will reflect in the sequence of questions from the bot as form.


    def submit(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict]:

        dispatcher.utter_message(template="utter_submit")

        return[]