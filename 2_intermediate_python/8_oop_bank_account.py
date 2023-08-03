class BankAccount:
    def __init__(self, account_number: str, balance: float, account_type: str) -> None:
        """
        Initialize a BankAccount object with account details.

        Args:
            account_number (str): The account number.
            balance (float): The account balance.
            account_type (str): The type of the account.

        Returns:
            None
        """
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self) -> None:
        """
        Destructor for BankAccount class.

        Returns:
            None
        """
        print(
            f"BankAccount object with account number {self.account_number} is destroyed."
        )


class Customer:
    def __init__(self, name: str, age: int, address: str) -> None:
        """
        Initialize a Customer object with customer details.

        Args:
            name (str): The name of the customer.
            age (int): The age of the customer.
            address (str): The address of the customer.

        Returns:
            None
        """
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = None

    def create_bank_account(
        self, account_number: str, balance: float, account_type: str
    ) -> None:
        """
        Create a BankAccount object for the customer.

        Args:
            account_number (str): The account number.
            balance (float): The account balance.
            account_type (str): The type of the account.

        Returns:
            None
        """
        self.bank_account = BankAccount(account_number, balance, account_type)

    def __del__(self) -> None:
        """
        Destructor for Customer class.

        Returns:
            None
        """
        print(f"Customer object for {self.name} is destroyed.")


if __name__ == "__main__":
    # Create a Customer object
    customer1 = Customer("Ram Prasad", 30, "Dhulikhel")
    customer1.create_bank_account("123456789", 1000.0, "Savings")

    # Create another Customer object
    customer2 = Customer("Hari Kumar", 25, "Kathmandu")
    customer2.create_bank_account("987654321", 2000.0, "Checking")

    # Explicitly delete the objects to trigger the destructors
    del customer1
    del customer2

    # Output: BankAccount object with account number 123456789 is destroyed.
    #         Customer object for John Doe is destroyed.
    #         BankAccount object with account number 987654321 is destroyed.
    #         Customer object for Jane Smith is destroyed.
