from django.dispatch import Signal, receiver

# creating signals
notification = Signal(providing_args = ["request","user"])


# receiver function
def show_notification(sender, **kwargs):
    print(sender)
    print(f'{kwargs}')
    print('Notification')