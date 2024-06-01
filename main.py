'''
Bot entrypoint.
'''
from datetime import date, timedelta
from booking import Booking


def main():
    '''Main entrypoint'''
    with Booking(teardown=True) as bot:
        bot.land_homepage()

        # close the window that appears when website first loads.
        bot.explicitly_close_modal()

        bot.set_currency('EGP')

        # Double check closing the modal, it may appears after choosing the currency.
        bot.explicitly_close_modal()

        # Enter destination
        bot.where_you_going('Dahab')

        # When you going ?
        bot.when_you_going(date.today(), date.today() + timedelta(days=3))


if __name__ == '__main__':
    main()
