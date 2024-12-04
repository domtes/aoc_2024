def count_word_occurences(rows: list[str], word: str) -> int:
    occurrences = 0
    reversed_word = "".join(reversed(word))
    wordlen = len(word)

    horizontal = []
    for line in rows:
        for j in range(0, len(line)-wordlen+1):
            horizontal.append(line[j:j+wordlen])

    horizontal_occurrences = [x for x in horizontal if x in (word, reversed_word)]
    
    occurrences += len(horizontal_occurrences)

    columns = list(zip(*rows))
    vertical = []

    for column in columns:
        for j in range(0, len(column)-wordlen+1):
            vertical.append("".join(column[j:j+wordlen]))


    vertical_occurrences = [x for x in vertical if x in (word, reversed_word)]
    occurrences += len(vertical_occurrences)

    diagonal_ltr = []
    for i in range(0, len(rows)-wordlen+1):
        for j in range(0, len(rows[0])-wordlen+1):
            diagonal_ltr.append("".join(rows[i+k][j+k] for k in range(0, wordlen)))

    diagonal_ltr_occurrences = [x for x in diagonal_ltr if x in (word, reversed_word)]

    occurrences += len(diagonal_ltr_occurrences)

    diagonal_rtl = []
    for i in range(0, len(rows)-wordlen+1):
        for j in range(wordlen-1, len(rows[0])):
            diagonal_rtl.append("".join(rows[i+k][j-k] for k in range(0, wordlen)))

    diagonal_rtl_occurrences = [x for x in diagonal_rtl if x in (word, reversed_word)]

    occurrences += len(diagonal_rtl_occurrences)

    return occurrences


def count_x_mas_shapes(rows: list[str]) -> int:
    occurrences = 0
    shape_length = 3

    for i in range(len(rows)-shape_length+1):
        for j in range(len(rows[0])-shape_length+1):
            if rows[i+1][j+1] != "A":
                continue
            word_1 = "".join([rows[i][j], rows[i+1][j+1], rows[i+2][j+2]])
            word_2 = "".join([rows[i][j+2], rows[i+1][j+1], rows[i+2][j]])

            if word_1 in ("MAS", "SAM") and word_2 in ("MAS", "SAM"):
                occurrences += 1

    return occurrences


def main():
    input_file = "day_4/input.txt"

    with open(input_file, "r") as f:
        data = [line.strip() for line in f.readlines()]

    print(f"xmas words = {count_word_occurences(data, 'XMAS')}")
    print(f"x-mas shapes = {count_x_mas_shapes(data)}")


if __name__ == "__main__":
    main()
