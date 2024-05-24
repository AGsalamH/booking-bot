'''
Bot entrypoint.
'''
from booking import Booking


def main():
    '''Main entrypoint'''
    with Booking(teardown=True) as booking:
        booking.land_homepage()

        # close the window that appears when website first loads.
        booking.close_modal()

        booking.set_currency('EGP')

        # Double check closing the modal, it may appears after choosing the currency.
        booking.close_modal()


if __name__ == '__main__':
    main()
