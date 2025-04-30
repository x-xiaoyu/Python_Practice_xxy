// Problem: 179.Largest Number
// Medium 2pts
// 04/24/2024
// Topics: Array, String, Greedy, Sorting
// Description: Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
// Since the result may be very large, so you need to return a string instead of an integer.

// Links:https://leetcode.com/problems/largest-number/description/

int compare(const void* a, const void* b) {
    // Create buffer sufficiently large to hold two concatenated numbers
    char order1[24] = {0}, order2[24] = {0};
    // Concatenate strings in both possible orders
    strcat(strcat(strcpy(order1, *(const char**)a), *(const char**)b), "\0");
    strcat(strcat(strcpy(order2, *(const char**)b), *(const char**)a), "\0");
    // Return the order that produces the larger number
    return strcmp(order2, order1);
}

char* largestNumber(int* nums, int numsSize) {
    if (numsSize == 0) return strdup(""); // Handle empty input

    // Convert integers to strings
    char** asStrings = (char**) malloc(numsSize * sizeof(char*));
    if (!asStrings) return NULL; // Check for malloc failure

    for (int i = 0; i < numsSize; i++) {
        asStrings[i] = (char*) malloc(12 * sizeof(char)); // Each int can be up to 10 digits plus sign and null terminator
        if (!asStrings[i]) { // Check for malloc failure
            for (int j = 0; j < i; j++) free(asStrings[j]); // Free any previously allocated memory
            free(asStrings);
            return NULL;
        }
        sprintf(asStrings[i], "%d", nums[i]);
    }

    // Sort strings using custom comparator
    qsort(asStrings, numsSize, sizeof(char*), compare);

    // Special case: check if the largest number is "0"
    if (strcmp(asStrings[0], "0") == 0) {
        free(asStrings[0]); // Clean up
        free(asStrings);
        return strdup("0");
    }

    // Calculate total length of the result string
    int totalLength = 1; // Start with 1 for the null terminator
    for (int i = 0; i < numsSize; i++) {
        totalLength += strlen(asStrings[i]);
    }

    // Concatenate sorted strings into the final result
    char* result = malloc(totalLength);
    if (!result) { // Check for malloc failure
        for (int i = 0; i < numsSize; i++) free(asStrings[i]);
        free(asStrings);
        return NULL;
    }
    result[0] = '\0'; // Initialize the result string

    for (int i = 0; i < numsSize; i++) {
        strcat(result, asStrings[i]); // Append current string
        free(asStrings[i]); // Free memory as we go
    }
    free(asStrings);

    return result;
}
