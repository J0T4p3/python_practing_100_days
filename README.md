# Password Generator CLI Tool

This is a simple Python command-line interface (CLI) tool that generates random passwords based on user preferences. The tool allows you to specify the length of the password, the number of special characters, and the number of numbers to include in the generated password.

## Prerequisites

- Python 3.x

## Usage

1. Clone the repository or download the script file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using the following command:

   ```
   python password_generator.py
   ```

5. Follow the instructions prompted by the tool:

   - Select the length of the password (minimum 8 characters, press Enter for 8).
   - Select the number of special characters to include.
   - Select the number of numbers to include.

6. The generated password will be displayed in the terminal.

## How it Works

The tool generates passwords by randomly selecting characters from different character sets:

- Special characters: ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~
- Uppercase letters: A to Z
- Lowercase letters: a to z
- Numbers: 0 to 9

The tool calculates the number of vowels (both lowercase and uppercase) based on the selected length, the number of special characters, and the number of numbers. It then generates the password by randomly selecting characters from the character sets according to the specified counts. Finally, the password is shuffled to ensure randomness.

If invalid inputs are provided (e.g., selecting more characters than the password length), an error message will be displayed.

Feel free to customize the character sets or modify the code to suit your specific requirements.

Please note that while this tool can generate passwords, it is always recommended to use a trusted password manager or library for managing and generating secure passwords.
