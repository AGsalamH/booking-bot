'''
Bot entrypoint.
'''
from booking import Booking


def main():
    '''Main entrypoint'''
    with Booking(teardown=True) as booking:
        booking.land_homepage()


if __name__ == '__main__':
    main()
