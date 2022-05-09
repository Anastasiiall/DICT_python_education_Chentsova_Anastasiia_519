print("""Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line"
Special commands: !help !done""")


def choose():
    com = input("Choose a formatter: ")
    if com == 'plain':
        text = input('Text: ')
        print(text)
        with open('output.md', 'a') as i:
            i.write(text)
        choose()
    elif com == 'bold':
        text = input('Text: ')
        print('**'+text+'**')
        with open('output.md', 'a') as i:
            i.write('**'+text+'**')
        choose()
    elif com == 'italic':
        text = input('Text: ')
        print('*'+text+'*')
        with open('output.md', 'a') as i:
            i.write('*'+text+'*')
        choose()
    elif com == 'header':
        level = int(input('Level: '))
        text = input('Text: ')
        if level == 1:
            print('#'+text)
            with open('output.md', 'a') as i:
                i.write('#'+text)
            choose()
        elif level == 2:
            print('##'+text)
            with open('output.md', 'a') as i:
                i.write('##'+text)
            choose()
        elif level == 3:
            print('###'+text)
            with open('output.md', 'a') as i:
                i.write('###'+text)
            choose()
        elif level == 4:
            print('####'+text)
            with open('output.md', 'a') as i:
                i.write('####'+text)
            choose()
        elif level == 5:
            print('#####'+text)
            with open('output.md', 'a') as i:
                i.write('#####'+text)
            choose()
        elif level == 6:
            print('######'+text)
            with open('output.md', 'a') as i:
                i.write('######'+text)
            choose()
        else:
            print('The level should be within the range of 1 to 6.')
            choose()
    elif com == 'link':
        url = input('URL: ')
        print(url)
        with open('output.md', 'a') as i:
            i.write(url)
        choose()
    elif com == 'inline-code':
        text = input('Text: ')
        print("'"+text+"'")
        with open('output.md', 'a') as i:
            i.write("'"+text+"'")
        choose()
    elif com == 'ordered-list':
        n = int(input('Number of rows: '))
        for x in range(n):
            k = x+1
            row = input('Row #'+str(k)+': ')
            print(str(k)+'. '+row)
            with open('output.md', 'a') as i:
                i.write(str(k)+'. '+row)
        choose()
    elif com == 'unordered-list':
        n = int(input('Number of rows: '))
        for x in range(n):
            k = x+1
            row = input('Row #'+str(k)+': ')
            print('* '+row)
            with open('output.md', 'a') as i:
                i.write('* '+row)
        choose()
    elif com == 'new-line':
        print()
        with open('output.md', 'a') as i:
            i.write('')
        choose()
    elif com == '!help':
        print('''Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line"
Special commands: !help !done''')
        choose()
    elif com == '!done':
        exit()
    else:
        print('Unknown formatting type or command')
        choose()


choose()
