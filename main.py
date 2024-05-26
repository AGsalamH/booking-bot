'''
Bot entrypoint.
'''
from datetime import date
from booking import Booking


def main():
    '''Main entrypoint'''
    with Booking(teardown=True) as booking:
        booking.land_homepage()

        # close the window that appears when website first loads.
        booking.explicitly_close_modal()

        booking.set_currency('EGP')

        # Double check closing the modal, it may appears after choosing the currency.
        booking.explicitly_close_modal()

        # Enter destination
        booking.where_you_going('Dahab')

        # When you going ?
        booking.when_you_going(date.today(), date(2024, 5, 30))


if __name__ == '__main__':
    main()
