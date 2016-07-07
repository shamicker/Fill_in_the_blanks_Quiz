"""
Fill in the Blanks Quiz -- or Reverse Mad Libs

Requirements:
- 3 levels
- each level has at least 4 questions
- user input - choose level, choose # of guesses, answer questions

Details:
- no functions are longer than 18 lines of code(excludes blank lines or
    function definition)
- Each fn includes a comment explaining behaviour, inputs, and outputs
    (when applicable)
- submit python file named "fill-in-the-blanks.py"
"""

html_text = """
HTML is the primary language of the web, and stands for Hyper Text (or
Hypertext) {0} Language. Like any language, it is made up of smaller
components and syntax.

A tag has < and > around it, and is a basic building block of HTML. An {1}
is usually made up of a beginning tag and an end tag, although sometimes there
is no closing tag. In this case, it's called a {2} tag.

An {3} is a specified characteristic of a tag, and a {4} is the
description of the {3}.

Structured HTML is crucial in order to create an efficient webpage.  It is the
outline of your document. There are 2 types of {1}s: {5} and block.

True or false: Both {5} and block {1} affect layout and style of a webpage?
{6}
"""

css_text = """
CSS is a style sheet document to accompany (and to style) HTML documents, and
the 'C' stands for {0}.

Everything within curly brackets is a {1}, which is made up of at least
one property with a value. A {2}, such as a tag, class, pseudo-class
or ID, is used to indicate what the {1} has power over.

Adding a {3} to clarify something is a good idea, and is denoted by
/*text*/, just as in HTML it's denoted by <!--text-->.

True or false: 'Blanket statements' are the least powerful in the hierarchy.
{4}
"""

python_text = """
Python is a high-level language that allows humans to communicate to computers,
and is a fairly mathematical language.

A {0} is a name assigned to a number or string that is more memorable than
the number or string itself might be. For instance, 'speed_of_light' could be
assigned to the seemingly random number 299792458. Sometimes, numbers without
a {0} is called a {1} number, and it's best to avoid these if at all
possible as it reduces the margin of error.

An {2} is something that has a value, although is not necessarily
numerical; it could also be alphabetical, a string, a formula or statement.

The '=' sign signifies an {3}.

The very first position of a string or list is always '0'. The 'Python' word
for 'position' is {4}.

True or false: An empty string causes an error when searched for? {5}
"""

html_answers = ["markup", "element", "void", "attribute",
                "value", "inline", "false"]

css_answers = ['cascading', 'declaration', 'selector', 'comment', 'true']

python_answers = ["variable", "magic", "expression", "assignment",
                  "index", "false"]


def choose_level():
    """
    Procedure with no inputs. Output is the player's choice of quiz.
    Include a loop for the player to change their mind regarding quiz-choice.
    """
    level_choices = ["html", "css", "python"]
    while True:
        player_prompt = ("""\n  Please type in (and then press enter) your choice of quiz topic:
        html
        css
        python
        -> """)
        user_choice = raw_input(player_prompt).lower()
        if user_choice not in level_choices:
            print " Sorry, I didn't catch that."
        else:
            level = user_choice
            player_prompt = " You chose the {} quiz! Are you sure? (Y/N) ".format(level)
            user_choice = raw_input(player_prompt).lower()
            if user_choice == "y" or user_choice == "yes":
                print "\n Welcome to the {} questions!".format(level)
                return level


def text_to_display(level):
    """
    Procedure with input of player's choice of level.
    Output is the appropriate answer_key and text.
    """
    if level == "html":
        return html_answers, html_text
    elif level == "css":
        return css_answers, css_text
    elif level == "python":
        return python_answers, python_text


def how_many(number):
    """
    Automate pluralization of "guess" for countdowns instead
    of downloading a package.
    """
    if int(number) == 1:
        return "guess"
    return "guesses"


def guesses():
    """
    Procedure with no input, but has a default of 3 attempts per question.
    Output is either 3, or player's choice of guesses per question (aka max_guesses).
    """
    tries = 3
    print (" You may choose your maximum number of tries per question."
           "The default is 3.")
    player_prompt = " Please type in your preferred number: "
    while tries > 0:
        user_choice = raw_input(player_prompt)
        if user_choice.isdigit():
            print "\n OK, {} {} allowed per blank. Here we go!\n".format(user_choice, how_many(user_choice))
            return int(user_choice)
        tries -= 1
        player_prompt = ("  Silly, that's not a valid number of guesses! {} more {}. \n"
                         " Try again: ").format(tries, how_many(tries))
    if tries == 0:
        print " You defaulted your number of guesses, so 3 it is!"
        return 3


def play_again(max_guesses):
    """
    Procedure with input of max_guesses. Ask player to play again, and to keep the max_guesses.
    The output is either a re-launch or termination of the game.
    """
    user_choice = raw_input(" Would you like to play again? (Y/N)").lower()
    if user_choice == "y" or user_choice == "yes":
        user_choice = raw_input(" Would you like the same number of guesses per question? (Y/N)").lower()
        if user_choice == "n" or user_choice == "no":
            max_guesses = None
        launch_quiz(max_guesses)
    else:
        print "\n Thank you for playing Shauna's Fill-in-the-Blanks Quiz!"
        print " Goodbye!"
        return None


def current_question(level, revealed_answers, index, max_guesses):
    """
    Procedure with 4 inputs: game level, revealed-answers, index, and max-guesses.
    Ask player for a response to current question, verify it against the answer_key.
    If true, return True (after substituting response into revealed_answers).
    If false, loop until true, or until player's guesses are used up and end game/ call the play_again function.
    """
    attempts_left = max_guesses
    while attempts_left > 0:
        answer_key, text = text_to_display(level)
        print text.format(*revealed_answers)
        player_prompt = "\n Please type your answer for question {}.\n  {} is: ".format(index+1, revealed_answers[index])
        response = raw_input(player_prompt).lower()
        if response == answer_key[index]:
            print "\n You are correct!!"
            revealed_answers[index] = "__"+answer_key[index]+"__"
            return True
        elif response != answer_key[index]:
            attempts_left -= 1
            if attempts_left == 0:
                print "\n Sorry, you have used up all your guesses.\n END GAME"
                play_again(max_guesses)
                return
            print ("\n Nope!\n    You have {} remaining {}."
                   "Have another crack at it.").format(attempts_left, how_many(attempts_left))


def launch_quiz(max_guesses=None):
    """
    Procedure with optional max_guesses parameter.
    Get level, re/set revealed_answers, get answer_key and text. If max_guesses is None, print text (with
    revealed_answers) and get max_guesses. Then start quiz.
    If all answers are correct, congrats and call the play_again function.
    """
    print "\n Yahoo!\n  You're playing Shauna's Fill-in-the-Blanks Quiz!"
    level = choose_level()
    revealed_answers = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__"]
    answer_key, text = text_to_display(level)
    if max_guesses is None:
        print text.format(*revealed_answers)
        max_guesses = guesses()
    for index in range(len(answer_key)):
        if not current_question(level, revealed_answers, index, max_guesses):
            return
    print " Congratulations!!!  You won the {} quiz!\n".format(level)
    play_again(max_guesses)


launch_quiz()
