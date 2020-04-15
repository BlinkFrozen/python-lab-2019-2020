import string


def code_cesar(file_name, codec):
    coded_text = []
    with open(file_name) as file:
        data = file.readlines()
        for line in data:
            coded_text.append([string.ascii_lowercase[
                                   (string.ascii_lowercase.index(char.lower()) + codec) % len(
                                       string.ascii_lowercase)] if char in string.ascii_letters else char for char
                               in line])
    coded_text_string = [''.join(line) for line in coded_text]
    with open("coded_text", "w+") as file:
        file.writelines(coded_text_string)
    print(coded_text_string)
    return coded_text_string


def decode_cesar(file_name, codec):
    decoded_cesar = []
    with open(file_name) as file:
        data = file.readlines()
        for line in data:
            decoded_cesar.append([string.ascii_lowercase[
                                      (string.ascii_lowercase.index(char.lower()) - codec) % len(
                                          string.ascii_lowercase)] if char in string.ascii_letters else char for
                                  char
                                  in line])
    decoded_text_string = [''.join(line) for line in decoded_cesar]
    with open("decoded_text", "w+") as file:
        file.writelines(decoded_text_string)
    print(decoded_text_string)
    return decoded_text_string


def zad5(frequency_file, coded_file):
    frequencies = []
    with open(frequency_file) as file:
        data = file.read().splitlines()
        frequencies = [line.split('\t') for line in data]
        print(frequencies)
    frequencies_in_coded = {}
    with open(coded_file) as file:
        data = file.read().splitlines()
        all_letters = sum(len(line) for line in data)
        for letter in string.ascii_lowercase:
            frequencies_in_coded[letter] = sum([line.count(letter) for line in data]) * 100 / all_letters
        print(frequencies_in_coded)
        for letter, frequency in frequencies_in_coded.items():
            new_string = []
            for line in data:
                new_string.append(
                    line.replace(letter, min(frequencies, key=lambda x: abs(float(x[1]) - frequency))[0]))
            data = new_string
            new_string = []
        print(data)
        with open('writen_to_file.txt', 'w+') as file:
            file.writelines(data)
