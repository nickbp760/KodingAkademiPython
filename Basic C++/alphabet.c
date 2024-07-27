#include <stdio.h>

int main() {
    char ch;

    // Prompt the user for input
    printf("Enter an alphabet: ");
    scanf("%c", &ch);

    // Check if the input is a letter
    if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
        // Check if the letter is a vowel
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
            ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
            printf("%c is a vowel.\n", ch);
        } else {
            printf("%c is a consonant.\n", ch);
        }

        // Check if the letter is uppercase or lowercase
        if (ch >= 'A' && ch <= 'Z') {
            printf("%c is an uppercase letter.\n", ch);
        } else {
            printf("%c is a lowercase letter.\n", ch);
        }
    } else {
        printf("Invalid input. Please enter an alphabet.\n");
    }

    return 0;
}
