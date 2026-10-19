def classify(width):
    if width < 98:
        return "Below range"
    elif 98 <= width <= 102:
        return "In range" 
    else:
        return "Above range"

def calculate_average(total, count):
    if count == 0:
        return 0
    return total / count
    
def main():
        num_tiles = int(input("Enter the number of tiles:" ))

        total_width = 0
        below_count = 0
        in_count = 0
        above_count = 0

        for i in range(num_tiles):
            width = int(input("Enter the tile width: "))

            classification = classify(width)
            print(classification)

            total_width += width

            if classification == "Below range":
                below_count += 1
            elif classification == "In range":
                in_count += 1
            elif classification == "Above range":
                above_count += 1

        average_width = calculate_average(total_width, num_tiles)
        print(f"Total width: {total_width}")
        print(f"Average width: {average_width}")
        print(f"Below range: {below_count}")
        print(f"In range: {in_count}")
        print(f"Above range: {above_count}")

main()
