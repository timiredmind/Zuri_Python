class Budget:
    def __int__(self):
        self.food = 0.00
        self.clothing = 0.00
        self.entertainment = 0.00
        self.transport = 0.00

    def deposit(self, category, amount_to_be_deposited):
        possible_categories = (
            "food",
            "clothing",
            "entertainment",
            "transport")
        if (category in possible_categories) and (amount_to_be_deposited > 0):
            if category.lower() == "food":
                self.food += amount_to_be_deposited
            elif category.lower() == "clothing":
                self.clothing += amount_to_be_deposited
            elif category.lower() == "entertainment":
                self.entertainment += amount_to_be_deposited
            else:
                self.transport += amount_to_be_deposited

        elif category not in possible_categories:
            raise ValueError(
                f"{category} is not part of the possible categories")
        else:
            raise ValueError(
                "The amount to be deposited should not be less than zero")

    def withdrawal(self, category, amount_to_be_withdrawn):
        possible_categories = (
            "food",
            "clothing",
            "entertainment",
            "transport")
        if category in possible_categories:
            if amount_to_be_withdrawn < 0:
                raise ValueError(
                    "The amount to be withdrawn cannot be less than 0")
            else:
                if category.lower() == "food":
                    if self.food == 0:
                        raise ValueError("Insufficient balance")
                    else:
                        # In the case where the amount to be withdrawn is more
                        # than the available balance, the program withdraws and
                        # returns the available balance
                        money = min(amount_to_be_withdrawn, self.food)
                        self.food -= money

                elif category.lower() == "clothing":
                    if self.clothing == 0:
                        raise ValueError("Insufficient balance")
                    else:
                        # In the case where the amount to be withdrawn is more
                        # than the available balance, the program withdraws and
                        # returns the available balance
                        money = min(amount_to_be_withdrawn, self.clothing)
                        self.clothing -= money

                elif category.lower() == "entertainment":
                    if self.entertainment == 0:
                        raise ValueError("Insufficient balance")
                    else:
                        money = min(amount_to_be_withdrawn, self.entertainment)
                        self.entertainment -= money

                else:
                    if self.transport == 0:
                        raise ValueError("Insufficient balance")
                    else:
                        money = min(amount_to_be_withdrawn, self.transport)
                        self.transport -= money

        else:
            raise ValueError("Invalid category entered")

    def request_balance(self, category):
        if category == "food":
            return "Your food balance is %.2f" % self.food
        elif category == "clothing":
            return f"Your clothing balance is %.2f" % self.clothing
        elif category == "entertainment":
            return f"Your entertainment balance is %.2f" % self.entertainment
        elif category == "transport":
            return f"Your transportation balance is %.2f" % self.transport
        else:
            raise ValueError("Invalid category entered")

    def transfer_from_food_balance(
            self,
            amount_to_withdraw,
            category_to_transfer_to):
        if amount_to_withdraw > 0:
            amount = min(self.food, amount_to_withdraw)
            self.food -= amount
        else:
            raise ValueError(
                "The amount to be transferred should be more than 0")

        if category_to_transfer_to == "clothing":
            self.clothing += amount
            return "You have successfully transferred %.2f to your clothing balance" % amount

        elif category_to_transfer_to == "entertainment":
            self.entertainment += amount
            return"You have successfully transferred %.2f to your entertainment balance" % amount

        elif category_to_transfer_to == "transport":
            self.transport += amount
            return "You have successfully transferred %.2f to your transport balance" % amount

        else:
            raise ValueError("Invalid category entered")

    def transfer_from_clothing_balance(
            self,
            amount_to_withdraw,
            category_to_transfer_to):
        if amount_to_withdraw > 0:
            amount = min(self.clothing, amount_to_withdraw)
            self.clothing -= amount
        else:
            raise ValueError(
                "The amount to be transferred should be more than 0")

        if category_to_transfer_to == "food":
            self.clothing += amount
            return "You have successfully transferred %.2f to your food balance" % amount

        elif category_to_transfer_to == "entertainment":
            self.entertainment += amount
            return "You have successfully transferred %.2f to your entertainment balance" % amount

        elif category_to_transfer_to == "transport":
            self.transport += amount
            return "You have successfully transferred %.2f to your transport balance" % amount

        else:
            raise ValueError("Invalid category entered")

    def transfer_from_entertainment_balance(
            self, amount_to_withdraw, category_to_transfer_to):
        if amount_to_withdraw > 0:
            amount = min(self.entertainment, amount_to_withdraw)
        else:
            raise ValueError(
                "The amount to be transferred should be more than 0")

        if category_to_transfer_to == "food":
            self.food += amount
            return "You have successfully transferred %.2f to your food balance" % amount

        elif category_to_transfer_to == "clothing":
            self.clothing += amount
            return "You have successfully transferred %.2f to your clothing balance" % amount

        elif category_to_transfer_to == "transport":
            self.transport += amount
            return "You have successfully transferred %.2f to your transport balance" % amount
        else:
            raise ValueError("Invalid category entered")

    def transfer_from_transport_balance(
            self,
            amount_to_withdraw,
            category_to_transfer_to):
        if amount_to_withdraw > 0:
            amount = min(self.transport, amount_to_withdraw)
        else:
            raise ValueError(
                "The amount to be transferred should be more than 0")

        if category_to_transfer_to == "food":
            self.food += amount
            return "You have successfully transferred %.2f to your food balance" % amount

        elif category_to_transfer_to == "entertainment":
            self.clothing += amount
            return "You have successfully transferred %.2f to your clothing balance" % amount

        elif category_to_transfer_to == "transport":
            self.transport += amount
            return "You have successfully transferred %.2f to your transport balance" % amount

        else:
            raise ValueError("Invalid category entered")
