import random


def get_average_distance(serial_nums):
    """
    Given a list of sorted integers will return a list containing distance between each index.
    Distance is the amount of elements between the index so [2,5] would be [2] since between
    2 and 5 there is 3 and 4

    :param serial_nums: A list of sorted integers representing serial numbers
    :return: Average distance between indexes
    """
    average_distances = []
    for x in range(0, len(serial_nums) - 1):
        average_distances.append(serial_nums[x + 1] - serial_nums[x] - 1)

    return sum(average_distances)/len(average_distances)


def maximum_likelihood_estimation(serial_nums):
    """
    Given a sorted list of serial numbers will use maximum likelihood estimation and return the total

    :param serial_nums: Sorted list of integers representing unique serial numbers
    :return: Return float with estimation of total amount of serial numbers
    """
    highest = serial_nums[-1]
    average_distance = get_average_distance(serial_nums)
    return highest + average_distance


def generate_serial_numbers(total_tanks, num_serials, seed):
    """
    Given a total number of tanks and amount of serial numbers found will return an array containing the
    amount of unique serial numbers asked for.

    :param total_tanks: An integer representing the total amount of tanks that have been created
    :param num_serials: An integer representing how many tank serial numbers are found
    :param seed: An integer, string or None that will be used to set seed for random number generation
    :return: A sorted list of integers each index representing a serial number
    """
    serial_nums = set()
    # Set seed for random number generation
    random.seed(seed)

    unique_serial_numbers = 0

    # Generate amount of serial numbers requested
    while unique_serial_numbers < num_serials:
        poss_serial = random.randint(1, total_tanks)
        if poss_serial not in serial_nums:
            serial_nums.add(poss_serial)
            unique_serial_numbers += 1

    print(sorted(serial_nums))
    return sorted(serial_nums)


def main():
    # Get settings from user
    total_tanks = input("How many tanks would you like to simulate with? ")
    num_serials = input("How many tank serial numbers do you want use? ")
    seed = input("Would like to use a set seed? Type None for a random seed ")
    # Check if we should have random seed
    if seed.lower() == "none":
        seed = None
    # Get serial number of tanks found
    serial_nums = generate_serial_numbers(int(total_tanks), int(num_serials), seed)
    # Apply formula
    estimated_total = maximum_likelihood_estimation(serial_nums)
    # Spit out result
    print(estimated_total)


if __name__ == "__main__":
    main()
