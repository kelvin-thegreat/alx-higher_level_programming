#include "lists.h"
/**
 * Definition for singly-linked list.
 * struct listint_s {
 *     int n;
 *     struct listint_s *next;
 * };
 */

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the first node of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int values[10000], i = 0, j = 0;

    while (current != NULL)
    {
        values[i++] = current->n;
        current = current->next;
    }

    j = i - 1;
    for (i = 0; i < j; i++, j--)
    {
        if (values[i] != values[j])
            return 0;
    }

    return 1;
}
