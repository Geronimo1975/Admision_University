from simple_salesforce import Salesforce
from config_loader import SALESFORCE_USERNAME, SALESFORCE_PASSWORD, SALESFORCE_TOKEN

sf = Salesforce(username=SALESFORCE_USERNAME, password=SALESFORCE_PASSWORD, security_token=SALESFORCE_TOKEN)

def save_interview_result(user, answer, evaluation):
    sf.Contact.create({
        'LastName': user,
        'Description': f"Răspuns la interviu: {answer}\nEvaluare AI: {evaluation}"
    })
