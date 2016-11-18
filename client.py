import binary_search
import generator

choice = 0
div_line = '--------------------------'
div_line_after_empty_line = '\n--------------------------'


def make_a_choice():
    print '\nAvailable tools:'
    print div_line
    print '[1] - Binary Search'
    print '[2] - String Generator'
    print '[3] - String border search'
    print '[q] - Exit'
    print div_line
    return raw_input('Choose the tool: ')


def call_binary_search_client(str_generator):
    use_string_generator = True

    if str_generator == 0:
        use_string_generator = False

    user_input = 'y'
    first_search = True

    current_search = binary_search.Search()
    current_search.integer_or_decimal()
    current_search.input_max_and_min()

    while user_input != 'n':

        if current_search.min_num >= current_search.max_num:
            while current_search.min_num >= current_search.max_num:
                print "Min cannot be more than max, please enter new values"
                current_search.input_max_and_min()

        if not first_search:
            current_search.ask_where_to_search(user_input)
        else:
            first_search = False
        current_search.define_search_num()
        sg_size = current_search.get_search_num()
        print 'Current guess: ' + str(sg_size)
        if use_string_generator:
            print str_generator.string_generator(sg_size)
        user_input = raw_input("\nSearch again[u/l/n]?")


def call_string_generator_client():
    print div_line_after_empty_line
    print 'Welcome to String Generator'

    while True:
        sg_choice = get_string_generator_choice()
        if sg_choice == 'q':
            break
        sg_mode = get_string_generator_mode(sg_choice)

        sg_size = int(raw_input('Enter the size of the string: '))

        my_generator = generator.StringGenerator(sg_mode, sg_size)
        print 'YOUR STRING: ' + my_generator.string_generator()


def get_string_generator_choice():
    print div_line
    print '[1] - All symbols mode'
    print '[2] - All letters mode (latin)'
    print '[3] - Just digits mode'
    print '[4] - Just punctuation mode'
    print '[q] - Quit'
    print div_line
    sg_choice = raw_input('CHOICE: ')
    return sg_choice


def get_string_generator_mode(sg_choice):
    sg_mode = 0

    if sg_choice == '1':
        sg_mode = generator.StringGenerator.ALL_MODE
    elif sg_choice == '2':
        sg_mode = generator.StringGenerator.ALL_LETTERS_MODE
    elif sg_choice == '3':
        sg_mode = generator.StringGenerator.JUST_DIGITS_MODE
    elif sg_choice == '4':
        sg_mode = generator.StringGenerator.JUST_PUNCTUATION_MODE
    return sg_mode


def call_string_border_search():

    while True:
        sg_choice = get_string_generator_choice()
        if sg_choice == 'q':
            break
        sg_mode = get_string_generator_mode(sg_choice)
        str_generator = generator.StringGenerator(sg_mode, 0)

        while True:
            user_input = 'y'
            first_search = True

            current_search = binary_search.Search()
            current_search.integer_or_decimal()
            current_search.input_max_and_min()

            while user_input != 'n':

                if current_search.min_num >= current_search.max_num:
                    while current_search.min_num >= current_search.max_num:
                        print "Min cannot be more than max, please enter new values"
                        current_search.input_max_and_min()

                if not first_search:
                    current_search.ask_where_to_search(user_input)
                else:
                    first_search = False
                current_search.define_search_num()
                sg_size = current_search.get_search_num()
                print 'Current guess: ' + str(sg_size)
                print str_generator.string_generator(sg_size)
                user_input = raw_input("\nSearch again[u/l/n]?")
        break


while True:
    choice = make_a_choice()

    if choice == '1':
        call_binary_search_client(0)
    elif choice == '2':
        call_string_generator_client()
    elif choice == '3':
        call_string_border_search()
        pass
    elif choice == 'q':
        break
    else:
        print 'Wrong choice, try again'
