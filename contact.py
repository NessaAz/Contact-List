class Contact:
    """
    Class that generates new instances of contacts.
    """

    contact_list = [] # Empty contact list

    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email

contact_list = [] # Empty contact list
 #Init method up here
def save_contact(self):
  '''
  save_contact method saves contacts into contact_list
  '''
  Contact.contact_list.append(self)

def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)

@classmethod
def contact_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                    return True

        return False          

@classmethod
def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list        