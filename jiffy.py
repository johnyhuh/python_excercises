# Define your function here
def jiffies_to_seconds(user_jiffies):
    try:
        user_jiffies = float(user_jiffies) / 100
        return (f'{user_jiffies:.3f}')
    except ValueError:
        return (f'{0:.3f}')

if __name__ == '__main__':
    input_value = input("Enter jiffy value: ")
    print(jiffies_to_seconds(input_value))
