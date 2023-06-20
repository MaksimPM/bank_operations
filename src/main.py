from utills import get_data, get_filtered_data, get_last_values, get_formatted_data


def main():
    count_last_values = 5

    data = get_data()
    data = get_filtered_data(data)
    data = get_last_values(data, count_last_values)
    data = get_formatted_data(data)

    for row in data:
        print(row, end='\n\n')


if __name__ == "__main__":
    main()
