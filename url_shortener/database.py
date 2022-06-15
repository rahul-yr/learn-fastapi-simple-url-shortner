import time


class MockDBOperations:
    '''
    Created a class to mimic the database operations.
    You can use this class to implement the actual database operations.
    '''

    # Initialize the database
    def __init__(self):
        # Here I used the dictionary to store the data.
        # You can use actual database connection to store the data.
        self.all_data = {}

    # Add the data to the database
    async def add_data_to_db(self, url : str , short_url : str) -> bool :
        # added a sleep to simulate the database operation
        time.sleep(0.2)
        try:
            # Check if the url already exists in the database
            if url in self.all_data:
                # If the url already exists, return False
                return False
            else:
                # If the url does not exist, add it to the database
                self.all_data[short_url] = url
                return True
        except:
            return False
    
    # Delete the data from the database
    async def delete_data_from_db(self, short_url : str) -> bool :
        # added a sleep to simulate the database operation
        time.sleep(0.2)
        try:
            # Check if the url already exists in the database
            if short_url in self.all_data:
                # If the url already exists, delete it from the database
                del self.all_data[short_url]
                return True
            else:
                # If the url does not exist, return False
                return False
        except:
            return False

    # Get the data from the database
    async def fetch_all_data(self) -> dict :
        # added a sleep to simulate the database operation
        time.sleep(0.2)
        # Return the data
        return self.all_data