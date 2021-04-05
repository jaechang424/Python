# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in [1, 2, 3, 4]: print(i, '')

languages = ['python', 'perl', 'c', 'java']

print(languages[0][0:])

for lang in languages:
    if lang in ['python', 'perl']:
        # print("%6s need interpreter" % lang)
        print(f"{lang:>6} need interpreter")
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
