from datetime import datetime


def diff_time(function):
    """
    Decorator to measure elapsed time from a subscribed function.
    TODO: Implement with a logger integration.

    :param function:
    :return: Result from subscribed function.
    """

    def inner(*args, **kwargs):
        init = datetime.now()
        try:
            result = function(*args, **kwargs)

            return result
        except Exception as e:
            print(f"Error in '{function.__name__}': {e}")
        finally:
            final = datetime.now()
            print(f"ElapsedTime('{function.__name__}'): {final - init}")

    return inner
