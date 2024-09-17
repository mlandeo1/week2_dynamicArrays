class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class DynamicList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_string(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return ''.join(result)

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def is_palindrome(self):
        # Step 1: Extract only letter characters, ignoring case and non-letter characters
        letters = []
        current = self.head
        while current:
            if current.data.isalpha():
                letters.append(current.data.lower())
            current = current.next
        return letters == letters[::-1]

def create_list_from_string(input_string):
    dynamic_list = DynamicList()
    for char in input_string:
        dynamic_list.append(char)
    return dynamic_list

def process_string(input_string):
    # Create a dynamic list from the input string
    dynamic_list = create_list_from_string(input_string)
    
    # 1. Print the string in reverse order
    dynamic_list.reverse()
    reversed_string = dynamic_list.to_string()
    print(f"Reversed string: {reversed_string}")
    
    # 2. Check if the input string is a palindrome (ignoring case and non-letter characters)
    dynamic_list.reverse()  # Reverse back to the original order
    if dynamic_list.is_palindrome():
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    process_string(input_string)
