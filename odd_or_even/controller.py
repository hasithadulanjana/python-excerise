class Controller:

    def __init__(self,view,model):
        self.view = view
        self.model = model
    def runner(self):
        number = self.view.get("Please enter number")
        checked_value = self.model.check_odd_or_even(int(number))
        self.view.say("Your Number is " + checked_value)
