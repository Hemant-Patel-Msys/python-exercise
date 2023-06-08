from contextlib import contextmanager


@contextmanager
def example_cm(string_input):
    print('Setup logic\n')

    swapped = string_input.swapcase()
    try:
        yield swapped
    except ValueError as e:
        print('An error occurred...')
    finally:
        print('\nTeardown logic\n')

    print('End of context manager\n')


with example_cm('the MAJESTIC squirrel') as swapped_string:
    # Managed code
    print(swapped_string)